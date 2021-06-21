# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
age = 35
interest = 'Python'
weight = 82.3

print(f'{age}, {interest}, {weight}')

age = int(input('Your age? : '))
interest = input('What is your hobby? : ')
weight = input('How much do you weigh? : ')

print(f'{age}, {interest}, {weight}')
