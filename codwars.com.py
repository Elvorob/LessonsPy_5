# def move(position, roll):
#     # your code here
#     return position + roll * 2
import functools


# def past(h, m, s):
#     # Good Luck!
#     return h * 60 * 60 * 1000 + m * 60 * 1000 + s * 1000

# import math
# def century(year):
#     # return (year + 99) // 100
#     return 1 + (year - 1) // 100
#
# year = int(input('year: '))
# # print(century(year))
# def check_for_factor(base, factor):
#    # if base % factor == 0:
#    #     return 'true'
#    # else:
#    #     return 'false'
#    return base % factor == 0
# print(check_for_factor(7,2))

# Find the first non-consecutive number
# Your task is to find the first element of an array that is not consecutive.
# By not consecutive we mean not exactly 1 larger than the previous element of the array.
# E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive but 6 is not, so that's the first non-consecutive number.
# If the whole array is consecutive then return null2.
# mine
# l = [1, 2, 3, 4, 5, 6]
# prev = l[0] # присваиваем новой перменной значение с нулевым индексом
# first = None # присваиваем переменной значение None, оно будет выводиться когда все значания в листе увеличиваются на 1 и нет нарушения последовательности
# for num in l[1:]: #если нужно начать считать не с нулевого элимента, то пишем так
#    if (prev + 1) != num:
#       first = num
#       break
#    prev += 1
# #return first
# print(first)
# def first_non_consecutive(arr):
# 1
#    for i, x in enumerate(arr[:-1]):
#       if x + 1 != arr[i + 1]:
#          return arr[i + 1]
# 2
#    for i in range(1, len(arr)):
#       if arr[i] - arr[i - 1] > 1:
#          return arr[i]
# print(first_non_consecutive([1, 2, 10, 4, 5, 6]))

# Is the string uppercase?
# Сreate a method to see whether the string is ALL CAPS.
# Examples (input -> output)
# "c" -> False
# "C" -> True
# "hello I AM DONALD" -> False
# "HELLO I AM DONALD" -> True
# "ACSKLDFJSgSKLDFJSKLDFJ" -> False
# "ACSKLDFJSGSKLDFJSKLDFJ" -> True
# In this Kata, a string is said to be in ALL CAPS whenever it does not contain any lowercase letter
# so any string containing no letters at all is trivially considered to be in ALL CAPS.
# def is_uppercase(inp):
#     return inp == inp.upper()
# print(is_uppercase('"+>g_#HQxmiX{c3`U!.2<\)Nz1*:Oh?}~$b/7'))

# def test_input(name):
#     name = input()
#     return name
# print(test_input('Лена'))
# b = -456;
# c = str(b);
# x = list(c);
# print(x)
# def sum_digits(number):
#     if number < 0:
#         number *= -1
#     list1 = list(str(number))
#     return int(functools.reduce(lambda x,y: int(x)+int(y), list1))
# print(sum_digits(0))

# def sum_digits(number):
#     a = str(abs(number))
#     print(type(a))
#     sum = 0
#     for x in a:
#         print(x)
#         print(type(x))
#         sum += int(x)
#     return sum
#
# print(sum_digits(13))


# def solution(string):
#     return string[::-1]
#
# print(solution('Elena Vorobyeva'))
#
# def is_triangle(a, b, c):
#     if a < (b + c) and b < (a + c) and c < (a + b):
#         return True
#     return False
# print(is_triangle(7,2,2))

# def is_lucky(n):
#     sum1 = 0
#     n = str(n)
#     for num in n:
#         sum1 += int(num)
#     if sum1 % 9 == 0:
#         return True
#     return False
# print(is_lucky(0))

# def calculator(a,b,sign):
#     if type(a) == int and type(b) == int:
#         if sign == '+': return a+b
#         elif sign == "-": return a-b
#         elif sign == "*": return a*b
#         elif sign == "/": return a/b
#         else: return 'unknown value'
#     return 'unknown value'
# print(calculator(1,2,'+'))
#
# a = 5
# print(type(a))

