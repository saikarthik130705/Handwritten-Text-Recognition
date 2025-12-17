# Handwritten Text Recognition from PDF

This project extracts handwritten text from PDF files and saves the recognized text into a plain text (.txt) file using Python. It demonstrates an end-to-end Handwritten Text Recognition (HTR) pipeline suitable for scanned documents.

## The project was developed as part of my FLSmidth internship task to explore OCR techniques beyond printed text.

## ⚙️ Tech Stack

Python 3.10+,
EasyOCR – handwriting-capable OCR engine, 
pdf2image – PDF to image conversion, 
Poppler – PDF rendering backend (Windows requirement), 
NumPy – image format conversion

## ⚠️ Limitations

Handwriting recognition accuracy depends heavily on:

    Writing clarity
    Scan quality
    Page resolution
    Cursive or highly stylized handwriting may reduce accuracy
    This is a best-effort OCR system, not a guaranteed transcription tool