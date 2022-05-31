"""ЗАДАНИЕ 2"""

"""Получение ввода и проверка, что получено число."""
while True:
    number = input('Введите время в секундах.\n')
    if not number.isdigit():
        print('Нужно ввести число.')
        continue
    number = int(number)
    break

"""Вычисления на основе полученного числа"""
hours = number // 3600
minutes = (number // 60) % 60
seconds = number % 60

print(f'Время: {hours:0>2}:{minutes:0>2}:{seconds:0>2}')
