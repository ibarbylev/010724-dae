import time
start = time.time()
print(start)  # Прошло секунд с 01.01.1970

# ======== начало программы ==========
time.sleep(2.75)

# ======== конец программы ==========

end = time.time()
print(f"Программа выполнена за {end-start:.2f}")
