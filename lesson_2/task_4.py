user_string = input('Введите строку: ')
word_list = user_string.split()
i = 0
for el in word_list:
    tmp_string = word_list[i]
    print(i + 1, '- ', tmp_string[0:10])
    i += 1
