import math

def sum_it(x, y):
    return x + y

def substr(x,y):
    return x - y

def mult(x,y):
    return x*y

def div(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        print("Cannot divide by zero")

def sqrt(x):
    return round(math.sqrt(x), 2)

def sqr(x):
    return x*x

def cos(x):
    return math.cos(x)