from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

video_path = "input.mp4"  # MUST exist in same folder

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video file")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.track(frame, persist=True, conf=0.5)

    frame = results[0].plot()

    cv2.imshow("Detection + Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()