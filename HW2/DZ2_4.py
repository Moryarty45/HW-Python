import random

num = int(input("Введите число: "))

def list (num):
    list_elements = []
    for i in range(- num,num + 1):
        list_elements.append (random.randint (- num, num + 1))
    return list_elements

x = int(input("Введите позицию первого элемента: "))
y = int(input("Введите позицию второго элемента: "))

def multiplication(list_elements):
    for i in range(len(list_elements)):
        mult = list_elements[x-1]*list_elements[y-1]
    print(f"Произведение чисел на позициях {x} и {y} в списке {list_elements} равно ({list_elements[x-1]} * {list_elements[y-1]}) ", mult)


multiplication(list(num))