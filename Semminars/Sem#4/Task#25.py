'''
Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
'''
#chars = input('Введи символы: ')
chars = 'a a a b c a a d c d d'
chars = chars.split()

dt = {} 

for item in chars:
    if item in dt: 
        dt[item] += 1
        print(f'{item}_{dt[item]}', end=' ')
    else: 
        dt[item] = 0
        print(item, end=' ')
        
    # if item not in dt: 
    #     dt[item] = 1
    #     print(item, end = ' ')
    # else: 
    #     dt[item] += 1
    #     print(f'{item}_{dt[item]-1}', end=' ')
