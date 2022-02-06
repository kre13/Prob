# a = int(input("Введите целое число: "))
# b = int(input("Введите еще одно целое число: "))
# c = input("Введите строку: ")
# d = float(input("Введите дробное число: "))
# e = a + b + d
# print(c,"=", e)

# import math
# a = input("Введите катет a: ")
# b = input("Введите катет b: ")
# a = float(a)
# b = float(b)
# c = math.sqrt(a**2+b**2)
# S = (a*b)/2
# P = a+b+c
# print("Гипотенуза равна", c)
# print("Площадь прямоугольного треугольника равна", S)
# print("Периметр прямоугольного треугольника равен", P)

# a = int(input("Введите целое число: "))
# b = float(input("Введите число с плавающей точкой: "))
# c = bool(input("Введите True | False: "))
# d = input("Введите строку: ")
# e = str(a)
# f = str(b)
# print("Введенные значения", a, b, c, d)
# print("Пробразование чисел в строку: ", e, f)

# a = input("Введите ваше имя: ")
# b = input("Ведите ваше отчество: ")
# c = input("Введите вашу фамилию: ")
# d = int(input("Ввведите ваш возраст: "))
# e = input("Введите город вашего проживания: ")
# print(a, b, c)
# print(d)
# print(e)

# a = int(input("Ввести первое число: "))
# b = int(input("Ввести второе число: "))
# c = int(input("Ввести третье число: "))
# slogenie = a+b+c
# vichitanie = a-b-c
# umnogenie = a*b*c
# delenie = a/b/c
# print("Сложение трех чисел равно: ", slogenie)
# print("Разность трех чисел равна: ", vichitanie)
# print("Умножение трех чисел равно: ", umnogenie)
# print("Деление трех чисел равно: ", delenie)

# #Домашнее задание 1
# a = 17/2*3+2
# b = 2+17/2*3
# c = 19%4+15/2*3
# d = (15+6)-10*4
# e = 17/2%2*3**3
# f = a+b+c+d+e
# print(f)
#
# #Домашнее задание 2
# a = 17/2*(3+2)
# print(a)
# b = 2+(17/2)*3
# print(b)
# c = 19%(4+15)/2*3
# print(c)
# d = (15+(6-10))*4
# print(d)
# e = 17/2%(2*3**3)
# print(e)
#
# #Домашнее задание 3
# anna = float(11)
# hleb = float(1.50)
# anna1 = float(11)-hleb*3
# print(anna1)
#
# # #Домашнее задание 4
# # prog = input("Введите имя: ")
# print(prog)
#
# #Домашнее задание 5
# a = 2
# b = 5
# print("У Анны", a, "яблока", "У Пола", b, "яблок")
#
# #Домашнее задание 5
# a = 2
# S = 6*a**2
# V = a**3
# print("Площадь куба поверхностей куба равна:", S)
# print("Объем куба равен:", V)

# import random
# a = random.randint(100, 999)
# print("Сгенерированное случайное трехзначное число: ", a)
# a1 = a//100
# a2 = a//10%10
# a3 = a%10
# a4 = a1+a2+a3
# print("Сумма чисел, случайно сгенерированного трехзначного числа: ", a4)

# import random
# a = random.randint(100, 999)
# print('Случайное число "a" =',a)
# print(a//100 + a//10%10 + a%10)

# a = [1,1,2,3,5,8,13,21,34,55,89]
# for i in a:
#     if i<5:
#         print(i)

# a = [1,1,2,3,5,8,13,21,34,55,89]
# b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# for i in a:
#     for j in b:
#         if i == j:
#             print(j)

# a = int(input("vvedite chislo: "))
# b = str(a)
# print(b, type(b))

# a = input("vvedite slovo: ")
# b = a[::-1]
# if a == b:
#     print("This is polindrom!")
# else:
#     print("This is ne polindrom!")

# def convert(seconds):
#     days = seconds // (24 * 3600)
#     seconds %= 24 * 3600
#     hours = seconds // 3600
#     seconds %= 3600
#     minutes = seconds // 60
#     seconds %= 60
#     print(f'{days}:{hours}:{minutes}:{seconds}')
#
# convert(1234565)
# a = input("vvedite chisla: ")
# b = a.split(",")
# print(b)

# a = input('Введите числа через запятую: ')
# b = a.split(',')
# c = map(int, b)
# lst = list(c)
# tup = tuple(lst)
# print('Список:', lst)
# print('Кортеж:', tup)

# a = [1,2,3,4,5,6]
# print(a[1], a[-1])

# n = int(input("vvedite chislo n: "))
# m = n + (n*n) + (n*n*n)
# print(m)

# a = int(input("vvedite chislo: "))
# for i in range(a):
#     if i == 237:
#         break
#     elif i % 2 == 0:
#         print(i)

# a = [1,2,3,4,5,6,7,8,9]
# b = [10,11,12,13,14,15]
# for i in a:
#     for j in b:
#         if i != j:
#             print(i+j)

# a_dict = {"one": 1, "two": 2, "three": 3}
# for key in a_dict:
#     print(key)

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i)
#     if i == 5:
#         break
#     i += 1

# lis = ['1', '2', '3', '4', '5']
# x = iter(lis)
# print(x)

# a = list("Привет")
# print(a)

# lis = ['a', 'b', 'c', 'd', 'e']
# x = iter(lis)
# print(next(x))

# def palindromic(sequence):
#     """Возвращает True, если последовательность является палиндромом."""
#     for i, item in enumerate(sequence):
#         if item != sequence[-(i+1)]:
#             return False
#     return True

# one_iterable = [2, 1, 3, 4, 7, 11]
# another_iterable = ['P', 'y', 't', 'h', 'o', 'n']
# for n, letter in zip(one_iterable, another_iterable):
#     print(letter, n)

# scoops = 5
# while scoops>0:
#     print("Еще шарик!")
#     coops = scoops-1
# print("Жизнь без мороженого скучна!")

sum(map(str.isupper,cities))

sum(map(str.islower,cities))
