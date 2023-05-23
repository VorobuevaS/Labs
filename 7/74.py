from PIL import Image, ImageFont
filename = "watermark.png"
with Image.open(filename) as y:
    y.load()
"""u = y.resize((y.width // 3, y.height // 3))"""
filename = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
for file in filename:
    with Image.open(file) as i:
        i.paste(y, (50, 50), y)
        i.save("D:\ " + "new2" + file)
