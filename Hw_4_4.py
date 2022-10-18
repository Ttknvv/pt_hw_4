##Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import randint
from random import choice
def kof(k):
    if k == 1:
        return f"{randint(1, 10)}"
    else:
        return f"{randint(0, 10)}*x^{k}"

k = int(input("k = "))
znak = ["+", "-"]
data = open("mnog2.txt", "a")
for i in range(k, 0, -1):
    d = kof(i)
    if "0" not in d and i != 1:
        data.writelines(d + str(choice(znak)))
    elif "0" not in d and i == 1:
        data.writelines(d)
data.writelines("=0")
data.close()
