def math(a):
    if a % 2 == 0: 
        return [a, a * a]
    
    
list_1 = [1, 2, 3, 5, 8, 15, 23, 38]
list_2 = []
for i in range(len(list_1)):
    for item in list_1: 
        list_2[i] = math(item)
print(list_2)