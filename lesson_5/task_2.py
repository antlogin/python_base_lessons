f = open("text_6.txt", 'r')
N_str = 0
N_words = 0
while True:
    content = f.readline()
    if content:
        N_str += 1
        print(N_str, ": ", len(content.split(" ")), " - кол-во слов в этой строке")
        N_words = N_words + len(content.split(" "))
    else:
        break
print("Всего", N_str, "строк. Во всех строках", N_words, "слов.")
f.close()
