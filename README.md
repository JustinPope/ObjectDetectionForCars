# Simple Object Detection Software Readme
## Version 1.0
#### Date: October 19, 2023

#### Author: Justin Pope

## Table of Contents
Introduction
Features
System Requirements
Installation
Getting Started
Usage
Troubleshooting
Contributing
License
## Introduction
Welcome to the first version of my Simple Object Detection Software! This software is designed to accurately determine the distance of objects from a single camera while simultaneously identifying the object type. It leverages Python 3.10.0 and PyTorch 2.1.0 to achieve its objectives.

Object detection is a crucial task in various fields, including robotics, autonomous vehicles, surveillance, and more. My software aims to provide a simplified solution to this problem, making it accessible for developers and researchers.

This readme will guide you through the installation, usage, and customization of the software.

## Features
- Single-camera object detection
- Accurate distance estimation
- Object type classification
- Utilizes Python 3.10.0 and PyTorch 2.1.0
## System Requirements
Before running the code, ensure that your system meets the following requirements:

- Python 3.10.0
- PyTorch 2.1.0
- YOLOv8
- Appropriate IDE for running PyTorch and image processing tasks (I recommend VS code)
## Installation
1. Clone the repository from GitHub:

          git clone https://github.com/yourusername/ObjectDetectionForCars.git

2. Change to the project directory:

          cd ObjectDetectionForCars

3. Install the required dependencies using pip:

          pip3 install torch torchvision torchaudio
          pip install ultralytics

You're now ready to start using the software!

## Getting Started
1. The software uses the pre-trained coco model for object detection. You can either use a pre-trained model provided in the repository or train your own model.

2. Configure the software by editing the settings in the 'main.py' file. You can specify the camera source, model path, and other parameters as needed.

3. Run the software via your IDE.

   The software will initiate object detection and display the results in real time.

## Usage
The software provides real-time object detection and distance estimation using a single camera source.

The detected objects will be classified and displayed with bounding boxes.

You can press 'Q' to exit the software.

## Troubleshooting
If you encounter any issues while using the software, please check the following:

Ensure you have installed all the required dependencies as mentioned in the installation section.

If you encounter any errors or bugs, please report them on my GitHub repository.

## License
This software is released under the MIT License. Feel free to use, modify, and distribute it as per the terms of the license.
