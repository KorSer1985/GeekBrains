# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def func_div(a, b):
    c = a / b
    return c

try:
    print(func_div(int(input('Enter a: ')), int(input('Enter b: '))))
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Enter only number")
