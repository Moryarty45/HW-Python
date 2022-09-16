N = int(input("Введите число: "))
arr = []
i = 2 

while i <= N:
    if N % i == 0:
        arr.append(i)
        N //= i
        i = 2
    else:
        i += 1

print(f"Простые множители введенного числа: {arr}")