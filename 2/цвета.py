'x = str(input("Введите название цвета"))'
'x2 = str(input("Введите название цета"))'
x, x2 = input(), input()
if x != "красный" and x != "синий" and x != "желтый":
    print(" ****")
elif x2 != "красный" and x2 != "синий" and x2 != "желтый":
    print(" $$$$")
elif (x == "желтый") and (x2 == "синий"):
        print("При смешении зеленый")
elif (x == "красный") and (x2 == "синий"):
        print("При смешении фиолетовый")
elif (x == "желтый") and (x2 == "красный"):
        print("При смешении оранжевый")
elif (x == "синий") and (x2 == "красный"):
        print("При смешении фиолетовый")
elif (x == "красный") and (x2 == "желтый"):
        print("При смешении оранжевый")
elif (x == "синий") and (x2 == "желтый"):
        print("При смешении зеленый")
else:
    print("такой цвет не входит в три основных")