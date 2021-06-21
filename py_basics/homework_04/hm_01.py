# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script, output_per_hour, rate_per_hour, prize = argv

total = round((int(output_per_hour) * float(rate_per_hour) + int(prize)), 2)
print(f'Accrued: {total} у.е.')
