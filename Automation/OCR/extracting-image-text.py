# in this lesson I will learning about how make use of pytesseract to extract text from images
# this useful for the tasks, such as converting image documents to text and saving them into a database

import os
import cv2
import pytesseract
from PIL import Image
from pathlib import Path

receipts_folder = Path(r"C:\Users\user\Documents\Amot The Dev\My Portfolio\Automation Skills\OCR\receipts")

c = 0
for number, image in enumerate(os.listdir(receipts_folder), start=1):
    image_path = Path.rename(receipts_folder/image, receipts_folder/f'receipt-{number}.jpeg')

    # extracting the text in each of the receipt 
    print(f'[+]Extracting data from {image_path.stem}')
    with cv2.imread(image_path) as img:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        threshold_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        ocr_config = r'--oem 3 --psm 6'
        receipt_details = pytesseract.image_to_string(threshold_img, config=ocr_config)
        print(receipt_details)
    c+=1
    if c > 3:break
