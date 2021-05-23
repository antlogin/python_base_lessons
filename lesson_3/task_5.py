sum_str = 0
switch = "on"
while True:
    print("Для выхода из программы введите q.")
    inp_str = input("Или введите последовательность чисел, разделеных пробелом: ")
    tmp_list = inp_str.split()
    for i in range(len(tmp_list)):
        if tmp_list[i] == "q":
            switch = "off"
            break
        else:
            try:
                sum_str = sum_str + float(tmp_list[i])
            except ValueError:
                print("Введено недопустимое значение: ", tmp_list[i])
    print("Сумма чисел равна ", sum_str)
    if switch == "off":
        break
