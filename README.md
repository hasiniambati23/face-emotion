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


# OUTPUT
<img width="562" height="601" alt="Screenshot 2026-02-25 084612" src="https://github.com/user-attachments/assets/6332030b-8ed7-45b3-811e-030045d603d7" />
<img width="477" height="410" alt="Screenshot 2026-02-25 084545" src="https://github.com/user-attachments/assets/3d7e5e3e-0dbd-4389-8a3a-559691fd81fa" />
<img width="595" height="567" alt="Screenshot 2026-02-25 084518" src="https://github.com/user-attachments/assets/ac1be377-5dc3-4a0c-98f7-bf7bdd6efe24" />
<img width="667" height="745" alt="Screenshot 2026-02-25 084452" src="https://github.com/user-attachments/assets/8680ad89-cf2e-4a23-8a32-417ad58d1fdb" />

