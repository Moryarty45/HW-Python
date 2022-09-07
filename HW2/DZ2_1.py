number = input("Введите число: ")
sum = 0
for i in number:
    if i != '.' and i != ',':
        sum += int(i)
print(f"Сумма цифр равна: {sum}")