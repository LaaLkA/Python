# Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.
n = 123
res = 0
while n > 0:
    res += n % 10
    n = int(n / 10)
print(res)