from PIL import Image
filename = "1.jpg"
with Image.open(filename) as y:
    y.load()

y = y.resize((y.width // 3, y.height // 3))
y.show()