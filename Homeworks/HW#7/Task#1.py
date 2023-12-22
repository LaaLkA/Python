'''
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, 
насколько легко он их придумывает, Вам стоит написать программу.

Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
Фразы отделяются друг от друга пробелами.

Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки. В ответе напишите Парам пам-пам, 
если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
Если фраза только одна, то ритм определить не получится и необходимо вывести: Количество фраз должно быть больше одной!.

Пример
На входе:
stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
На выходе:
Парам пам-пам
'''


# def sum(stroke):
#     count = 0
#     vowels = 'уеоаыяию'
#     for item in stroke:
#         if item in vowels:
#             count += 1
#     return count

# def check(stroke):
#     lst = map(lambda count: count == count , stroke.split())
stroka = 'со-лнце-гре-ет ве-сной'
phrases = stroka.split()
count_vowels = []
vowels = 'уеоаыяию'
for item in phrases:
    count = 0
    for word in item:
        if word in vowels:
            count += 1
    count_vowels.append(count)

if len(count_vowels) == 1:
    res = 'Количество фраз должно быть больше одной!'
elif len(set(count_vowels)) == 1:
    res = 'Парам пам-пам'
else: 
    res = 'Пам парам'

print(res)