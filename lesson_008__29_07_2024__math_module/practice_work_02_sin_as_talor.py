"""Приближенное значение синуса можно вычислить по формуле Тейлора.

sin(x) = x - x^3/3! + x^5/5! - x^7/7! + x^9/9! - ...

Написать программу, которая
 - приблизительно вычисляет значение синуса от вводимого значения x;
 - оценивает погрешность вычисления с помощью этой формулы относительно настоящего значения,
        полученного при вызове нужной функции из библиотеки math.
"""

import math


def approximate_sin(x, n):
    result = 0
    i = 0
    while i < n:
        sign = (-1) ** i
        factorial = math.factorial(2 * i + 1)
        element = (x ** (2 * i + 1)) / factorial
        result += sign * element
        i += 1
    return result


# Угол 45 градусов в радианах
angle = math.radians(45)

# Количество членов ряда Тейлора
terms = 8

# Вычисляем приближенное значение синуса
approx_sin_value = approximate_sin(angle, terms)

print("Приближенное значение синуса:", approx_sin_value)
print("Значение синуса по стандартной библиотеке math:", math.sin(angle))
print(f"Разница {approx_sin_value - math.sin(angle)}")
