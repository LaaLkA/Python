# Создание пустого списка
list_1 = []
list_1 = list() # с помощью функции
# Задание массива с элементами
list_1 = [1, 2, 3, 4, 5]
# Вывод массива
print(list_1)
# Вывод массива без скобок
print(*list_1)

# перебирание элементов
for i in list_1:
    print(list[i])

# Использование длины массива
print(len(list_1)) # фун-я len() берёт длину как строки, так и массива

list_2 = [1, 5]
print(list_2)
list_2.append(8) # фун-я append() добавляет в конец масиива/строки эленмент, указанный в скобках
print(list_2)