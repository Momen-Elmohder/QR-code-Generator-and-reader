import os
import qrcode

os.makedirs("QRImages", exist_ok=True)

class_name = "Data Structure"
session_id = "1234-5678"
data = f"{class_name} - Session ID: {session_id}"

qrcodeImg = qrcode.make(data)
qrcodeImg.save(f'QRImages/{class_name}-QRcode.png')
