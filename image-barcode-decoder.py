import cv2
import os
from dotenv import load_dotenv
load_dotenv()

FILE_PATH = os.get('FILE_PATH')
img = cv2.imread(FILE_PATH)

bcd = cv2.barcode.BarcodeDetector()

retval, decoded_info, decoded_type, points = bcd.detectAndDecode(img)

if retval:
    frame = cv2.polylines(img, points.astype(int), True, (0, 255, 0), 3)
    cv2.imshow('Barcode Decoder', frame)
    print(decoded_info)
else:
    print("No Barcode Detected. Try again.")