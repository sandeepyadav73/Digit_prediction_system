# 🖊️ Handwritten Digit Recognition with Live Canvas

This project is a functional **Machine Learning application** that recognizes handwritten digits (0–9).  
It uses a **Support Vector Machine (SVM)** classifier along with an **interactive OpenCV-based drawing canvas**, allowing real-time digit recognition from user input.

---<img width="671" height="476" alt="image" src="https://github.com/user-attachments/assets/e0631b3f-b123-4460-9c3a-7ded8d0a1d61" />


## 🎯 Project Overview

- **Accuracy:** 98.61% (tested on the Scikit-learn Digits Dataset)
- **Core Technologies:** Python, Scikit-learn, OpenCV
- **Interface:** Real-time drawing canvas using mouse callback functionality

---

## 🚀 Key Features

- ✍️ **Live Prediction**  
  Draw a digit on the canvas and press **`p`** to get an instant prediction.

- ⚙️ **Smart Preprocessing**
  - Converts input to grayscale  
  - Resizes the image to **8×8 pixels**  
  - Normalizes pixel values to **0–16 scale**

- 🎮 **Interactive Controls**  
  Keyboard shortcuts for prediction, clearing the canvas, and quitting the app.

- ⚡ **High Performance**  
  Optimized SVM model ensures fast and accurate digit classification.

---

## 🛠️ Tech Stack

| Component | Technology |
|---------|------------|
| **Language** | Python 3.x |
| **Machine Learning** | Scikit-learn (SVM) |
| **Computer Vision** | OpenCV |
| **Array Processing** | NumPy |
| **Visualization** | Matplotlib |

---

## 📋 Installation & Usage

### 1️⃣ Requirements

```bash
pip install opencv-python scikit-learn numpy matplotlib
```

### 2️⃣ Running the Application

```bash
python my_digit_project.py
```

### 3️⃣ Controls

| Action | Key / Mouse |
|------|------------|
| Draw digit | Left Mouse Button + Drag |
| Predict digit | `p` |
| Clear canvas | `c` |
| Quit application | `q` |

---

## 🧠 How It Works

### 🔹 Model Training
The SVM classifier is trained using the Scikit-learn Digits Dataset.

### 🔹 Feature Engineering
Canvas input is converted to grayscale, resized to 8×8 pixels, and normalized.

### 🔹 Classification
The processed image is flattened and passed to the trained SVM model to predict the digit.

---

## 📌 Future Enhancements

- CNN-based deep learning model
- Save drawn digits as images
- GUI using Tkinter or Streamlit
- Web or mobile version

---

## 📄 License

This project is for educational purposes and open for learning and experimentation.
