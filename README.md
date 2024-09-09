# Face-Detection-And-Blurring-With-OpenCV-And-MediaPipe
Face Detection And Blurring With OpenCV And MediaPipe

This project demonstrates face detection and blurring using OpenCV and MediaPipe. It captures video from a webcam, detects faces in real-time, and applies a blur effect to the detected faces.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [Example Images](#Example-Images)

## Installation

To run this project, you need to have Python installed along with the required libraries. Follow the steps below to set up the environment:

1. Clone the repository:
    ```sh
    git clone https://github.com/AbdullahUsama/face-detection.git
    cd face-detection
    ```

2. Create a virtual environment (optional but recommended):
    ```sh
    python -m venv venv-name
    On Windows use `venv-name\Scripts\activate`
    ```

3. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To run the face detection and blurring application, execute the following command:

```sh
python face-detection.py
```
Press q to quit the application.

## How It Works
The script performs the following steps:

1. Captures video from the webcam using OpenCV.
2. Converts the captured frames to RGB format.
3. Uses MediaPipe's Face Detection module to detect faces in the frames.
4. For each detected face, calculates the bounding box coordinates.
5. Applies a blur effect to the detected face region.
6. Draws a rectangle around the blurred face.
7. Displays the processed frames in a window.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue.

## Example Images

**Face Detection:**

![image](https://github.com/user-attachments/assets/b5ddd636-178b-4f43-a871-eaa341659571)

**Face Blur:**

![image](https://github.com/user-attachments/assets/8a82dfc0-2491-4373-9a8c-cab6e0f81f81)

   
