"""Решить квадратное уравнение вида ax^2+bx+c=0"""
from math import sqrt as sqrt
print('Пример формулы квадратного уравнения: ax^2+bx+c=0')
a = float(input('Введите коэффициент a'))
b = float(input('Введите коэффициент b'))
c = float(input('Введите коэффициент c'))
D = b**2 - (4*a*c)
if D < 0:
    print('нет корней, уравнение не имеет решений')
elif D == 0:
    print('1 корень')
    print((-b + sqrt(D))/2)
elif D > 0:
    print('2 корня')
    print((-b + sqrt(D)) / 2)
    print((-b - sqrt(D)) / 2)
