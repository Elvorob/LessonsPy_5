##### Листы list
# #
# l = []
# print(l)
# #
# l=[1, 'str', 2.5, True, None]
# print(l)
# #
# s = 'I like eggs for breacfast'
# # my_list = list(s)
# # print(my_list)
# my_list1 = s.split(' ')
# # print(my_list1)
# # print(my_list1[-1])
# # print(my_list1[0])
# print(id(my_list1))
# #
# l1 = [8, 6, 5, 1, 0]
# print(l1)
# # print(id(0))
# # l1[0] = 4
# # print(l1)
# # print(id(0))
# l2 = [10,20]
# # l1.append(l2)
# # print(l1)
# # print(l1[-1])
# # print(l1[-1][0])
# str = 'extra'
# l1.append(str)
# l2.extend(str)
# # l1.extend(l2)
# print(l1)
# print(l2)
# #
# nums=[2, 3, 1, 5, 6, 4, 0]
# print(f'initial list: {nums}')
# print(id(nums))
# # SORTED() .SORT()
# #
# str1= 'absvdf'
# print (sorted(str1))
# print (sorted(str1,reverse=True))
# #
# print('SORTED()')
# nums1=sorted(nums)
# print(f'New sorted list% {nums1}')
# print(f'initial list: {nums}')
# print(f' ID: {id(nums1)}')
# #
# print('.SORT()')
# nums1=nums.sort()
# print(f'New sorted list: {nums1}') # none
# print(f'initial list: {nums}')
# print(f' ID: {id(nums)}')
# #
# print('.REVERSE()')
# print(nums.reverse())
# print(nums)
# print(f' ID: {id(nums)}')
# #
# # slising
letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(letters[0:-1:2])
print(letters[-3])
print(letters[::-1])
print(letters[1:-1])
print(letters[2:])
#
# # list comprehension
# l = [1, 2, 3, 4, 5]
# new_l = []
# for x in l:
#     if x%2:
#         new_l.append(x*x)
# print(new_l)
# #
# new_l = [x*x for x in l if x%2] # возводим в степень нечетные
# # new_l = [x*x for x in l if x%2==0] # возводим в степень четные числа
# print(new_l)
from itertools import count

###### Кортежи или TUPLES
# #
# mytuple = 1,2,3
# print(mytuple)
# #
# my_tuples = (1, True, 'name', None, 'name', 'name', 25)
# print(my_tuples)
# #
# name = 'Mark',
# print(name)
# #
# name = ('Mark',)
# print(name)
# print(type(name))
# name = ('Mark')
# print(name)
# print(type(name))
# #
# letters = ('apple', 'banana', 'cat')
# a, b, c = letters
# print(a)
# print(b)
# print(c)
# print(type(c))
# #
# letters[0] = 'ananas' # не сработает так как кортэж неизменяемая структура данных.
# print(letters)
# letters = list(letters) # можно перевести в лист если нужно поменять
# letters[0] = 'ananas'
# print(tuple(letters))
# print(letters)
# #
# # как получить индекс элимента с конкретным значением и как посчитать
# my_tuples = (1, True, 'name', None, 'name', 'name', 25)
# print(my_tuples.index('name'))
# print(my_tuples.count('name'))
# #
# # Фильтрация
# my_tuples = (1, True, 'name', None, 'name', 'name', 25)
# result = tuple(filter(lambda x: isinstance(x, int), my_tuples))
# print(result)
# #
# #Tuple Methods
# my_tuples = (1, True, 'name', None, 'name', 'name', 25)
# print(f'Sum: {sum(result)}')
# print(f'Max: {max(result)}')
# print(f'Min: {min(result)}')
# print(f'Lenght of my_tuple: {len(my_tuples)}')
# print(f'Lenght of result: {len(result)}')
# #
# Iterate tuple with loops, работает для листов и остальных похожих структур
# my_tuples = (1, True, 'name', None, 'name', 'name', 25)
# for (index, item) in enumerate(my_tuples):
#     print(index, item)
# #
# i = 0
# while i < len(my_tuples):
#     print(my_tuples[i])
#     i += 1
# #
# # nested list in tuple
# letters = ('apple', ["banana", 'mango'], 'melon')
# letters[1][0] = 'cherry'
# print(letters)
# #
# # swaping variables
# a = 5
# b = 10
# a, b = b, a
# print(f'a= {a}')
# print(f'b= {b}')
# #
# # Passing tuples as an argument in a fanktion
# def sum_it(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
# print(sum_it(4, 5, 10, 6, 20))

