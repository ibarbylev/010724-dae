from decimal import Decimal, getcontext


# =========== числа, с точностью, указанной в аргументе ===========
number1 = Decimal('0.1')
number2 = Decimal('0.2')
result = number1 + number2
print(result)  # 0.3


# =========== числа, со стандартной точностью decimal ===========

number1 = Decimal(0.1)
number2 = Decimal(0.2)
result = number1 + number2
print(result)  # 0.3000000000000000166533453694
#                  123456789012345678901234567890
print(getcontext().prec)  # 28 знаков
