# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
revenue = float(input("Your company's revenue: "))
costs = float(input("Your firm's costs: "))

if revenue > costs:
    profitability = round(revenue / costs, 2)
    print('Your company makes a profit!')
    print(f'The return on revenue is: {profitability}')
elif revenue < costs:
    print('Your company operates at a loss...')
else:
    print('Your company is not profitable')

staff = int(input('How many employees do you have?: '))
print(f'Profit per employee = {round(revenue / staff, 2)}')
