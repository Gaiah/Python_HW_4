## Task 3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
path = "polynomial_file.txt"

k = int(input("Input a number for polynomial degree: "))

coefficient_1 = random.randint(0, 100)
coefficient_2 = random.randint(0, 100)
coefficient_3 = random.randint(0, 100)

polynomial = (f"{coefficient_1}x^{k} + {coefficient_2}x + {coefficient_3} = 0")
#print(polynomial)

data = open(path, 'w')
data.write(polynomial)
data.close
