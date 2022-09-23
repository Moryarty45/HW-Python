import random

def list (num):
    list_elements = []
    for i in range(num):
        list_elements.append (random.randint (i, num+1))
    print(f"Список {list_elements}")
    return list_elements;

list_quantity = int(input("Длина списка = "))
new_list = list(list_quantity);
print(sum(new_list[item] for item in range(1, len(new_list), 2)))