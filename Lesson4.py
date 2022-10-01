# FUNCTION
# def person(age, last_name, name):
#     return f'Hello, me name is {name} {last_name}. I am {age} years old'
#
# print(person(18, 'Smith',  'Anna'))
import functools

# def person(age, last_name ='Smith', name='Anna'):
#     return f'Hello, me name is {name} {last_name}. I am {age} years old'
#
# # print(person(18))
# # print(person(name='Alice',18))
# # print(person(18, name='Alice'))
# print(person(name='Alice',age=18))

# BILD_IN FUNCTION
# min_arg = min(5, 6, 8, 10)
# print(min_arg)

# SCOPE (пространство имен)
# x = 15
# y = 78
# def sum_it(x,y):
#     print(f'Locals: {locals()}')
#     return  x+y
# print(f'Inside the function: {sum_it(5,8)}')
# print(f'Globals: {globals()}')

# LAMBDA
# print((lambda x, y: x*y)(5, 8))

# mult = lambda x, y: x*y
# print(mult(5,8))

# Пример использования:
# домашнее задание из урока 3:
# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# print(type(list_1[2]))
# 1
# sum_l = 0
# for x in list_1:
#     if type(x) == int:
#         sum_l = sum_l + x
# print(sum_l)
#
# print(sum(filter(lambda x: type(x) == int, list_1)))

# Найти в list_1 нечетное число разные способы:
#
# print('принт из функции')
# def take_odd(num):
#     if type(num) == int and num%2:
#         return True
#     return False
# print(list(filter(take_odd, list_1)))
#
# print('принт решения с lambda')
# filtred=list(filter(lambda x: type(x) == int, list_1))
# print(list(filter(lambda x: x%2, filtred)))
#
# print('если у нас однородный массив чисел list_3 = [1,2,5,8,10,105,78]')
# list_3 = [1,2,5,8,10,105,78]
# print('решение с вызовом lambda')
# print(list(filter(lambda x: x%2, list_3)))
# print('решение с вызовом функции take_odd')
# print(list(filter(take_odd, list_3)))

#    - распечатайте все строки, где есть буква 'a'
# решение из домашки:
# первый вариант решения
# print('Решение с циклом 1 способ:')
# matches = []
# for match in list_1:
#     if type(match) == str:
#         if "a" in match:
#             matches.append(match)
# print(matches)
# второй вариант решения
#(что делаем: тут может быть как какое-то выражение, так и функция, так и просто значение из list_1 без изменений)
# for (что перебираем) in (где перебираем значения)
# (если нужно условие для того где перебираем значение, то используем:
# if (условие) in (если проверяем внутри самого значения,
# если это убрать то условие будет просто проверять равно ли значение "а",
# а не проверят есть ли "а" внутри слова))
# print('Решение с циклом 2 способ:')
# matches = [x for x in list_1 if type(x) == str and "a" in x]
# print(matches)
# # лямбдой нужно фильтровать два раза
# print('решение с lambda')
# filtred = list(filter(lambda x: type(x) == str, list_1))
# print(list(filter(lambda x: "a" in x, filtred)))

#MODULES
# два способа как вызвать встроенные функции:
# 1
# import functools
# res = functools.reduce(lambda x,y: x+y, [1,5,8,11,13])
# print(res)
# 2
# from functools import reduce
# res = reduce(lambda x,y: x+y, [1,5,8,11,13])
# print(res)

# создали собственный модуль с функциями my_file, теперь вызываем от туда функции
# import my_file
# print(my_file.sum_it(5,6))

# если нужно все методы из модуля импортировать
# from my_file import *
# print(mult(4,6))

# как делать тесты с помощью assert
# def tests():
#     assert sum_it(5, 8) == 13, f'Wrong number, actual result is {sum_it(5,8)}'
#     assert mult(10, 6) == 60, f'Wrong number, actual result is {mult(10,6)}'
#     assert div(10, 0) == 'division by zero'
#
# tests()

# ВСТРОЕННЫЕ MODULES (bild in)
# import math
# import math as m
# arr = [1, 2, 3, 4, 5, 10, 25]
# n_arr = m.prod(arr)
# print(n_arr)
#
# import datetime
# birth_y = 1980
# curr_date = datetime.date.today()
# curr_age = curr_date.year - birth_y
# curr_month = curr_date.month
# print(curr_date)
# print(curr_age)
# print(curr_month)

# def sum_it(**kwargs):
#     # x = 0
#     # for i in kwargs.values():
#     #     x += i
#     # return x
#     print(type(kwargs))
#     return sum(kwargs.values())
#
# print(sum_it(num1=1,num2=4, num3=6))
#
# def sum_i(*a):
#     print(type(a))
#     return sum(a)
# print(sum_i(1,4,8))

# ДОМАШНЯЯ РАБОТА
# 4.1.Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
# (с помощью кортежа): периметр квадрата(4*light_side), площадь квадрата(light_side*light_side)
# и диагональ квадрата(light_side * корень квадратный из 2).
# def square(side_light):
#     import math
#     perim = side_light * 4
#     area = side_light * side_light
#     diagonal = side_light * round(math.sqrt(2), 2)
#     return (perim, area, diagonal)
# print(square(5))

# 4.2.Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их
# построчно в формате аргумент: значение. Например:
# name: John
# last_name: Smith
# age: 35
# position: web developer
# def xt(**a):
#     f=''
#     for key, value in a.items():
#          f += key + ": " + value + '\n'
#     return f
#
# print(xt(name='John', last_name='Smith', age='35', position='web developer'))
#
# def xt(**a):
#     for key, value in a.items():
#         print(key, ":", value)
#
# xt(name='John', last_name='Smith', age=35,position='web developer')

#
# 4.3.Используя лямбда - выражение, из списка my_list = [20, -3, 15, 2, -1, -21]
# создайте новый список, содержащий только положительные числа
# my_list = [20, -3, 15, 2, -1, -21]
l1 = list(filter(lambda x: x>=0, my_list))
print(l1)
# #
# # 4.4.Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
g = functools.reduce(lambda x,y: x*y, l1)
print(g)
# 4.5.Создайте файл my_calc.py ипропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
# Примените эти функции в качестве методов в другом файле.
import my_calc
print(my_calc.div(5,5))
print(my_calc.sqrt(5))
print(my_calc.mult(3,4))
print(my_calc.sum_it(5,5))
print(my_calc.substr(12,6))

def test_calc():
    assert my_calc.div(10,5) == 2, f'Wrong number, actual result is {my_calc.div(10,5)}'

test_calc()