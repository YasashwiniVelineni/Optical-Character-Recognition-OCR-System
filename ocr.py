import cv2
import pytesseract
import numpy as np

image = cv2.imread("sample_image.png")

if image is None:
    print("Image not found!")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = cv2.GaussianBlur(gray, (5, 5), 0)


_, thresh = cv2.threshold(
    gray,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

text = pytesseract.image_to_string(thresh)

print("\nExtracted Text:\n")
print(text)

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("\nText saved to output.txt")
