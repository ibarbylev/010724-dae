"""
Напишите программу, которая запрашивает у пользователя натуральное число N
и вычисляет сумму первых N элементов следующей суммы:

1 - 1/3 + 1/5 - 1/7 +1/9


Выведите результат на экран с помощью команды print.
Используйте библиотеку decimal для вычисления суммы с большой точностью.

Пример вывода:

Введите натуральное число N: 1000
Сумма первых 1000 элементов ряда Лейбница: 0.785398163397448309615660845
"""

from decimal import Decimal


def calculate_leibniz_series_sum(N):
    total_sum = Decimal(0)
    i = 0
    while i <= N:
        sign = (-1) ** i
        denominator = 2 * i + 1
        total_sum += sign * Decimal(1) / Decimal(denominator)
        i += 1
    return total_sum


N = 1000
result = calculate_leibniz_series_sum(N)

print("Сумма первых", N, "элементов ряда Лейбница:", result)
print(f"Разница: {result - Decimal(0.785398163397448309615660845)} ")
