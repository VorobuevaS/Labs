from pathlib import Path
from PIL import Image, ImageFilter
filename = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jfif"]
for file in filename:
    with Image.open(file) as i:
        i.load()
        a = i.filter(ImageFilter.CONTOUR)
        a.show()
        Path('new-dir')
        Path('new-dir') + a