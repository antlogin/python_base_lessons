f = open("my_file.txt", 'w')
my_str: str = input("Вводите строки (пустая строка - окончание ввода): ") + "\n"
while len(my_str) > 1:
    f.write(my_str)
    my_str = input() + "\n"
f.close()