# r = range(5) # Выводит значения от 0 до 5 (не включительно) - 0 1 2 3 4
# r = range(2,5) # Выводит значения от 2 до 5 (не включительно) - 2 3 4 range(первое число - начало, втророе число - конец(не включительно))
# r = range(1, 10, 2) # Выводит значения от 1 до 10 (не включительно) с шагом 2 - 1, 3, 5, 7, 9 range( 1е число - начало, 2е число - конец(не включительно), 3е число - шаг)
# r = range(100, 0, -20) # 100 80 60 40 20

# r = range(100, 0, -20)
# for i in r: 
#     print(i) # 100 80 60 40 20 Выводится построчно

# a = 'qwerty'
# print(a[2])

# a = 'qwerty'
# for i in a:
#     print(i)

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# print(len(text)) # Len() помагает узнать длину строки
# print('ещё' in text) # Выводит есть ли у нас "ещё" в text
# print(text.lower()) # lower - всё в нижнем регистре
# print(text.upper()) # upper - всё в верхнем регистре
# print(text.replace('ещё', 'ЕЩЁ')) # perlace(1е значение - что заменяем, 2е значение - на что заменяем)
 
text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-1])

# # print(text[-5]) # б
# print(text[:]) # съешь ещё этих мягких французских булок / вывод всего 
# print(text[:2]) # съ вывод от 0 до 1 элемента
# print(text[20:]) # с 20 до конца
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё от 2 элемента до 9 не включительно
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл от 0 до конца нашей строки с шагом 6
# print(text[::6]) # сеикакл точно также как и строка выше
text = text[2:9] + text[-5] + text[:2] # ешь ещёбсъ
print(text)