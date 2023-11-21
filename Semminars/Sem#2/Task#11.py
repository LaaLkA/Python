"""
Задача №11. Решение в группах
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6 
"""
number  = int(input("Введите число A "))
number_A = 0
number_B = 1
count = 2

while number_B < number:
    temp = number_B
    number_B += number_A
    number_A = temp
    count += 1

if number_B == number: 
    print(f'Число А является числом фибаначи. {count}ым по счёту')
else:
    print(-1)