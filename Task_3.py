## Task 2               Задайте последовательность чисел. Напишите программу, которая выведет список 
##                       неповторяющихся элементов исходной последовательности.
import random

list = []
list_to_delete = []

for i in range(1, 21):
    list.append(random.randint(1, 30))

def delete_elements(list_a: list, del_list: list):

    for i in list_a:
        if list_a.count(i) > 1:
            list_a.remove(i)
            del_list.append(i)
    
    for i in del_list:
        for j in list_a:
            if i == j:
                list_a.remove(i)
    return list_a


print(list)
print(delete_elements(list, list_to_delete))
#print(list_to_delete)