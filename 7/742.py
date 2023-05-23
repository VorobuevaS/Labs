from PIL import Image, ImageFont
filename = "watermark.png"
with Image.open(filename) as y:
    y.load()
width, height = y.size
print(width, height)
filename = "1.jpg"
with Image.open(filename) as i:
    i.load()
i.paste(y, (0, 0), y)
i.save("D:\ 11.jpg")