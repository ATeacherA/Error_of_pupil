"""Определить существование треугольника и его тип"""
a = float(input('Введите первую сторону: '))
b = float(input('Введите вторую сторону: '))
c = float(input('Введите третью сторону: '))
if a == b == c :
    print('равносторонний')
elif (a != b) and (b!= c) and (c != a):
    print('разносторонний')
elif (a == b) or (b == c) or (c == a): 
    print('равнобедренный')
else:
    print('Ошибка значения трех сторон, такого треугольника не существует')