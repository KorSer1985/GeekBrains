# 6. Реализовать два небольших скрипта:
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import cycle


def cycle_func(original_list, iteration):
    i = 0
    iter = cycle(original_list)
    while i < iteration:
        print(next(iter))
        i += 1


cycle_func(['Ахтунг', 333, False, 8.12], int(input("Enter iteration: ")))
