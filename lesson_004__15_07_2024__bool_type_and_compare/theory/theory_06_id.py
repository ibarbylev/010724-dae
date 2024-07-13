x = 5
print(id(x))  # 12181448

a = 4
b = 4
c = 5

print(id(a) == id(b))  # True
print(id(a) == id(c))  # False

a += 1
print(id(a) == id(b))  # False
print(id(a) == id(c))  # True
