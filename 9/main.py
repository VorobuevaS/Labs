from pathlib import Path
from PIL import Image, ImageFilter
n = ''
y = Path(n).glob('*')
Path('dir').mkdir(parents=True, exist_ok=True)
for f in y:
    if f.suffix in ['.jpg', '.png']:
        with Image.open(f) as i:
            i.load()
            a = i.filter(ImageFilter.CONTOUR)
            a.show()
            a.save(Path('dir', a))