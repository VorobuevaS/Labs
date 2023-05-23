a = open("3.txt", 'r')
x = a.readlines()
print(x)
d = []
t = ","
p = 0
b = open("3new.txt", 'w')
for i in range(6):
    x[i] = x[i].rstrip("\n")
    print(x[i])
    y = x[i].split("-")
    d.append(y[0])
    print(y)
    j = y[0]
    y[0] = y[1]
    y[1] = j
    if t in y[0]:
        r = y[0].split(",")
        d.append(r[0])
        d.append(r[1])
        s = r[0] + " - " + y[1]
        s1 = r[1] + " - " + y[1]
        b.write(s + "\n")
        b.write(s1 + "\n")
    else:
        d.append(y[0])
        s = y[0] + " - " + y[1]
        b.write(s + "\n")
    print(s)
print(d)
for i in range(len(d)):
    p = 0
    for m in range(len(d)):
        if d[i] == d[m]:
            p += 1
            if p == 2:
                e = d[i]

print(e)
a.close()
b.close()
g = 0
file = open("3new.txt", 'r')
z = file.readlines()
print(z)
for i in range(len(z)):
    if e in z[i]:
        g += 1
        if g == 2:
            w = z[i].rstrip("\n").split("-")
print(w)
for i in range(len(z)):
    if e in z[i]:
        o = z[i].rstrip("\n").split("-")
        l = o[0] + " - " + o[1] + ", " + w[1]
        b = open("3new.txt", 'a')
        b.write(l)
        b.close()
        b = open("3new.txt", 'r')
        lol = b.readlines()
        lol.pop(i)
        lol.pop(i)
        print(lol)
        b.close()
        break
b = open("3new.txt", 'w')
for i in range(len(lol)):
     b.write(lol[i])





