"""Найти максимальное число из трех"""
print('Введите три числа')
N = 3
print('максимальное число из последовательности', max([int(input('Введите {} число: '.format(x+1))) for x in range(N)]))