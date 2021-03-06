# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
#
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(a, b):
    return 1 / a ** abs(b)


def my_func_(a, b):
    x = a
    for i in range(abs(b) - 1):
        a *= x
    return 1 / a


print(my_func(2, -3))
print(my_func_(float(input('Enter a valid integer: ')), int(input('Enter a negative integer: '))))
