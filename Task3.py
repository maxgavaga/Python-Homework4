# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

from cgi import print_arguments


b = [1, 1, 2, 3, 3, 4, 5]
a = []
for i in b:
    if b.count(i) == 1:
        a.append(i)
print(a)