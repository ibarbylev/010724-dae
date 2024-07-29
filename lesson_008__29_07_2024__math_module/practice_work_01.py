"""Правильный многоугольник — выпуклый многоугольник,
у которого равны все стороны и все углы между смежными сторонами.
Площадь правильного многоугольника с длиной стороны a и количеством сторон n
вычисляется по формуле:

S = n * a^2 / (4 * tg(PI/n))

Даны два числа: натуральное число n и вещественное число a.
Напишите программу, которая находит площадь указанного правильного многоугольника.

Формат входных данных:
На вход программе подаётся два числа n и a.

Формат выходных данных:
Программа должна вывести вещественное число – площадь многоугольника.

"""

# ---------------- удалить отсюда ----------------
import math

n, a = 5, 3.5

area = (n * a ** 2) / (4 * math.tan(math.pi / n))

print(area)
# 21.075848157214846