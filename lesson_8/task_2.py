class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data1 = input("Введите первое число: ")
inp_data2 = input("Введите второе число: ")

try:
    inp_data1 = float(inp_data1)
    inp_data2 = float(inp_data2)
    if inp_data2 == 0:
        raise OwnError("Делитель равен 0!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Результат: {inp_data1 / inp_data2}")
