
# ✋ EmojiWave: Transforming Hand Gestures into Emojis

## 📋 Project Overview

**EmojiWave** is a web application that uses computer vision to detect hand gestures in real-time. It then translates these gestures into corresponding emojis using a custom-trained Convolutional Neural Network (CNN). The app leverages **Streamlit** for an interactive user experience, enabling users to either upload an image or use their webcam for real-time gesture recognition.

## 🎬Live Demo
 Experience EmojiWave in Action: (https://emojiwaveapp.streamlit.app/)

## 🚀 Key Features
- **Real-time emoji feedback:** Detects hand gestures via webcam or uploaded images and displays corresponding emojis.
- **Interactive experience:** Fun and personal interaction without the need for touch or voice inputs.
- **Portable deployment:** Easily deployed via Docker for seamless use across different environments.

## 🔧 Tech Stack
- **Python**
- **TensorFlow** (for deep learning)
- **OpenCV** (for computer vision)
- **Streamlit** (for interactive web interface)
- **Jupyter / Google Colab** (for model development)
- **Docker** (for containerized deployment)
- **VS Code** (for development)

## 📸 How It Works
1. **Upload an image** or use your **webcam** for gesture recognition.
2. The system processes the image, detecting hand gestures.
3. The recognized gesture is matched to an emoji and displayed on the screen.


## 📂 Project Structure

```
EmojiWave/
├── api/                         # API files
│   ├── fast.py                  # FastAPI application server
│   ├── model.py                 # Model architecture
│   └── preprocessor.py          # Data preprocessing functions
├── models/                      # Directory for trained models
│   └── final_model_acc99.h5     # Final trained model with 99% accuracy
├── notebooks/                   # Jupyter notebooks
│   ├── Baseline_Model.ipynb     # Notebook for baseline model training
│   ├── EDA.ipynb                # Exploratory Data Analysis notebook
│   ├── Preprocess.ipynb         # Notebook for data preprocessing
│   └── The Best Model.ipynb     # Notebook for fine-tuning the best model
├── outputs/plots/               # Directory for storing model output
│    ├── baseline.jpeg           # Visualization of baseline model results
│    └── best_model.jpeg         # Visualization of best model results
├── streamlit_app/               # Directory for the Streamlit app
│   ├── .streamlit/              # Streamlit configuration
│   │   └── config.toml          # Configuration file for Streamlit app
│   ├── pages/                   # Subdirectory for Streamlit app pages
│   │   ├── CameraInput.py       # Page for capturing input from camera
│   │   ├── MoreResources.py     # Page for additional resources
│   │   └── UploadImage.py       # Page for uploading an image
│   ├── EmojiWaveLogo.gif        # GIF logo
│   └── Home.py                  # Main homepage of the Streamlit app
├── .gitignore                   # Git ignore rules
├── project_summary.txt          # Summary of the project
├── README.md                    # Project documentation
└── requirements.txt             # List of project dependencies
```



## 💻 How to Run the Project Locally

To run the app on your local machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/noura-alzahrani/EmojiWave.git
   ```

2. Install required dependencies:
   ```bash
   cd EmojiWave
   pip install -r requirements.txt
   ```

3. Launch the app using Streamlit:
   ```bash
   streamlit run streamlit_app/app.py
   ```

---

## 👥 Acknowledgments

Shoutout to my incredible team for making EmojiWave happen:

- [**Mohammed Albaijan**](https://github.com/moalb08)
- [**Norah Alharbi**](https://github.com/NourahNH)
- [**Amal Alahmadi**](https://github.com/amal-Stu)
- [**Yousif Alnasser**](https://github.com/ai-yousif)
