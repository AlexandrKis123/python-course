#2. Пользователь вводит время в секундах. Переведите время в часы, минуты
#и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

seconds = int(input('Введите время в секундах: '))
minutes = seconds // 60
second = seconds % 60
hours = minutes // 60
minutes_answer = minutes % 60
print(f'{hours}:{minutes_answer}:{second}')