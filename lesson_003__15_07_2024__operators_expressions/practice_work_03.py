"""Написать программу, которая принимает несколько аргументов
и возвращает заранее заданную функцию от них.
Например, программе на вход приходят 4 числа,
записанные в разных строках – количество дней, часов, минут и секунд.
Вывести это время в секундах.
"""

SECONDS_IN_MIN = 60
SECONDS_IN_HOUR = 60 * SECONDS_IN_MIN
SECONDS_IN_DAY = 24 * SECONDS_IN_HOUR

days = int(input("Введите количество дней: "))
hours = int(input("Введите количество часов: "))
minutes = int(input("Введите количество минут: "))
seconds = int(input("Введите количество секунд: "))

total_seconds = (days * SECONDS_IN_DAY
                 + hours * SECONDS_IN_HOUR
                 + minutes * SECONDS_IN_MIN
                 + seconds)

print(f"Общее время в секундах: {total_seconds}")
