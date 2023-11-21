"""
На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, 
а некоторые – гербом. Ваша задача - определить минимальное количество монеток, которые нужно перевернуть, 
чтобы все монетки лежали одной и той же стороной вверх.

Входные данные:

На вход программе подается список coins, где coins[i] равно 0, если i-я монетка лежит гербом вверх,
и равно 1, если i-я монетка лежит решкой вверх. Размер списка не превышает 1000 элементов.

Выходные данные:

Программа должна вывести одно целое число - минимальное количество монеток, которые нужно перевернуть.
"""
coins = [0, 1, 0, 0, 0, 1]
count_resh = 0
count_orel = 0
i = 0

while i < coins.__len__():
    if coins[i] == 0:
        count_orel += 1
    else:
        count_resh += 1
    i += 1
if count_orel > count_resh:
    print(count_resh)
else:
    print(count_orel)