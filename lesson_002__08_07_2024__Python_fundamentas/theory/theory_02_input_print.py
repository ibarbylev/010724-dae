"""Копируем содержимое предыдущего файла и меняем
stdin и stdout на input() и print()
"""
import sys


print("Введите что-нибудь: ")

input_data = input()

print(f"Это сообщение печатается в стандартном выводе\n")
print(f"Вы только что ввели с клавиатуры: <{input_data}\n>")
