'''
Задача №39. Решение в группах
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
Ввод: 
7 
3 1 3 4 2 4 12
6
4 15 43 1 15 1 
(каждое число вводится с новой строки)
Вывод:
3 3 2 12
'''
import random as rnd

def array(arr):
    for i in range(len(arr)):
        arr[i] = rnd.randint(1,10)


a = int(input('Enter a '))
b = int(input('Enter b '))
list_1 = [0]*a
list_2 = [0]*b
# res = list()

# for i in range(a):
#     list_1[i] = rnd.randint(1, 10)
# for i in range(b):
#     list_2[i] = rnd.randint(1, 10)

array(list_1)
array(list_2)
print(list_1,list_2)
for item in list_1:
    if item not in list_2:
        print(item, end=' ')

# for item in list_1:
#     if item not in list_2:
#         res.append(item)
# print(res)