# def func(*args):
#     l = []
#     for item in args:
#         l.append(item*item)
#     return l
# print(func(2,5,6,8,10))
# #
# # DICTIONARIS
# my_dict ={
#     'Name':'Anna',
#     'Lastname' : 'Pavlova',
#     'Age':20,
#     'Department':'IT'
# }
# print(my_dict)
# print(id(my_dict))
# print(my_dict['Name'])
# my_dict['Lastname'] = 'Smitnova'
# print(my_dict)
# print(id(my_dict))
# print(len(my_dict))
# my_dict['Salary'] = 5000
# print(my_dict)
# print(id(my_dict))
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# print(my_dict.pop('Salary'))
# print(my_dict)
# print(my_dict.get('Salary', 'Not found'))
# #
# # SETS
# print(set([1,3,5,7,4,3,8]))
# set1 = {1, 2, 3, 'one', 'ten'}
# set2 = {1, 2, 3, 'one', 'ten', 100,525}
# set3 = {1,2,3}
# print(set1.issubset(set2))
# print(set2.issuperset(set1))
# print(set2.intersection(set1, set3))
# print(set2.difference(set1,set3))
# print(set1)
# print(set1.remove(1))
# print(set1)
# print(set1.add(8))
# print(set1)
# #
# fs = frozenset({1,2,3})
# print(fs)
# fs.remove(1) # нельзя remove или add
# print(fs)

#### Home Work
# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(my_list[-2])
#
# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
print(type(list_1[2]))
# 1
# sum_l = 0
# for x in list_1:
#     if type(x) == int:
#         sum_l = sum_l + x
# print(sum_l)
# 2
# первый вариант решения
matches = []
for match in list_1:
    if type(match) == str:
        if "a" in match:
            matches.append(match)
print(matches)
# второй вариант решения
matches = [match for match in list_1 if type(match) == str and "a" in match]
print(matches)
# решение третий вариант, подсказан в группе пайтон
print(f'Task 3.2.2 answer: {[l1_item for l1_item in list_1 if "a" in str(l1_item)]}')
#
# 3.3. Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж
# list = ['cat', 'dog', 'horse', 'cow']
# tuple1 = tuple(list)
# print(list)
# print(tuple1)
#
# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
# family_1 = input('Family one: ')
# family_2 = input('Family two: ')
# family_1 = tuple(family_1.split(', '))
# family_2 = tuple(family_2.split(', '))
# if len(family_1) > len(family_2):
#     print(family_1)
# elif len(family_1) < len(family_2):
#     print(family_2)
# else:
#     print('Equal')
#
# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение
# film = {
#     'title':'Favorit film',
#     'director':'Director Film',
#     'year':'1999',
#     'budget':'1000000',
#     'main_actor':'Actor Main',
#     'slogan':'slogan slogan'
# }
# print(film)
# print(film.keys())
# print(film.values())
#
# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# print(sum(my_dictionary.values()))
#
# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
# list = list(set([1, 2, 3, 4, 5, 3, 2, 1]))
# print(list)
#
# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга
#  set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
#  set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# # 1
# print(set1.intersection(set2))
# # 2
# set3 = set1.difference(set2)
# set4 = set2.difference(set1)
# sets = set4.union(set3)
# print(sets)
# # 3
