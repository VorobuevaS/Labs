def z51():
    io = ["1", "2", "3", "4", "5"]
    a = input(" ")
    if a in io:
       print("You win!!!")
    else:
       print("You don't win!!!")

def z52():
    sp = ["1", "4", "4", "2"]
    max = -1
    for i in range(len(sp)):
        e = sp.count(sp[i])
        if max < e:
            max = e
            t = sp[i]
    print(t)

def z53():
    n = ("пн", "вт", "ср", "чт", "пт", "сб", "вс")
    a = int(input(" "))
    for i in n:
        print(n[:-a])
        print(n[-a:])
        break
def z54():
    a = ["Иванов", "Чайников", "Гвоздь", "Лук", "Воробей"]
    b = ["Гусь", "Кирпич", "Шаман", "Серый", "Белый"]
    max = -1
    print(a)
    print(b)
    e = [ ]
    a2 = a[-2:]
    b2 = b[-2:]
    e = a2 + b2
    s = (*e,)
    t = len(s)
    print(s)
    print(t)
    r = tuple(sorted(s))
    print(r)
    fam = input(" ")
    if fam in r:
          e = r.count(fam)
          if max < e:
              max = e
    print(e)
    print(fam)
print(z54())