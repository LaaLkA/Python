list_1 = [x for x in range(1, 20)]
print(list_1)

list_1 = list(map(lambda x: x + 10, list_1)) # Фун-я map(x, y) принимает на вход 2 параметра: х - фун-я которую мы хотим применить, н - сам объект
print(list_1)