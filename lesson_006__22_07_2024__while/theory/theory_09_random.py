"""
random(): генерирует случайное число от 0.0 до 1.0
randint(): возвращает случайное число из определенного диапазона
randrange(): возвращает случайное число из определенного набора чисел
shuffle(): перемешивает список
choice(): возвращает случайный элемент списка

"""
import random

# random(): генерирует случайное число от 0.0 до 1.0
print(random.random())

# randint(): возвращает случайное число из определенного диапазона
print(random.randint(1, 100))

# randrange(): возвращает случайное число из определенного набора чисел
print(random.randrange(0, 10000, 200))

# shuffle(): перемешивает список
my_list = ['apple', 'kiwi', 'orange', 'tomato']
random.shuffle(my_list)
print(my_list)

# choice(): возвращает случайный элемент списка
my_list = ['apple', 'kiwi', 'orange', 'tomato']
print(random.choice(my_list))

