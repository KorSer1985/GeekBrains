# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
seconds = int(input('Enter the time in seconds: '))

hours = seconds // 3600
min = (seconds - hours * 3600) // 60
sec = seconds % 60

print(f'{hours}:{min}:{sec}')
