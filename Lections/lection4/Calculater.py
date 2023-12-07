# def calk1(a):
#     return a+a

# def calk2(a):
#     return a*a

# def math(op, x):
#     print(op(x))

# math(calk1, 5)
# math(calk2, 5)


def calk2(a,b):
    return a * b

def math(op, x, y):
    print(op(x, y))

# def calk1(a,b):
#     return a + b
    
# calk1 = lambda a,b: a + b
    

# math(calk1, 5, 45)
math(calk2, 5, 45)
math(lambda a, b: a + b, 5, 45)