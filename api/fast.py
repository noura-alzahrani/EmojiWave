from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
import io
import numpy as np
from api.preprocessor import preprocess_uploaded_image, preprocess_captured_image
from api.model import load_trained_model
app = FastAPI()


# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


model = load_trained_model("models/final_model_acc99.h5")
class_names = [
    'call_me',
    'fingers_crossed',
    'index_up',
    'okay',
    'paper',
    'rock',
    'rock_on',
    'scissor',
    'spock',
    'thumbs_up'
]

@app.get("/")
def root():
    return {"ok": True}

@app.post("/predict")
async def predict(file: UploadFile = File(...), source: str = Form(...)):
    image_bytes = await file.read()

    if source == "upload":
        img_array = preprocess_uploaded_image(image_bytes)
    elif source == "camera":
        img_array = preprocess_captured_image(image_bytes)
    else:
        return {"error": "Unknown source type"}

    prediction = model.predict(img_array)
    predicted_class = int(np.argmax(prediction))
    return {"prediction": class_names[predicted_class]}
