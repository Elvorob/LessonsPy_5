# задание 2.1
# import random
# charhealth = random.randint(-100, 100)
# print ('Your character health is',charhealth)
# if charhealth > 0:
#     print("you're still alive, keep it up!")
# else:
#     print("Unfortunately you died, my condolences!")

# Задание 2.2
# num = int(input('введите число для проверки: '))
# if num % 2 == 0:
#     print('Ваше число четное')
# else:
#     print('Ваше число нечетное')

# Задание 2.3
# y = int(input('Введите год: '))
# # Считаем какой год високосный или нет.
# if y % 4 == 0:
#     if y % 100 == 0:
#         if y % 400 == 0:
#             x = 1
#         else:
#             x = 0
#     else:
#         x = 1
# else:
#     x = 0
# # Печатаем результат
# if x == 1:
#     print('високосный')
# else:
#     print('не високосный')

# Задание 2.4
text = input('Введите текст для печати: ')
rep = int(input('Введите колличество повторений: '))
i = 1
while i <= rep:
    print(text)
    i += 1
