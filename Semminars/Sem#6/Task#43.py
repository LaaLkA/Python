'''
Задача №43. Решение в группах
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод: 1 2 3 2 3 
Вывод: 2
'''
# def array(lst, b):
#     print('Введите массив')
#     i = 0
#     while i < b: 
#         lst.append(int(input()))
#         i += 1
#     return lst 

# def search(arr):
#     count = 0
#     for i in range(len(arr) - 1):
#         for j in range(i + 1, len(arr)):
#             if arr[i] == arr[j]:
#                 count += 1
#     return count
    
    
# b = int(input('Введите длину массива '))    
# lst = []
# print(f'Количество пар в массиве = {search(array(lst, b))}')

from collections import Counter
list_n = [1, 2, 3, 2, 3, 3, 3]
count = 0

cnt = dict(Counter(list_n))
print(cnt)

for n in cnt.values(): 
    count += (n * (n - 1)) // 2
print(count)