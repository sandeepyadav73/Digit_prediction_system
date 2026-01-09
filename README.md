# 🖊️ Handwritten Digit Recognition with Live Canvas

This project is a functional **Machine Learning application** that recognizes handwritten digits (0–9).  
It uses a **Support Vector Machine (SVM)** classifier along with an **interactive OpenCV-based drawing canvas**, allowing real-time digit recognition from user input.

---

## 🎯 Project Overview

- **Accuracy:** 98.61% (tested on the Scikit-learn Digits dataset)
- **Core Technologies:** Python, Scikit-learn, OpenCV
- **Interface:** Real-time drawing canvas using mouse callbacks

---

## 🚀 Key Features

- ✍️ **Live Prediction**  
  Draw a digit on the canvas and press **`p`** to get an instant prediction.

- ⚙️ **Smart Preprocessing**  
  Automatically:
  - Converts input to grayscale  
  - Resizes to **8×8 pixels**  
  - Normalizes pixel values to **0–16 scale** (same as training data)

- 🎮 **Interactive Controls**  
  Quick keyboard shortcuts to predict, clear, or exit.

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

Install the required Python libraries:

```bash
pip install opencv-python scikit-learn numpy matplotlib


2️⃣ Running the Application

Run the script from your terminal:

python my_digit_project.py

3️⃣ Controls
Action	Key / Mouse
Draw digit	Left Mouse Button + Drag
Predict digit	p
Clear canvas	c
Quit application	q
🧠 How It Works
🔹 Model Training

The SVM classifier is trained on the Scikit-learn Digits Dataset, which contains 8×8 grayscale images of handwritten digits.

🔹 Feature Engineering

User-drawn digits from the canvas are:

Converted to grayscale

Resized to 8×8 pixels

Pixel intensities scaled to match dataset format

🔹 Classification

The processed image is flattened into a feature vector and passed to the trained SVM model, which predicts the most likely digit (0–9).

📌 Future Enhancements

CNN-based deep learning model

Save drawn digits as images

GUI using Tkinter or Streamlit

Mobile or web-based version

📄 License

This project is for educational purposes and open for learning, modification, and experimentation.
