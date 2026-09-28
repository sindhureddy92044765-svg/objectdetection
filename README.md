# YOLOv8 Object Detection System

A Python-based object detection application using **YOLOv8, OpenCV, PyTorch, and Tkinter** to detect and identify objects in images. The project provides a graphical user interface for selecting images, running YOLOv8 inference, and displaying the detection results.

## Project Overview

Object detection is a computer vision technique used to identify objects within an image and determine their locations using bounding boxes.

This project implements an **Object Detection System using YOLOv8**. It combines the YOLOv8 pre-trained detection model with OpenCV and a Tkinter-based graphical user interface.

The application allows users to:

* Select an image from the computer
* Perform object detection using YOLOv8
* Detect multiple objects in a single image
* Display bounding boxes around detected objects
* Display object names and confidence scores
* Save the detection result
* View the original and processed images through the application

## Features

### Image-Based Object Detection

Users can select an image from their computer and run YOLOv8 object detection on it.

### Bounding Box Detection

Detected objects are highlighted using bounding boxes.

### Class Identification

The system identifies detected objects using the class labels provided by the YOLOv8 model.

### Confidence Score

The detection result includes a confidence score indicating the model's confidence for each detected object.

### Graphical User Interface

The project uses **Tkinter** to provide an easy-to-use desktop interface.

### Image Processing

**OpenCV** is used for image loading, processing, and displaying detection results.

### Result Visualization

The application displays the processed image with detected objects and their corresponding labels.

## Technologies Used

| Technology  | Purpose                              |
| ----------- | ------------------------------------ |
| Python      | Main programming language            |
| YOLOv8      | Object detection                     |
| Ultralytics | YOLOv8 implementation                |
| OpenCV      | Image processing and computer vision |
| PyTorch     | Deep learning framework              |
| Tkinter     | Graphical User Interface             |
| Pillow      | Image handling in GUI                |

## Project Structure

```text
Object_detection_model/
│
├── object_detection_gui.py
├── .gitignore
├── car.jpg
├── gira.jpg
├── zebra.jpg
├── detected_result.jpg
└── README.md
```

> The YOLOv8 model weights are excluded from the Git repository through `.gitignore`.

## How YOLOv8 Works

The basic workflow of the system is:

```text
Input Image
     │
     ▼
Image Preprocessing
     │
     ▼
YOLOv8 Model
     │
     ▼
Object Detection
     │
     ├── Object Class
     ├── Bounding Box
     └── Confidence Score
     │
     ▼
Detection Result
     │
     ▼
Display / Save Result
```

## Installation

### 1. Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/anushagsoppin/Object_detection_model.git
```

Move into the project directory:

```bash
cd Object_detection_model
```

### 2. Install Required Packages

Install the required Python libraries:

```bash
pip install ultralytics opencv-python pillow torch torchvision
```

Alternatively, if a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

## YOLOv8 Model

This project uses a YOLOv8 pre-trained model for object detection.

The model can be loaded using:

```python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
```

The `yolov8n.pt` model is the lightweight YOLOv8 Nano model.

If the model file is not present locally, Ultralytics can download the required model weights when the model is initialized.

## Running the Application

Run the GUI application using:

```bash
python object_detection_gui.py
```

The application opens the graphical interface.

### Basic Workflow

1. Start the application.
2. Select an input image.
3. Run object detection.
4. YOLOv8 processes the image.
5. Detected objects are identified.
6. Bounding boxes are drawn around detected objects.
7. Detection labels and confidence scores are displayed.
8. The processed image can be saved as a result.

## Example

For an input image containing objects such as a car, giraffe, or zebra, the YOLOv8 model analyzes the image and produces a result similar to:

```text
Input Image
     │
     ▼
YOLOv8 Detection
     │
     ▼
┌───────────────────────────────┐
│ Object       Confidence       │
│ Car          0.91             │
│ Person       0.87             │
└───────────────────────────────┘
     │
     ▼
Bounding Boxes + Labels
```

The exact detected classes and confidence values depend on the input image and model prediction.

## Sample Images

The repository contains sample images used for testing the object detection system.

Example test images include:

* `car.jpg`
* `gira.jpg`
* `zebra.jpg`

The generated detection output is stored as:

```text
detected_result.jpg
```

## Model Details

The project uses **YOLOv8 Nano (`yolov8n.pt`)**, which is designed to provide a relatively lightweight object detection model suitable for experimentation and real-time applications.

YOLO performs object detection in a single inference pipeline and predicts:

* Bounding box coordinates
* Object class
* Confidence score

## Advantages

* Simple graphical interface
* Fast object detection
* Supports multiple object classes
* Uses a pre-trained deep learning model
* Easy to test with different images
* Combines computer vision and deep learning
* Suitable for learning and demonstrating object detection concepts

## Limitations

* Detection performance depends on the pre-trained model.
* Performance can vary depending on image quality and object size.
* CPU-based inference can be slower than GPU-based inference.
* The current implementation primarily focuses on image-based detection.
* Accuracy may vary for objects or environments that differ significantly from the data used to train the pre-trained model.

## Future Enhancements

Possible improvements include:

* Add reliable real-time webcam detection
* Add video file detection
* Add batch image processing
* Add configurable confidence thresholds
* Add detection history
* Add database-based user management
* Add CSV export for detection results
* Add performance metrics such as inference time
* Add support for custom-trained YOLO models
* Improve GUI design and user experience
* Add object counting functionality
* Add detection statistics and reports

## Applications

YOLO-based object detection can be used in applications such as:

* Surveillance systems
* Traffic monitoring
* Autonomous systems
* Industrial inspection
* Smart agriculture
* Retail analytics
* Wildlife monitoring
* Safety monitoring
* Computer vision research

## Learning Outcomes

Through this project, the following concepts were explored:

* Computer Vision
* Object Detection
* Deep Learning
* YOLO architecture
* Image preprocessing
* OpenCV
* PyTorch
* Model inference
* Bounding box visualization
* Confidence scores
* Python GUI development

## Requirements

Recommended environment:

```text
Python 3.x
Ultralytics
PyTorch
OpenCV
Pillow
Tkinter
```

## Author

**Anusha Girish Soppin**

Computer Science & Engineering Student

GitHub:
https://github.com/anushagsoppin

## License

This project is intended for educational and learning purposes.

## Acknowledgements

This project uses the **Ultralytics YOLOv8** framework and its pre-trained models for object detection.

Ultralytics documentation:

https://docs.ultralytics.com/

---

## Project Summary

**YOLOv8 Object Detection System** is a Python-based computer vision application that uses a pre-trained YOLOv8 model to detect objects in images. The system integrates YOLOv8 with OpenCV, PyTorch, Pillow, and Tkinter to provide object detection and result visualization through a graphical user interface.
