## 5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

path = "polyn_1.txt"
data = open(path, 'r')
a = data.readline().split()
data.close

print(a)

path = "polyn_2.txt"
data = open(path, 'r')
b = data.readline().split()
data.close

print(b)

sum = 0

for i in a:
    for j in b:
        if i.isdigit and j.isdigit:
            sum = int(i) + int(j)
        print(sum, end = " ")