from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image

# Load model and processor
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")

# Load and prepare image
image = Image.open(
    "./samples/hand-write-documents-letters-and-notes-in-beautiful-handwriting-styles.webp"
).convert("RGB")
pixel_values = processor(images=image, return_tensors="pt").pixel_values

# Run OCR
generated_ids = model.generate(pixel_values)
text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

print("Extracted text:", text)
