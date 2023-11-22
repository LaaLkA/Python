"""
Словари
"""
d = {} # создаём пустой словарь
d = dict() # создаём пустой словарь через функцию dict()

d['q'] = 'qwerty' # создали ключ q со значением qwerty
print(d)

d['w'] = 'werty'
print(d['w'])

dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ← типы ключей могут отличаться
print(dictionary['up']) # ↑ типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
# print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
dictionary[895] = 955123
print(dictionary)
for item in dictionary:
    # print(item)
    print('{}: {}'.format(item, dictionary[item]))
    
for (k,v) in dictionary.items():
    print(k, v)
print(dictionary.items())