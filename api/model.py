# model.py

import os
from tensorflow.keras.models import load_model

def load_trained_model(model_path="models/final_model_acc99.h5"):

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"⚠️Error:file dose not exist {model_path}")

    model = load_model(model_path)
    print(f"✅ loding model sucess: {model_path}")
    return model
