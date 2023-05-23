from tkinter import *
def z1():
    class Restaurant:
        def __init__(self, rest_n, c_t):
            self.rest_n = rest_n
            self.c_t = c_t

        def describe_restaurant(self):
            print(f"Name of restaurant {self.rest_n}, kitchen: {self.c_t}")
    class IceCreamStand(Restaurant):
        def __init__(self, rest_n, c_t, flavors, time, local):
            super().__init__(rest_n, c_t)
            self.flavors = flavors
            self.local = local
            self.time = time
        def doby(self):
            print("Виды:")
            print(*self.flavors, sep="\n")
        def noydoby(self):
            e = input()
            s.append(e)
            s.pop(0)
            print("New")
            print(*self.flavors, sep="\n")
        def proverka(self):
            e2 = input()
            for i in s:
                if e2 == i:
                    print("esty")
    class LOL(IceCreamStand):
        def __init__(self, rest_n, c_t, flavors, time, local, vidupak):
            super().__init__(rest_n, c_t, flavors, time, local)
            self.vidupak = vidupak
        def sss(self):
            self.vidupak = "stakan"
            print("vid ypakovki:")
            print(self.vidupak)
    class OL(IceCreamStand):
        def __init__(self, rest_n, c_t, flavors, time, local, vidupaki):
            super().__init__(rest_n, c_t, flavors, time, local)
            self.vidupaki = vidupaki
        def ss(self):
            self.vidupaki = "iskimo"
            print("vid ypakovki:")
            print(self.vidupaki)
    s =["ванильное", "клубничное"]
    p = IceCreamStand(" Ларек", "Мороженное ", s, "c 10:00 do 23:00", "St.Petersdurg")
    x = LOL(" Ларек", "Мороженное ", s, "c 10:00 do 23:00", "St.Petersdurg", " ")
    y = OL(" Ларек", "Мороженное ", s, "c 10:00 do 23:00", "St.Petersdurg", " ")
    p.describe_restaurant()
    p.doby()
    p.noydoby()
    x.sss()
    y.ss()
    p.proverka()
z1()
def z3():
    class Restaurant:
        def __init__(self, rest_n, c_t):
            self.rest_n = rest_n
            self.c_t = c_t

        def describe_restaurant(self):
            print(f"Name of restaurant {self.rest_n}, kitchen: {self.c_t}")
    class IceCreamStand(Restaurant):
        def __init__(self, rest_n, c_t, flavors, time, local):
            super().__init__(rest_n, c_t)
            self.flavors = flavors
            self.local = local
            self.time = time
        def doby(self):
            print(*self.flavors, sep="\n")

        def noydoby(self):
            e = input()
            s.append(e)
            s.pop(0)
            print("New")
            print(*self.flavors, sep="\n")

    s = ["ванильное", "клубничное", "шоколадное"]
    p = IceCreamStand(" Ларек", "Мороженное ", s, "c 10:00 do 23:00", "St.Petersdurg")
    p.describe_restaurant()
    p.doby()
    u = Tk()
    u['bg'] = "lightyellow"
    u.title("Мороженка")
    u.geometry('300x250')

    "f = Frame(u, bd=5 )"
    "f.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)"
    t = Label(u, text = "Виды мороженного", bg = "lightyellow", font = 30)
    t.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)
    t.pack()


    for i in s:
           e = i
           o = Label(u, text = e, bg = "lightyellow", font = 24)
           o.pack()
    u.mainloop()
z3()


