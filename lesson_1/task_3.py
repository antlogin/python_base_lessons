doing = True
while doing:
    string_nomber_n = input("Введите число N от 0 до 9: ")
    if string_nomber_n.isdigit():
        if int(string_nomber_n) <= 9:
            print()
            print("Сумма вида N+NN+NNN равна:")
            print(int(string_nomber_n) + int(string_nomber_n + string_nomber_n) + int(
                string_nomber_n + string_nomber_n + string_nomber_n))
            doing = False
        else:
            print("Введенное число > 9")
            doing = True
    else:
        print("Введенное не является целым положительным числом")
        doing = True
