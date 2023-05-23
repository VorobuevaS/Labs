
def W(a):
    d = a.split(".")
    a3 = int(d[2][2:])
    a2 = int(d[1])
    a1 = int(d[0])
    if a1*a2 == a3:
        print("Магия вне Хогвартца")
    else:
        print("Not magic")

a = input(" ")
W(a)