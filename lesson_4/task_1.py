from sys import argv

script_name, output, rate, prize = argv
salary = float(output) * float(rate) + float(prize)
print("Зарплата: ", salary)