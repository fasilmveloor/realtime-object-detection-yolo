# Real-time Object Detection with YOLO and Webcam

![Example GIF](example.gif)

This project demonstrates real-time object detection using the YOLO (You Only Look Once) model with a webcam feed. It leverages OpenCV for capturing video frames and the Ultralytics library for YOLO-based object detection.

## Features

- Real-time object detection using your webcam.
- YOLO model for accurate and efficient object recognition.
- Customizable threshold for object detection confidence.
- Minimal setup required to get started.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before running the project, you'll need the following:

- Python 3.x
- Pip (Python package manager)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/fasilmveloor/realtime-object-detection-yolo.git
   ```

2. Navigate to the project directory:

    ```bash
    cd realtime-object-detection-yolo
    ```

3. Install the required Python packages::

    ```bash
    pip install -r requirements.txt
    ```

### Usage
1. Run the object detection script:

    ```python
    python3 main.py
    ```
    This will open a window displaying the webcam feed with real-time object detection.

2. To exit the program, press the 'Q' key.

### Customization
You can customize the project to suit your needs:

- Adjust the YOLO model weights and configuration files in the yolo_model directory if you want to use a different YOLO 
  model.
- Modify the confidence threshold in the object_detection.py script to control the sensitivity of object detection.
- Explore additional options provided by the Ultralytics library for advanced YOLO configuration.
