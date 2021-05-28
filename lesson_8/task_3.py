class OwnErrorNum(Exception):
    switch = True

    def __init__(self, num):
        self.number = num
        try:
            tmp = float(self.number)
            OwnErrorNum.switch = True
        except ValueError:
            OwnErrorNum.switch = False
            print("Вы ввели не число, повторите ввод")

    @classmethod
    def Output(cls):
        return cls.switch


print("Для выхода из программы введите q")
result = ''
while True:
    inp_str = input("Введите число и нажмите Enter: ")
    if inp_str == "q":
        break
    else:
        OwnErrorNum(inp_str)
        if OwnErrorNum.Output():
            result = result + " " + inp_str
print(result)
