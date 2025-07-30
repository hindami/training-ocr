import pytesseract
from PIL import Image

img = Image.open(
    "./samples/handwrite-anything-for-you-in-neat-clear-handwriting-0a3b.webp"
)
text = pytesseract.image_to_string(img)
print(text)
