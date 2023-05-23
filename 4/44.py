def W(a):
    d = 0
    d2 = 0
    e = int(len(a)/2)
    s = a[e:]
    s2 = a[:-e]
    y = len(s)
    y2 =len(s2)
    o = "1" + "0" * (y-1)
    o2 = "1" + "0" * (y2 - 1)
    o = int(o)
    o2 = int(o2)
    p = int(s)
    p2 = int(s2)
    print(o, o2)
    for i in range(1, y+1):
        b = int(p / o)
        p = p % o
        o = o/10
        d = d + b
        print(b, p, o, d)
    for i in range(1, y2+1):
        b2 = int(p2 / o2)
        p2 = p2 % o2
        o2 = o2 / 10
        d2 = d2 + b2
        print(b2, p2, o2, d2)
    print(d, d2)
    if d == d2:
        print("lucky")
    else:
        print("no lucky")
a = input(" ")
W(a)