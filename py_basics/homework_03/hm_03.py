# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    count = [a, b, c]
    count.remove(min(count))
    return sum(count)

print(f'Sum of the largest arguments = '
      f'{my_func(int(input("enter the first argument: ")), int(input("enter the second argument: ")), int(input("enter the third argument: ")))}')
