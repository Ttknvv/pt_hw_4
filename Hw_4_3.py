##Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint
num = int(input("Введите число = "))
list = [randint(0, 10) for i in range(0, num)]
list1 = []
list2 = []
for i in list:
    if i not in list1:
        list1.append(i)
ind = 0
for i in range(0, len(list1)):
    for j in range(0, num):
        if list1[i] == list[j]:
            ind = ind + 1
    if ind == 1:
        list2.append(list1[i])
    ind = 0

print(list2)