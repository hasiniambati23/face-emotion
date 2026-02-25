# Face Emotion Detection

A real-time face emotion detection application using your webcam. This project detects human emotions like happy, sad, angry, surprised, and more, and displays the dominant emotion on the video feed.

# Features

- Real-time emotion detection using FER library.

- Supports multiple faces in a single frame.

- Shows dominant emotion with a small emoji (optional enhancement).

- Fullscreen display for better visualization.

- Colored bounding box and text for detected faces (purple text).

# Requirements

- Python 3.8+

- OpenCV

- FER (Facial Expression Recognition) library

- MTCNN for face detection (optional, improves accuracy)

# Installation

Clone the repository (or download the files):

git clone <your-repo-url>
cd face-emotion-detection

# Install required packages:

- pip install opencv-python fer mtcnn

Note: If you face issues with mtcnn, you can remove mtcnn=True from the detector initialization.

# Usage

1. Run the Python script:

   python emotion_demo.py

- Allow access to your webcam if prompted.

- The application will show a fullscreen window displaying your face(s) with detected emotions and emojis.

- Press q to quit the application.
