##Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input("Введите число = "))

list = []
divisor = 2
while(divisor <= N):
    if (N % divisor) == 0:
        list.append(divisor)
        N = N/divisor
    else:
        divisor += 1

print(list)