from math import pi

d = int(input("Введите число знаков после запятой числа Пи:\n"))
print(f"Число Пи с точность в {d} знаков равно {round(pi, d)}")