# AI & Computer Vision Mini Projects

This repository contains a set of mini-projects built using **OpenCV** and Python. Each project focuses on a different aspect of computer vision—ranging from basic image operations to real-time face detection and emotion recognition using a webcam.

These projects are ideal for beginners exploring how AI can be used with live camera feeds for fun and practical applications.

---

## What's Inside?

### 1. **BGR to Gray Image Conversion**
Converts a color image to grayscale using OpenCV. Includes display and saving functionality. Great for understanding how image color spaces work.

> 📂 File: `(1)BGR_To_GRAY_Image_Conv.py`

---

### 2. **Capture Image from Camera**
Snaps a photo using your laptop's webcam and saves it instantly.

> 📂 File: `(2)Camera_Feed.py`

---

### 3. **Color Tuning with HSV Trackbars**
Allows you to tune HSV (Hue, Saturation, Value) values using trackbars to isolate specific colors from a live webcam feed. Useful for object tracking based on color.

> 📂 File: `(3)Color_Tuning_Based_On_HSV_Value.py`

---

### 4. **Basic Face Detection**
Real-time face detection using Haar Cascade classifier. Detects faces and highlights them with bounding boxes.

> 📂 File: `(4)Face_Detection.py`

---

### 5. **Face Detection with Image Capture**
Same as above, but also includes counting and capturing 30 face images with labeling like “person detected”.

> 📂 File: `(5)Face_Detection-2.py`

---

### 6. **Moving Object Detection**
Detects movement in the video feed. Helpful in surveillance applications. Tracks and counts moving objects based on frame differences.

> 📂 File: `(6)Moving_Object_Detection.py`

---

### 7. **Object Tracking Based on Color**
Tracks a colored object (e.g., a blue ball) in real time and gives directional feedback like "Left", "Right", or "Stop" depending on its position and size.

> 📂 File: `(7)Object_Tracking_Based_On_Colour.py`

---

### 8. **Face Emotion Recognition**
Uses a pre-trained model to detect human emotions such as happy, sad, angry, etc., in real-time through your webcam.

> 📂 File: `(8)face_emotion_recog.py`  
> ⚠️ Requires `facial_emotion_recognition` library

---

## Tools & Libraries

- **Python 3.8+**
- **OpenCV**
- **NumPy**
- **imutils**
- **facial_emotion_recognition** (for emotion detection project)

---

## How to Run

1. Clone the repo or download the ZIP  
2. Open any script in a Python environment (like VS Code or Jupyter)  
3. Install required packages:
```bash
pip install opencv-python imutils facial-emotion-recognition
