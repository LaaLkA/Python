'''
Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes 
'''


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# if is_prime(int(input('Введите число для проверки: '))): 
#     print('Yes')
# else: 
#     print('No')


# В одну строку
print('Yes' if is_prime(int(input('Введите число для проверки: '))) else 'No')