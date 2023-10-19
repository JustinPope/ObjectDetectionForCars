# Import YOLOv8 from ultralytics
from ultralytics import YOLO
import cv2

# Load the YOLOv8 model that is pretrained on the coco dataset 
model = YOLO('yolov8n.pt')

# Load the video file used for demonstration 
video_path = './TestingVideos/Example1.mp4'
cap = cv2.VideoCapture(video_path)

# Read the frames from the loaded video
readable = True
while readable:
    readable, frame = cap.read()

    if readable:
        
        # Detect objects using YOLOv8, and track them
        results = model.track(frame, persist=True)

        # Plot the results obtained from the object detection
        frame_ = results[0].plot()

        # Visualize the data that is obtained
        cv2.imshow('frame', frame_)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break