# def move(position, roll):
#     # your code here
#     return position + roll * 2

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
def is_uppercase(inp):
    return inp == inp.upper()
print(is_uppercase('"+>g_#HQxmiX{c3`U!.2<\)Nz1*:Oh?}~$b/7'))