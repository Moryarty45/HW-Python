n = int(input("Введите число: "))

def fibonacci(n):
    fibo_num = []
    a, b = 1, 1
    for i in range(n):
        fibo_num.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n+1):
        fibo_num.insert(0, a)
        a, b = b, a - b
    return fibo_num;

print(f"Последовательность Фибоначчи для числа {n}: {fibonacci(n)}")