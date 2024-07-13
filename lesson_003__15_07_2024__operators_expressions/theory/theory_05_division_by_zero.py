from decimal import Decimal, getcontext, DivisionByZero, InvalidOperation

# Создание нового контекста
context = getcontext().copy()
context.traps[DivisionByZero] = False  # Отключение исключения деления на ноль

# Установка нового контекста
getcontext().clear_traps()
getcontext().traps[DivisionByZero] = False
getcontext().traps[InvalidOperation] = False

# Пример деления на ноль
result = Decimal('1') / Decimal('0')
print("Результат деления на ноль:", result)
result = Decimal('-1') / Decimal('0')
print("Результат деления на ноль:", result)