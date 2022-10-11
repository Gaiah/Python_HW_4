## 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

list = []
user_num = abs(int(input("Input a number: ")))

for i in range(2, user_num + 1):
    while user_num % i == 0:
        list.append(i)
        user_num //= i
    if user_num > 1 and user_num % i != 0:
        list.append(user_num)
        user_num //= user_num
print(list)