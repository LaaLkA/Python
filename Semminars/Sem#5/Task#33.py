'''
Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
'''
rating = [2, 3, 4, 4, 5, 5, 2]
max_rating = max(rating)
min_rating = min(rating)
for i in rating:
    if rating[i] == max_rating:
        rating[i] = min_rating
print(rating)