import csv
with open('1.csv') as f:
    R = csv.reader(f)
    X = list(R)
    w = 0
    for i in range (3):
        s = ''
        x1 = X[i]
        print(x1)
        e = x1[0]
        e2 = int(x1[1])
        e3 = int(x1[2])
        s += str(e) + ' - ' + str(e2) + 'шт. за ' + str(e3) + ' руб.'
        print("Нужно купить: ")
        print(s)
        w += e2 * e3
    print(w)