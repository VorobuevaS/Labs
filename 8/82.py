from PIL import Image, ImageFont, ImageDraw

s = {'8 марта': 'lab8/1.jpg', '23 февраля': 'lab8/2.jpg',
    'новый год': 'lab8/3.jpg', '1 сентября': 'lab8/4.jpg'}

i = input('К какому празднику нужна открытка?')
k = Image.open(s[i])
k.show()