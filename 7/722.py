from PIL import Image
filename = "1.jpg"
with Image.open(filename) as img:
    img.load()

img = img.resize((img.width // 3, img.height // 3))
img.show()
img.save('D:\ 1copy.jpg')
img = img.transpose(Image.FLIP_TOP_BOTTOM)
img.show()
img.save('D:\ 1copy2.jpg')