import sys


sys.stdout.write("Введите что-нибудь: ")

input_data = sys.stdin.readline()

sys.stderr.write(f"Здесь выводятся ошибки стандартного вывода (если они есть)\n"
                 f"поэтому этот текст красного цвета\n")

sys.stdout.write(f"Это сообщение печатается в стандартном выводе\n")
sys.stdout.write(f"Вы только что ввели с клавиатуры: <{input_data}\n>")
