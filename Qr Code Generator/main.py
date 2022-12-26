# Qr Code Generator Software!
import pyqrcode


def qrcode():
    q = pyqrcode.create(input())
    q.png('qrcode.png', scale=6)
    print("Qr code generated successfully!")


if __name__ == '__main__':
    qrcode()
