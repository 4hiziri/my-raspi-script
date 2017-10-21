from pyzbar.pyzbar import decode
from PIL import Image

image = 'test.jpg'
data = decode(Image.open(image))

print(data)
