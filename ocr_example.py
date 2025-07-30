# from PIL import Image, ImageFilter, ImageEnhance
# import pytesseract
# import cv2
# import numpy as np

# # Load image using OpenCV
# image_path = "./samples/handwrite-anything-for-you-in-neat-clear-handwriting-0a3b.webp"
# img = cv2.imread(image_path)

# # Convert to grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Apply Gaussian Blur to reduce noise
# blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# # Apply thresholding to binarize the image
# _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# # Optional: apply dilation to strengthen characters
# kernel = np.ones((2, 2), np.uint8)
# dilated = cv2.dilate(thresh, kernel, iterations=1)

# # Save temp processed image
# processed_path = "processed_image.png"
# cv2.imwrite(processed_path, dilated)

# # Use Tesseract on processed image
# text = pytesseract.image_to_string(Image.open(processed_path))

# print("Extracted Text:\n", text)

import pytesseract
from PIL import Image

img = Image.open(
    "./samples/handwrite-anything-for-you-in-neat-clear-handwriting-0a3b.webp"
)
text = pytesseract.image_to_string(img)
print(text)
