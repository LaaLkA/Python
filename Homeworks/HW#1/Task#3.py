# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.
n = 485916
b = n
res1 = 0
res2 = 0
while b > 999:
    res1 += b%10
    b = int(b / 10)
c = int(n/1000)
while c > 0:
    res2 += c%10
    c = int(c / 10)
if res1 == res2:
    print("yes")
else:
    print("no")
