from PIL import Image, ImageFont, ImageDraw

i = Image.open('lab8/8 мар.jpg')
n = input('Имя, кого вы хотите поздравить?')
font = ImageFont.truetype("lab8/arial_bold.ttf", 35)
d = ImageDraw.Draw(i)
d.text((30, 60), n + ", поздравляю!", font = font, fill = 'red')
i.show()
i.save('lab8/pozdrav')