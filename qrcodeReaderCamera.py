import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
 
#Error handling
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, img = cap.read()


    for barcode in decode(img):
        data = barcode.data.decode('utf-8')
        barcodeType = barcode.type
        print("QR Code Content:")
        print(data)
        (x, y, w, h) = barcode.rect
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        text = "{} ({})".format(data, barcode.type)
        cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 225), 2)


    cv2.imshow('QR Reader', img)


    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
