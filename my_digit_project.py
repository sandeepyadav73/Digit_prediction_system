import cv2
import numpy as np
from sklearn import datasets, svm
from sklearn.model_selection import train_test_split

# 1. Model Training (Aapka purana logic)
digits = datasets.load_digits()
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

classifier = svm.SVC(gamma=0.001)
X_train, X_test, y_train, y_test = train_test_split(data, digits.target, test_size=0.5, shuffle=False)
classifier.fit(X_train, y_train)

# 2. Canvas Setup
drawing = False 
canvas = np.zeros((400, 400), dtype="uint8") # Black background

def draw_digit(event, x, y, flags, param):
    global drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(canvas, (x, y), 15, 255, -1) # Safed rang se draw karein
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

cv2.namedWindow("Draw any Digit (0-9)")
cv2.setMouseCallback("Draw any Digit (0-9)", draw_digit)

print("Instructions:")
print("- Mouse se digit draw karein.")
print("- 'p' dabayein prediction ke liye.")
print("- 'c' dabayein canvas clear karne ke liye.")
print("- 'q' dabayein exit karne ke liye.")

while True:
    cv2.imshow("Draw any Digit (0-9)", canvas)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'): # Exit
        break
    
    elif key == ord('c'): # Clear
        canvas = np.zeros((400, 400), dtype="uint8")
        print("Canvas Cleared!")

    elif key == ord('p'): # Predict
        # Image ko 8x8 mein convert karna (Model ke requirement ke hisaab se)
        img_resized = cv2.resize(canvas, (8, 8), interpolation=cv2.INTER_AREA)
        
        # Scaling: Dataset 0-16 scale par hota hai, OpenCV 0-255 par
        img_normalized = (img_resized / 255.0) * 15.0
        
        # Prediction
        prediction = classifier.predict(img_normalized.reshape(1, -1))
        print(f"--- Prediction: {prediction[0]} ---")
        
        # Result ko screen par dikhane ke liye
        cv2.putText(canvas, f"Result: {prediction[0]}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)

cv2.destroyAllWindows()