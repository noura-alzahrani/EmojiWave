import tensorflow as tf
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image
import io


def load_and_prcess_data(DATA_PATH, IMG_SIZE=224, BATCH_SIZE=32, SEED=42, augment=True):
    AUTOTUNE = tf.data.AUTOTUNE
    normalization_layer = tf.keras.layers.Rescaling(1./255)

    train_ds = tf.keras.utils.image_dataset_from_directory(
        DATA_PATH,
        validation_split=0.2,
        subset="training",
        seed=SEED,
        image_size=(IMG_SIZE, IMG_SIZE),
        batch_size=BATCH_SIZE
    )

    val_ds = tf.keras.utils.image_dataset_from_directory(
        DATA_PATH,
        validation_split=0.2,
        subset="validation",
        seed=SEED,
        image_size=(IMG_SIZE, IMG_SIZE),
        batch_size=BATCH_SIZE
    )

    data_augmentation = tf.keras.Sequential([
        tf.keras.layers.RandomFlip("horizontal"),
        tf.keras.layers.RandomRotation(0.05),
        tf.keras.layers.RandomZoom(0.1),
        tf.keras.layers.RandomTranslation(0.1, 0.1)
    ])

    def to_grayscale(image, label):
        image = tf.image.rgb_to_grayscale(image)
        return image, label

    def preprocess(ds, is_train=False):
        ds = ds.map(to_grayscale, num_parallel_calls=AUTOTUNE)
        ds = ds.map(lambda x, y: (normalization_layer(x), y), num_parallel_calls=AUTOTUNE)
        if is_train and augment:
            ds = ds.map(lambda x, y: (data_augmentation(x), y), num_parallel_calls=AUTOTUNE)
        ds = ds.cache()
        ds = ds.prefetch(buffer_size=AUTOTUNE)
        return ds

    train_ds = preprocess(train_ds, is_train=True)
    val_ds = preprocess(val_ds, is_train=False)

    return train_ds, val_ds

def preprocess_crop_and_predict2(img_path, model, class_names, img_size=64, margin=20):
    # 1. قراءة الصورة
    img_bgr = cv.imread(img_path)
    assert img_bgr is not None, "الصورة غير موجودة أو المسار خطأ"

    # 2. تحويل إلى رمادي
    img_gray = cv.cvtColor(img_bgr, cv.COLOR_BGR2GRAY)

    # 3. عكس الألوان
    img_inverted = cv.bitwise_not(img_gray)

    # 4. تطبيق Threshold
    _, thresh = cv.threshold(img_inverted, 50, 255, cv.THRESH_BINARY)

    # 5. العثور على أكبر كونتور
    contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    if contours:
        largest_contour = max(contours, key=cv.contourArea)
        x, y, w, h = cv.boundingRect(largest_contour)

        # نضيف هامش حول القص
        x_margin = max(x - margin, 0)
        y_margin = max(y - margin, 0)
        x_end = min(x + w + margin, thresh.shape[1])
        y_end = min(y + h + margin, thresh.shape[0])

        cropped_thresh = thresh[y_margin:y_end, x_margin:x_end]
    else:
        cropped_thresh = thresh

    # 6. تغيير الحجم
    img_resized = cv.resize(cropped_thresh, (img_size, img_size))

    # 7. تجهيز الصورة
    img_array = img_resized.astype('float32') / 255.0
    img_array = np.expand_dims(img_array, axis=-1)
    img_array = np.expand_dims(img_array, axis=0)

    # 8. التوقع
    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction)

    # 9. عرض النتيجة
    plt.figure(figsize=(4,4))
    plt.imshow(img_resized, cmap='gray')
    plt.title(f"prediction: {class_names[predicted_class]}", fontsize=14)
    plt.axis('off')
    plt.show()

    return class_names[predicted_class]

