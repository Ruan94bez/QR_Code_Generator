import qrcode
import cv2
from pyzbar.pyzbar import decode

ID = "" #Place the QR code data Here

def CreateQRCode(data):
    # Creating an instance of QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Adding data to the instance
    qr.add_data(data)
    qr.make(fit=True)

    # Creating an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("QrCode.png")
    print("QR Code Generated")

def ReadQRCode(file_path):
    # Load the image using OpenCV
    img = cv2.imread(file_path)

    # Convert image to grayscale (required for QR detection)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect QR codes
    qr_codes = decode(gray_img)

    # Print the data in the QR code
    for qr_code in qr_codes:
        print("Data:", qr_code.data.decode('utf-8'))

# Generate QR Code
CreateQRCode(ID)

# Read QR Code
ReadQRCode("QRcode.png")
