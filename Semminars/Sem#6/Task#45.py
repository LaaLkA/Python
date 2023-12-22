'''
Задача №45. Решение в группах
Два различных натуральных числа n и m называются
дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и
наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных
чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не
превосходящее 10^5
. Программа должна вывести все
пары дружественных чисел, каждое из которых не
превосходит k. Пары необходимо выводить по одной в
строке, разделяя пробелами. Каждая пара должна быть
выведена только один раз (перестановка чисел новую
пару не дает).
Ввод: 300 
Вывод: 220 284
'''
def get_divisors_sum(number):
        result = [1]
        for divisors in range(2, number // 2 + 1):
                if number % divisors == 0:
                        result.append(divisors)
        return sum(result)


k = int(input('Введите число k '))
friends = set()

# for number in range(k + 1):
#         if get_divisors_sum(get_divisors_sum(number)) == number:
#                 print(f'Числа {get_divisors_sum(number)} и {number} являются дружественными!')
#         else: 
#                 print(f'Числа {get_divisors_sum(number)} и {number} не являются дружественными!')

for number in range(k + 1):
        if get_divisors_sum(get_divisors_sum(number)) == number and get_divisors_sum(number) != number:
                friends.add(tuple(sorted((number, get_divisors_sum(number)))))
print(f'Дружественные числа: ')
for a, b in friends:
        print(a, b)