# 1. تبييض الخلفية
def make_background_white(image):
    img_array = np.array(image)

    if len(img_array.shape) == 3:
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    else:
        gray = img_array

    _, mask = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)

    if len(img_array.shape) != 3:
        img_array = cv2.cvtColor(img_array, cv2.COLOR_GRAY2BGR)

    img_array[mask == 255] = [255, 255, 255]

    return img_array

# 2. تحسين جودة الصورة الرمادية
def enhance_image(img_gray):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    enhanced_img = clahe.apply(img_gray)
    return enhanced_img

# 3. تجهيز الصورة بعد التحسين
def preprocess_camera_image(image, img_size=64, margin=20):
    img_array = np.array(image)

    if len(img_array.shape) == 3:
        img_gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    else:
        img_gray = img_array

    # تحسين الإضاءة
    img_gray = cv2.convertScaleAbs(img_gray, alpha=1.5, beta=30)

    # تحسين التباين
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    img_gray = clahe.apply(img_gray)

    # تحسين الحواف
    img_blurred = cv2.GaussianBlur(img_gray, (3, 3), 0)

    img_inverted = cv2.bitwise_not(img_blurred)
    _, thresh = cv2.threshold(img_inverted, 50, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)

        x_margin = max(x - margin, 0)
        y_margin = max(y - margin, 0)
        x_end = min(x + w + margin, thresh.shape[1])
        y_end = min(y + h + margin, thresh.shape[0])

        cropped_thresh = thresh[y_margin:y_end, x_margin:x_end]
    else:
        cropped_thresh = thresh

    img_resized = cv2.resize(cropped_thresh, (img_size, img_size))

    img_normalized = img_resized.astype('float32') / 255.0
    img_normalized = np.expand_dims(img_normalized, axis=-1)
    img_normalized = np.expand_dims(img_normalized, axis=0)

    return img_normalized


def preprocess_uploaded_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img_array = np.array(image)

    if len(img_array.shape) == 3:
        img_gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    else:
        img_gray = img_array

    img_inverted = cv2.bitwise_not(img_gray)
    _, thresh = cv2.threshold(img_inverted, 50, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)

        margin = 20
        x_margin = max(x - margin, 0)
        y_margin = max(y - margin, 0)
        x_end = min(x + w + margin, thresh.shape[1])
        y_end = min(y + h + margin, thresh.shape[0])

        cropped_thresh = thresh[y_margin:y_end, x_margin:x_end]
    else:
        cropped_thresh = thresh

    img_resized = cv2.resize(cropped_thresh, (64, 64))

    img_normalized = img_resized.astype('float32') / 255.0
    img_normalized = np.expand_dims(img_normalized, axis=-1)
    img_normalized = np.expand_dims(img_normalized, axis=0)

    return img_normalized

def preprocess_captured_image(image_bytes, img_size=64, margin=20):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img_array = np.array(image)

    if len(img_array.shape) == 3:
        img_gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    else:
        img_gray = img_array

    # نرفع الإضاءة قليلاً
    img_gray = cv2.convertScaleAbs(img_gray, alpha=1.3, beta=25)

    # نحسن التباين
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    img_gray = clahe.apply(img_gray)

    img_inverted = cv2.bitwise_not(img_gray)
    _, thresh = cv2.threshold(img_inverted, 60, 255, cv2.THRESH_BINARY)  # رفعت الثريشولد شوي

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)

        x_margin = max(x - margin, 0)
        y_margin = max(y - margin, 0)
        x_end = min(x + w + margin, thresh.shape[1])
        y_end = min(y + h + margin, thresh.shape[0])

        cropped_thresh = thresh[y_margin:y_end, x_margin:x_end]
    else:
        cropped_thresh = thresh

    img_resized = cv2.resize(cropped_thresh, (img_size, img_size))

    img_normalized = img_resized.astype('float32') / 255.0
    img_normalized = np.expand_dims(img_normalized, axis=-1)
    img_normalized = np.expand_dims(img_normalized, axis=0)

    return img_normalized
