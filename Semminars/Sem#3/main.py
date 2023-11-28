lst = [1, 1, 2, 0, -1, 3, 4, 4]
# for i in range(10):
#     print(i)
# print(a[-0])
# for i in range(len(lst)):
#     print(lst[i])
# for item in lst:
#     print(item)

# for i in range(2, 8): # [2, 8)
#     print(lst[i])

# for i in range(2, 8, 2): # [2, 8) с шагом 2
#     print(lst[i])

# for i in range(7, -1, -1): # проход с отрицательным шагом
#     print(lst[i])

# lst.insert(0, 100) # добавили число 100 на 0 индекс, при этом сдвинули все остальные эелементы вправо (i + 1)

# lst.pop(0) # удаляет число с указанным индексом

# lst.remove(4) # удаляет определённое значение (один раз) не удаляет все повторения

# lst.append(True) # добавляет любой конспект в конец списка
# print(lst)

'''
Срезы
'''
# print(lst[0:3]) # срез от левого включительно, до правого невключительно [0, 2]
# print(lst[3:3+4:2]) # срез от левого включительно, до правого невключительно [0, 7] с шагом 2
# print(lst[8:0:-1])
# print(lst[::-1])
'''
Кортежи
'''
# kort = (1, 2, 3, 4)
# # В кортеж ничего нельзя добавить или удалить
'''
Множества
'''
# lst = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5]
# st = set(lst)
# # st = set()

# st.add(6)
# print(st)
# Mnoj = {88 : 'privet', 'kluch' : 'TbI'} # Словари
# print(Mnoj.items())
# print(Mnoj['kluch'])

# dt = {}
# dt['Andrew'] = 20
# dt['Vasya'] = 25
# print(dt)

# dt = {}
# for number in lst:
#     dt[number] = dt.get(number, 0) + 1
    
# # for value in dt.values():
# #     print(value)
    
# for key, value in dt.items():
#     print(f"{key} : {value}")