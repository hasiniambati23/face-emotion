import cv2
from fer import FER

# Initialize webcam and emotion detector
cap = cv2.VideoCapture(0)
detector = FER(mtcnn=True)

# Make OpenCV window full screen
cv2.namedWindow("Emotion Detection", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Emotion Detection", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    try:
        results = detector.detect_emotions(frame)
    except ValueError:
        results = []

    # Draw faces and emotions
    for face in results:
        (x, y, w, h) = face["box"]
        emotions = face["emotions"]
        dominant_emotion = max(emotions, key=emotions.get)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Changed text color from blue to purple (BGR: 128, 0, 128)
        cv2.putText(frame, dominant_emotion, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (128, 0, 128), 2)

    # Show frame using OpenCV
    cv2.imshow("Emotion Detection", frame)

    # Break on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()