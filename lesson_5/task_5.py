f = open("text_5.txt", 'w', encoding="utf-8")
numbers = [11, 22, 33, 44, 55]

for i in range(len(numbers)):
    print(numbers[i], end="", file=f)
    if i < len(numbers) - 1:
        print(" ", end="", file=f)
f.close()

f = open("text_5.txt", 'r', encoding="utf-8")
numbers_read = []
N_str = 0
summ = 0
numbers_read = f.readline().split(" ")
for i in range(len(numbers_read)):
    summ += float(numbers_read[i])
print(summ)
f.close()
