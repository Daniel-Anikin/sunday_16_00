# Эта программа считывает два числа и выводит их сумму:
num_1 = int(input())
num_2 = int(input())
print(num_1 + num_2)

# Напишите программу, которая считывает три числа и выводит деление суммы первых дыух на третье
# Каждое число записано в отдельной строке.

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
print((num_1 + num_2) / num_3)

# Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.
# Каждое число записано в отдельной строке.
height = int(input())
base = int(input())
print(height * base / 2)

# Написать пронрамму для нахождения корней квадратного уровнения,
# если даны a, b, c
#Надо подобрать такие a, b, c, чтоб получились натуральные числа без мнимых единиц
a, b, c = int(input()), int(input()), int(input())
D = (b ** 2 - 4 * (a * c)) ** (0.5)
x1 = (-b + D) / (2 * a)
x2 = (-b + D) / (2 * a)
print(x1, x2)

# Вывести n-е чётное число (первым считается 2, вторым 4 и т.д.).
print(2 * int(input()))

# Составьте арифметическое выражение и вычислите n-е нечётное число
# (первое - 1, второе - 3 и т.д.).
print(2 * int(input()) - 1)