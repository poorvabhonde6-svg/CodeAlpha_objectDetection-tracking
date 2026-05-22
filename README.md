🚀 Object Detection and Tracking System using YOLOv8

A real-time computer vision project that performs Object Detection and Multi-Object Tracking using state-of-the-art deep learning models. This system processes video streams (webcam or pre-recorded videos), detects multiple objects in each frame, and assigns unique tracking IDs to maintain object identity across frames.

The project is designed for real-time video analytics applications such as surveillance systems, traffic monitoring, smart city solutions, and AI-based automation systems.

📌 Project Description

This system uses a pre-trained YOLOv8 deep learning model to detect objects in real-time video frames. After detection, it applies a tracking mechanism that assigns and maintains unique IDs for each detected object across consecutive frames.

Each frame is processed using OpenCV, and results are visualized with:

Bounding boxes
Class labels (person, car, bus, etc.)
Confidence scores
Tracking IDs

The system is optimized for speed and accuracy, making it suitable for real-time applications.

✨ Key Features
🎯 Real-time object detection using YOLOv8 (Ultralytics)
🧠 Multi-object tracking with persistent IDs
📹 Supports webcam and video file input
📦 Bounding box visualization with class labels
📊 Confidence score display for each detection
⚡ Optimized frame-by-frame processing
🔁 Continuous tracking across frames
🖥️ OpenCV-based real-time rendering window
🧩 Modular and easy-to-modify Python code
📁 Supports custom video datasets
🚀 High FPS processing for real-time performance

🛠️ Complete Tech Stack
🔹 Programming Languages
Python 3.8+
JavaScript (for web dashboard interaction)
HTML5
CSS3
🔹 Computer Vision & AI / ML
Ultralytics YOLOv8 (Object Detection Model)
PyTorch (Deep Learning Framework backend)
TorchVision (image transformations & utilities)
OpenCV (cv2) for real-time video processing
NumPy (numerical computations)
🔹 Object Tracking
ByteTrack (YOLOv8 built-in tracker)
SORT / DeepSORT (optional advanced tracking system)
Unique ID assignment system for multi-object tracking
🔹 Web Dashboard (Frontend + Backend)
Streamlit (Python-based web UI framework)
Flask (optional backend API layer if used)
HTML / CSS (UI structure & styling)
JavaScript (frontend interactivity if custom UI used)
🔹 Video Processing
OpenCV VideoCapture API
Real-time frame-by-frame processing
Webcam & video file support (.mp4, .avi)
🔹 Model & Dataset
YOLOv8 Pretrained Weights (yolov8n.pt)
COCO Dataset (80+ object classes)
Person
Car
Bicycle
Bus
Truck
Traffic Light
and more
🔹 Backend / Processing Engine
Python Processing Pipeline
Frame inference engine (YOLOv8 predictor)
Real-time detection pipeline
🔹 UI / Visualization
OpenCV GUI window (real-time detection display)
Streamlit Dashboard UI (web-based interface)
Bounding box rendering with labels + confidence scores
Tracking ID overlays
🔹 Development Tools
VS Code (IDE)
Python Virtual Environment (venv)
pip (package manager)
Git & GitHub (version control)
🔹 Deployment / Optional Enhancements
Streamlit Cloud (web deployment)
Flask API deployment
Docker (containerization optional)
ONNX (model optimization)
TensorRT (GPU acceleration)
🔹 System Requirements
Windows / Linux / macOS
Python installed (3.8+ recommended)
GPU optional (for faster inference)

🎯 Output Description

When the project runs successfully, you will see:

A live video window
Real-time object detection
Bounding boxes around objects
Class labels (Person, Car, etc.)
Confidence score (e.g., 0.85)
Unique tracking IDs for each object
Smooth frame-by-frame processing
📌 Use Cases
🏙️ Smart Surveillance Systems
🚦 Traffic Monitoring & Vehicle Counting
🧍 People Tracking in Public Spaces
🏭 Industrial Automation Monitoring
🧠 AI-based Security Systems
📊 Video Analytics for Research
🚗 Smart City Infrastructure Projects