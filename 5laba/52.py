sp = ["1", "2", "4", "2"]
max = -1
for i in range(4):
    e = sp.count(i)
    if max < e:
        max = e
        t = i