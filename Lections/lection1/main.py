n = 1
print(type(n))
print(n)

n = "Just"
print(type(n))
print(n)

n = "Ju\"st"
print(type(n))
print(n)

n = "Ju'just'st" # разные ковычки
print(type(n))
print(n)

n = 1.23
print(type(n))
print(n)

# для комментирования нужно поставить решётку либо использовать комментирование нескольких строк
# для быстрого комментирования использовать сочетание клавиш ctrl + K + ctrl + U
"""
Это способ 
комментировать 
несоклько строк
"""
a = "Hello"
b = "World"
print(a,b)

c = 4
d = 5,4
print(f"{c} - {d}")

e = 5,89
f = 3
print("{} - {}".format(e, f))

# Ввод данных 
#input() -  функця ввода данных
print("Введите первую строку")
a = input()
print(a)




