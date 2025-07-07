import cv2
import os
from pyzbar.pyzbar import decode

image_path = 'QRImages/Data Structure-QRcode.png'

#Error handling 
if not os.path.exists(image_path):
    print(f"ERROR File not found: {image_path}")
    exit()

img = cv2.imread(image_path)

if img is None:
    print(f"ERROR Unable to read image: {image_path}")
    exit()

for barcode in decode(img):
    data = barcode.data.decode('utf-8')
    print("QR Code Content:")
    print(data)