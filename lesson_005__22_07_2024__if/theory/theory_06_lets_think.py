""" Давайте объединим условия для задач 2 и 4:
    если есть дождь - выполняются условия задачи 2
    если нет - условия задачи 4.
"""

is_rainy = False
other_options = "Сильный ветер?"

if is_rainy:
    print("На улице идёт дождь")
    print("Нужно взять зонт!")

else:
    if other_options == "Солнечно ли?":
        print("Сегодня солнечно.")
    elif other_options == "Идёт ли снег?":
        print("Сегодня идёт снег.")
    elif other_options == "Сильный ветер?":
        print("Сегодня сильный ветер.")
    elif other_options == "Облачно?":
        print("Сегодня облачно.")
    else:
        print('Ничего не подошло)))')
