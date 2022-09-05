plane = int(input("Введите номер плоскости: "))
if plane == 1:
    print("X и Y должны быть > 0")
elif plane == 2:
    print("X должно быть < 0, Y должен быть > 0")
elif plane == 3:
    print("X должно быть < 0, Y должен быть < 0")
elif plane == 4:
    print("X должно быть < 0, Y должен быть < 0")
else:
    print("Плоскостей всего 4!")