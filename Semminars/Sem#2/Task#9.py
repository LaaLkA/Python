"""
Задача №9. Решение в группах
По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while
Input: 5
Output: 120
"""
# number = int(input("Введите число "))
# i = 1
# Fact = 1
# while i <= number:
#     Fact *= i
#     i += 1
# print(Fact)

# number = input("Введите число ")
# i, fact = 1
# while i <= number:
#     fact *= i
#     i += 1
# print(fact)

"""
Решение с преподавателем
"""
n = int(input("Введите значение n "))
print(n)
i = 1
factorial = 1
while i <= n: 
    factorial *= i
    i += 1
print(factorial)