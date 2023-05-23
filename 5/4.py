import random
s = []
d = dict()
f = ["В", "Г", "Ш", "И", "Я"]
y = ["японский", "китайский", "английский", "немецкий", "испанский"]
for i in f:
    p = random.choice(y)
    d[i] = p
    if p == "китайский":
       s.append(i)
print(s)
print(d)