x_a = int(input('Введите координату "x" точки A:\n'))
y_a = int(input('Введите координату "y" точки A:\n'))
x_b = int(input('Введите координатy "x" точки B:\n'))
y_b = int(input('Введите координатy "y" точки B:\n'))
print (round( (((x_a-x_b)**2) + ((y_a-y_b)**2)) **0.5, 3))