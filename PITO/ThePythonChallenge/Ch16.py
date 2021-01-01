from PIL import Image, ImageChops

image = Image.open(r"ThePythonChallenge\Resources\mozart.gif")

for y in range(image.size[1]):
    box = 0, y, image.size[0], y + 1
    row = image.crop(box)
    bytes = row.tobytes()
    i = bytes.index(195)
    row = ImageChops.offset(row, -i)
    image.paste(row, box)

image.save(r"ThePythonChallenge\Resources\level16-result.gif")