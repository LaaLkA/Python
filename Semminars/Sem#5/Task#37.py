'''
Задача №37. Решение в группах
Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
'''


def reverse(n):
    string = input()
    if n == 1:
        return string
    return reverse(n - 1) + ' ' + string
    # Второй вариант решения
    # if n == 0:
    #     return ''
    # string = input()
    # return reverse(n - 1) + ' ' + string
    

num = int(input())
print(reverse(num))