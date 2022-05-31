"""ЗАДАНИЕ 1"""

"""Создание нескольких переменных."""
name = 'Cat'
fav_num = 42
cool_number = 1.23

"""Вывод созданных переменных."""
print(f'String: {name}\n'
      f'Int: {fav_num}\n'
      f'Float: {cool_number}\n')

"""Запрос числа от пользователя и вывод этого числа в консоль."""
while True:
    user_num = input('Введите красивое число.\n')
    if not user_num.isdigit():
        print('Нужно ввести число, а не что угодно.')
        continue
    print(f'Ваше красивое число: {int(user_num)}')
    break

"""Запрос строки от пользователя и вывод этой строки в консоль."""
user_str = input('Теперь введите что угодно.\n')
print(f'Ваше что угодно: {user_str}')
