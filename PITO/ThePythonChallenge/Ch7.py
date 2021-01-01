import requests
from io import BytesIO
from PIL import Image
import re

img = Image.open(BytesIO(requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png').content))
row = [img.getpixel((x, img.height / 2)) for x in range(img.width)]
row = row[::7]
ords = [r for r, g, b, a in row if r == g == b]
text = ''.join(map(chr, ords))
nums = re.findall(r"\d+", "".join(map(chr, ords)))
print("".join(map(chr, map(int, nums))))