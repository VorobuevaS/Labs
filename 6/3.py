st = ['Иванова', 'Коршунова', 'Шарипова', 'Воробьёва']
l = ['английский', 'китайский', 'японский']
s = {}
for i in st:
    s[i] = random.choice(l)

print(s)
print(sorted(l))

for i in s:
    if s[i] == 'китайский':
        print(i)
