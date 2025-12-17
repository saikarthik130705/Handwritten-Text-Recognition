import easyocr
from pdf2image import convert_from_path
import os
import numpy as np


# CONFIG

INPUT_PDF = "Handwriting_Sample_English.pdf"
OUTPUT_TEXT_FILE = "extracted_text.txt"

OCR_LANGUAGES = ['en'] 


# Initialize OCR Reader

reader = easyocr.Reader(OCR_LANGUAGES, gpu=False)


# Convert PDF to images

images = convert_from_path(
    INPUT_PDF,
    dpi=300,
    poppler_path=r"C:\poppler\poppler-25.12.0\Library\bin"
)


all_text = []


# OCR each page

for page_no, image in enumerate(images, start=1):
    print(f"Processing page {page_no}...")
    
    image_np = np.array(image)
    results = reader.readtext(image_np)


    for (_, text, confidence) in results:
        all_text.append(text)


# Save extracted text

os.makedirs("output_text", exist_ok=True)

with open(OUTPUT_TEXT_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(all_text))

print("\n✅ Handwritten text extracted successfully!")
print(f"Saved to: {OUTPUT_TEXT_FILE}")
