import random

def list (num):
    list_elements = []
    for i in range(num):
        list_elements.append (random.randint (i, num+1))
    print(f"Список {list_elements}")
    return list_elements;

def sum_odd_index(new_list):
    new_list_num = new_list[1::2]
    sum = 0
    for i in range(len(new_list_num)):
        sum = sum + new_list_num[i]
    return print(sum);

list_quantity = int(input("Длина списка = "))
new_list = list(list_quantity);
sum_odd_index(new_list)