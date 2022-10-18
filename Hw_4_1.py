##Вычислить число c заданной точностью d

num = float(input("Enter the number = "))
d = len(input("Enter the accuracy (0.0001) = ")) - 2

print(f"{num:.{d}f}")