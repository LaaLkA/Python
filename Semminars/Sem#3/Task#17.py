# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6


lst = [1, 1, 2, 0, -1, 3, 4, 4]
# lst = input().split()
# # n = 10
# # for i in range(n):
# #     lst.append(int(input()))
# # print(lst)
# print(lst)
st = set(lst)
print(len(st))