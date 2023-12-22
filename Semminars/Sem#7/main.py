# lst = []
# lst = input().split()
# print(lst)
# # for i in range(len(lst)):
# #         lst[i] = int(lst[i])

# lst = list(map(int, lst))
# print(lst)


def is_even(number):
        return number % 2 == 0

lst = [1, 4, 6, 7, 8, 10, 12]
result = list(filter(is_even, lst))
result2 = list(map(is_even, lst))
print(result)
print(result2)

sum_lambda = lambda arg1, arg2: arg1 + arg2
print(sum_lambda(10, 20))