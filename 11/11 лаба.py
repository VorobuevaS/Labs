def z1():
    class Restaurant:
        def __init__(self, rest_n, c_t):
            self.rest_n = rest_n
            self.c_t = c_t
        def describe_restaurant(self):
            print(f"Name of restaurant {self.rest_n}, kitchen: {self.c_t}")
        def open_restaurant(self):
            print("Restaurant is open")
    newRest = Restaurant("Japan", "japanese food")
    newRest.describe_restaurant()
    newRest.open_restaurant()
z1()
def z2():
    class Restaurant:
        def __init__(self, rest_n, c_t):
            self.rest_n = rest_n
            self.c_t = c_t
        def describe_restaurant(self):
            print(f"Name of restaurant {self.rest_n}, kitchen: {self.c_t}")
        def open_restaurant(self):
            print("Restaurant is open")
    a = input()
    d = input()
    newRest = Restaurant(a, d)
    newRest.describe_restaurant()
    newRest.open_restaurant()
z2()
def z3():
    class Restaurant:
        def __init__(self, rest_n, c_t, r1):
            self.rest_n = rest_n
            self.c_t = c_t
            self.r1 = r1
        def describe_restaurant(self):
            print(f"Name of restaurant {self.rest_n}, kitchen: {self.c_t}, {self.r1}")
        def open_restaurant(self):
            print("Restaurant is open")
        def change(self):
            c = input()
            self.r1 = c
            print(f"Name of restaurant {self.rest_n}, kitchen: {self.c_t}, {self.r1}")
    a = input()
    d = input()

    newRest = Restaurant(a, d, "5")
    newRest.describe_restaurant()
    newRest.open_restaurant()
    newRest.change()
z3()