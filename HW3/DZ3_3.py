import random

def list (num):
    list_elements = []
    for i in range(num):
        list_elements.append (round(random.uniform(i, num+1), 3))
    print(f"Список {list_elements}")
    return list_elements;


def diff_min_max(x):
    list_elements=[]
    half = 0
    result = 0
    for i in range(len(x)):
        half = x[i] % 1
        list_elements.append(half)
    result = round(max(list_elements) - min(list_elements), 3 )
    return result

list_quantity = int(input("Длина списка = "))
new_list = list(list_quantity);
print(f"Разница между максимальным и минимальным значением дробной части элементов: {diff_min_max(new_list)}")