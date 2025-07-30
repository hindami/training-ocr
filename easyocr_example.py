import easyocr

reader = easyocr.Reader(
    ["ch_sim", "en"]
)  # this needs to run only once to load the model into memory
result = reader.readtext(
    "./samples/handwrite-anything-for-you-in-neat-clear-handwriting-0a3b.webp"
)

for _, text, _ in result:
    print(text)
