f = open("text_4.txt", 'r', encoding="utf-8")
arr_str = []
N_str = 0
avr_salary = 0
while True:
    content = f.readline()
    if content:
        content = content.rstrip()
        arr_str.append(content.split(" "))
        N_str += 1
    else:
        break
i = 0
f.close()

f = open("text_4_new.txt", 'w', encoding="utf-8")
while i < N_str:
    if arr_str[i][0] == "One":
        arr_str[i][0] = "Один"
    if arr_str[i][0] == "Two":
        arr_str[i][0] = "Два"
    if arr_str[i][0] == "Three":
        arr_str[i][0] = "Три"
    if arr_str[i][0] == "Four":
        arr_str[i][0] = "Четыре"
    # и т.д.
    # Можно, конечно, через словарь сделать
    # или написать отдельную функцию, но так быстрее,
    # а у меня совсем не хватает времени на ДЗ.
    print(arr_str[i][0], " ", arr_str[i][1], " ", arr_str[i][2], file=f)
    i += 1
f.close()
