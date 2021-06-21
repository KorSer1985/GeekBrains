# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_func(name, surname, year, city, email, telephone):
    return ', '.join([name, surname, year, city, email, telephone])


print(my_func(surname='Корепанов', name='Сергей', year='1985', city='Мирный', email='Sakha@Welcome_to.hell',
              telephone='01101000011001010110110001101100'))
