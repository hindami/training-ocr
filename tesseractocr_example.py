import pytesseract
from PIL import Image, ImageOps, ImageFilter
import cv2
import numpy as np


# Basic

# img = Image.open("./samples/spanduk-pecel-lele.jpg.webp")
# img = cv2.imread("./samples/2f6ebe421be187944d109100d28d70c1.jpeg")
# text = pytesseract.image_to_string(img)
# print(text)

# with open("output.txt", "w") as output_file:
#     output_file.write(text)

# Advance
config = "--psm 6 -l eng"
# text = pytesseract.image_to_string(img, config=config)

# with open("output.txt", "w") as output_file:
#     output_fil, llkou.write(text)

# Improving accuracy


## Convert image to grayscale

# gray_image = ImageOps.grayscale(img)

# original = pytesseract.image_to_string(img, config=config)
# graying = pytesseract.image_to_string(gray_image, config=config)

# print(f"original {original}")
# print(f"graying {graying}")
# gray_image.show()


# gray_image.save("path_to_save_grayscale_image.jpg")

# Resized image
# scale_factor = 4
# resized_image = gray_image.resize(
#     (gray_image.width * scale_factor, gray_image.height * scale_factor),
#     resample=Image.LANCZOS,
# )
# text = pytesseract.image_to_string(resized_image, config=config)
# print(text)


# Resize the image to enhance details.
# scale_factor = 2
# resized_image = gray_image.resize(
#     (gray_image.width * scale_factor, gray_image.height * scale_factor),
#     resample=Image.LANCZOS,
# )

# Apply edge detection filter (find edges).
# thresholded_image = resized_image.filter(ImageFilter.FIND_EDGES)
# thresholded_image.show()
# text = pytesseract.image_to_string(thresholded_image, config=config)
# print(text)


def preprocess_for_ocr(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    mean_brightness = np.mean(gray_image)
    if mean_brightness < 100:
        gray_image = cv2.equalizeHist(gray_image)
    elif mean_brightness > 180:
        gray_image = cv2.convertScaleAbs(gray_image, alpha=1, beta=-50)

    # blurred = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # thresh = cv2.adaptiveThreshold(
    #     blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    # )

    # coords = np.column_stack(np.where(thresh > 0))
    # angle = cv2.minAreaRect(coords)[-1]
    # if angle < -45:
    #     angle = -(90 + angle)
    # else:
    #     angle = -angle

    # (h, w) = gray_image.shape[:2]
    # M = cv2.getRotationMatrix2D((w // 2, h // 2), angle, 1.0)
    # deskewed = cv2.warpAffine(
    #     thresh, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE
    # )
    # resized = cv2.resize(deskewed, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
    # return resized
    return gray_image


final_image = preprocess_for_ocr(
    "./samples/hand-write-documents-letters-and-notes-in-beautiful-handwriting-styles.webp"
)
text = pytesseract.image_to_string(final_image)

print(text)
