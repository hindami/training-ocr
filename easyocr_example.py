import easyocr

import cv2


# Basic

# reader = easyocr.Reader(["en"])
# result = reader.readtext("./samples/split_1.png", detail=3)

# for _, text, _ in result:
#     print(text)

# Using OpenCV
contrast = 1.1
brightness = -1

pict = cv2.imread(
    "./samples/hand-write-documents-letters-and-notes-in-beautiful-handwriting-styles.webp"
)

adjusted_image = cv2.convertScaleAbs(pict, alpha=contrast, beta=brightness)

reader = easyocr.Reader(["en"])
result = reader.readtext(adjusted_image)

for _, text, _ in result:
    print(text)

# cv2.imshow("Original Image", pict)
# cv2.imshow("Adjusted Contrast", adjusted_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
