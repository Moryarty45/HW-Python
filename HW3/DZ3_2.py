import random

def list (num):
    list_elements = []
    for i in range(num):
        list_elements.append (random.randint (i, num+1))
    print(f"Список {list_elements}")
    return list_elements;

def prod_list(x):
    new_list= []
    prod = 0
    if len(x)%2 == 1:
        for i in range(len(x)//2 + 1):
            if i == 0:
                prod = x[i] * x[-1]
            else:
                prod = x[i] * x[-i -1]
            new_list.append(prod)
    else:
        for i in range(len(x)//2 ):
            if i == 0:
                prod = x[i] * x[-1]
            else:
                prod = x[i] * x[-i -1]
            new_list.append(prod)
    return new_list

list_quantity = int(input("Длина списка = "))
new_list = list(list_quantity);
print(prod_list(new_list));