# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
A = int(input("Введите число: "))
B = int(input("Введите степен: "))


def Pow(i, j):
    if j == 1:
        return i
    if j != 1:
        return Pow(i, j-1)*i


print(Pow(A, B))