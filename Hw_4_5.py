##

mnog = "mnog.txt"
mnog2 = "mnog2.txt"
first = ""
second = ""
data = open(mnog, "r")
data2 = open(mnog2, "r")
for i in data:
    first = i
for j in data2:
    second = j
data3 = open("mnog3.txt", "a")
data3.writelines(first[:len(first)-2]+"+"+second)
data.close()
data2.close()
data3.close()