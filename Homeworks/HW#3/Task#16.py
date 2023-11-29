'''
Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.
Пример:
list_1 = [1, 2, 3, 4, 5]
k = 6
# 5
'''
# import math

list_1 = [1, 2, 3, 4, 5]
k = 4
# min = 0
# i_min = 0
# for i in range(len(list_1)):
#     if k == list_1[i]:
#         print(list_1(i))
#     l = abs(k - list_1(i))
#     m = abs(k - list_1(i + 1))
#     if l < m:
#         i_min = i
#     else:
#         i_min = i + 1
# print(list_1(i_min))

min_dif = 999
closest_value = None

for element in list_1: 
    dif = abs(element - k)
    if dif < min_dif:
        min_dif = dif
        closest_value = element
if closest_value == k: 
    print(k)
else:
    print(closest_value)