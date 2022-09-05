num_day = int(input("Введите номер дня недели: "))
if num_day == 6 or num_day == 7:
    print('Выходной')
elif num_day > 7:
    print('Не существующий день недели')
else: 
    print("Рабочий день")