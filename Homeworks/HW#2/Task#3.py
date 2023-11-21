"""
Требуется вывести все целые степени двойки (т.е. числа вида 2k),
не превосходящие числаN.
"""
number = int(input("Введите число "))
number_srav = 0
stepen = 0
while number_srav < number:
    number_srav = 2 ** stepen
    if number_srav <= number:
        print(number_srav)
    stepen += 1