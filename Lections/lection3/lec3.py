# Фун-я ничего не возвращает
def sum_numbers(n):
    summa = 0
    for i in range(1,n+1):
        summa += i
    print(summa)


sum_numbers(5)


# Фун-я возвращает сумму


def sum_numbers(n):
    summa = 0
    for i in range(1,n+1):
        summa += i
    return summa


print(sum_numbers(5))


# Фун-я с неограниченным количеством передаваемый аргументов


def sum_str(*args): # Нужно поставить * 
    res = ''
    for i in args:
        res += i
    return res


print(sum_str('q', 'e', 'l'))
print(sum_str('q', 'e', 'l', 'r', 'f'))
print(sum_str('1', '8', '9'))