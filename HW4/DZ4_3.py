lst = list(map(int, input("Задайте последовательность чисел через пробел:").split()))
print(f"Ваша последовательность: {lst}")

new_lst = [e for e in set(lst) if lst.count(e) == 1]
print(f"Список из неповторяющихся элементов: {new_lst}")