# def owned_cat_and_dog(cat_years, dog_years):
#     ownedCat = 0
#     while cat_years >= 15 and ownedCat == 0:
#         cat_years -= 15
#         ownedCat += 1
#     while cat_years >= 9 and ownedCat == 1:
#         cat_years -= 9
#         ownedCat += 1
#     ownedCat += (ownedCat == 2)*cat_years // 4
#     ownedDog = 0
#     while dog_years >=15 and ownedDog ==0:
#         dog_years -= 15
#         ownedDog += 1
#     while dog_years >= 9 and ownedDog == 1:
#         dog_years -= 9
#         ownedDog +=1
#     ownedDog += (ownedDog == 2)*dog_years // 5
#     return [ownedCat, ownedDog]
#
# def owned_cat_and_dog(cat_years, dog_years):
#     cat = 0;
#     dog = 0;
#     # cat's year
#     if cat_years >= 15 and cat_years < 24:
#         cat += 1
#     elif cat_years >= 24 and cat_years < 28:
#         cat += 2
#     elif cat_years >= 28:
#         cat = 3 + (cat_years - 28)//4
#     # dog's year
#     if dog_years >= 15 and dog_years < 24:
#         dog += 1
#     elif dog_years >= 24 and dog_years < 29:
#         dog += 2
#     elif dog_years >= 29:
#         dog = 3 + (dog_years - 29)//5
#     return [cat, dog]
# print(owned_cat_and_dog(56,64))

# def function(start_num, end_num):
#     return list(range(start_num, end_num, 1))
# print(function(2,9))

# def check(seq, elem):
#     for x in seq:
#         if x == elem:
#             return True
#     return False
# print(check([80, 117, 115, 104, 45, 85, 112, 115], 45))

# def filter_lucky(lst):
#     res = []
#     res1 =[]
#     for x in lst:
#         x1=list(str(x))
#         for i in x1:
#             if i == '7':
#                 res.append(x)
#     for n in res:
#         if n not in res1:
#             res1.append(n)
#     return res1
# print(filter_lucky([157358, 83527, 192743, 136667, 26075, 175511, 137853, 39407, 92537, 173481, 193007, 171132, 137428, 5879, 131547, 148672, 101755, 117623, 76416, 156307, 170685, 80074, 88798, 30170, 85878, 157870, 134706, 72705, 76857, 197305, 76205, 187630, 10758, 17889, 27832, 77858, 7220, 151274, 176742, 87663, 168277, 173854, 183674, 55617, 86793, 47102, 164817, 170994, 170633, 189746, 131397, 57963, 197401, 76769, 49375, 163731, 74978, 68079, 183337, 33278, 87474, 128783, 69746, 23795, 9727, 88276, 66732, 157594, 173651, 73172, 80907, 96705, 191795, 47766, 177975, 72287, 111337, 4771, 123617, 176557, 98837, 5074, 14768, 57594, 114176, 189447, 70401, 150715, 130970, 170550, 19427, 100873, 87066, 64722, 71759, 88972, 147978, 157860, 179722, 35715, 100479, 8733, 40372, 152275, 109271, 157395, 134175, 163797, 70609, 38473, 150075, 84971, 70992, 126708, 187180, 75022, 17940, 153987, 69702, 149758, 107940, 178500, 182037, 92743, 184702, 82735, 176692, 124727, 44757, 35746, 97260, 143729, 159731, 6720, 187591, 114178, 40776, 100474, 177871, 41637, 177262, 108971, 138187, 71011, 74704, 172022, 102587, 181217, 73711, 171059, 175738, 187409, 177549, 63367, 167941, 102778, 47432, 36702, 88768, 74298, 69927, 173850, 120782]))

# def high_and_low(numbers):
#     l = numbers.split(' ')
#     return max(l, key=int) + ' ' + min(l, key=int)
#
# print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))

f= 'Pig,latin,!@#435345,is cool'
# for x in f:
#     print(x)
# f1 = f.split( )
# # print(f1)
# def validate_hello(greetings):
#     for x in ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']:
#         if str(x) in greetings.lower():
#             return True
#     return False
#     # return ('hello' or 'ciao' or 'salut' or 'hallo' or 'hola' or 'ahoj' or 'czesc') in greetings.lower()
# print(validate_hello('wie geht\'s dir?'))

def sort_dict(d):
    d = list(d.items())
    d = sorted(d, reverse=True)
    return d

print(sort_dict({3:1, 2:2, 1:3}))
# t = {3:1, 2:2, 1:3}
# print(t.values())