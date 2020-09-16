# Taken from CS50's week 6 source code:

# Generates a QR code
# https://github.com/lincolnloop/python-qrcode

import pyqrcode

# Generate QR code
img = qrcode.create("https://youtu.be/fL308_-Kbt0")

# Save as file
img.save("qr.png", "PNG")