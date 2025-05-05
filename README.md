
# Project Overview: EmojiWave Project: Real-Time Hand Gesture Recognition with Emoji Feedback
This project was built during an 8-day sprint in the Saudi Digital Academy’s Data Science Bootcamp, in partnership with Le Wagon.

It detects hand gestures from a webcam or uploaded image, predicts the gesture using a custom-trained CNN model, and displays the corresponding emoji on-screen using Streamlit.

Our project is an intelligent interactive system that recognizes hand gestures in real-time using a camera and instantly displays the corresponding emoji—no touch or voice required.

# Why This Project Matters
Interacting with machines should be natural, inclusive, and touchless when needed. Our system offers an alternative interaction model that is not only fun, but potentially life changing for users with accessibility needs, presenters, and more.

# Team Members
- Noura Alzahrani
- Norah Alharbi
- Amal Alahmadi
- Mohammed Albaijan
- Yousif Alnasser

# Tech Stack
- Python
- TensorFlow
- OpenCV
- Streamlit
- Jupyter / Google Colab
- Docker
- VS Code

#Challenges & Solutions
#1. Low Accuracy with Camera Input
- Problem: Model failed to predict correctly using real-time camera images.
- Cause: Camera input looked different from training data.
- Solution: Built 3 separate preprocessing pipelines for:
  - Training data
  - Uploaded images
  - Webcam frames

#2.Choosing the Right Model
- We tested both pretrained and custom models.
- Our best-performing model was built from scratch, reaching 99% accuracy after tuning.

#3.Time Constraints
- Project duration: 8 days only.
- Each team member worked on specific tasks with high coordination.

#Features
- Upload an image OR use your webcam live
- Real-time emoji overlay based on predicted gesture
- Fun, personal experience
- Portable deployment via Docker

# Future Enhancements
- Assign functionality to gestures (volume, slides, etc.)
- Transparent/no UI mode
- Multi-user recognition
- Wider gesture/emotion recognition

# How to Run
1. Clone the repo
2. Install requirements
3. Launch Streamlit:
```bash
streamlit run app.py
