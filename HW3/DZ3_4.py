x = int(input("Введите число: "))
y = "";
 
while x > 0:
    y = str(x % 2) + y
    x = x // 2
 
print(f"Двоичное число равно {y}");