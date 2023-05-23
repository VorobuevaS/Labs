x = input("Введите пароль")
x2 = input("Введите пароль второй раз")
a = 0
b = 0
c = 0
d = 0
for i in x:

 if i.isnumeric():
    a = 1
 if i.islower():
    b = 1
 if i.isupper():
    c = 1
 if i in "@%#&":
    a = 1

if len(x) > 6 and a and b and c and d:
    print("Пароль подходит")
    if x == x2:
        print("Пароли совпадают")
    else:
        print("Пароли не совпадают")
else:
    print("Пароли неверный")