def D(a):
    try:
      d = 100 / a
    except ZeroDivisionError:
        print("Введен 0! Не надо так!!!")
    except ValueError:
        print("Введено не число!")
    else:
        print(d)
a = int(input(" "))
D(a)