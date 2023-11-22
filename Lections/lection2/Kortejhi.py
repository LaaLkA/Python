"""
Кортежи
Кортеж - это неизменяемый список
"""
t = () # создание пустого кортежа
print(type(t)) # class <'tuple'>
t = (1,)
print(type(t))
t = (1)
print(type(t))
t = (1, 2)
t = tuple(t)
print(type(t))
t = (28, 9, 1990)
print(type(t))
t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue))# r:red g:green b:blue

v = (1, 8, 9)
# Вариации присваивания значений переменным
# a = b = c = 1
# a, b = 1, 2
# c = 9
a, b, c = v
print(a, b, c)
