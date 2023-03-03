# # 24. Черника растет на круглой грядке, кусты высажены только по окружности. У каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов. На кустах выросло различное число ягод – на i-ом кусте выросло ai ягод. Собирающий
# модуль собирает ягоды с этого куста и с двух соседних с ним. Напишите программу для нахождения максимального числа
# ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом.
from random import randint
num = int(input('Input a number: '))
bush = []
sum_list = []

for i in range(1, num + 1):
    bush.append(list())
    for j in range(i):
        bush[j].append(randint(1, 20))
print(bush)

for i in bush:
    # print(sum(i), end=' * ')
    sum_list.append(sum(bush[bush.index(i) - 2]) + sum(bush[bush.index(i) - 1]) + sum(i))

print(f'The maximum number of berries: {max(sum_list)}')