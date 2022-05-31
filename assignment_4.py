"""ЗАДАНИЕ 4"""

"""Получение целого числа."""
while True:
    number = input('Введите целое положительное число.\n')
    if not number.isdigit():
        print('Нужно ввести целое число.')
        continue
    number = int(number)
    break

"""Сохранение первоначально числа для последующего вывода."""
original_number = number

"""Перебор каждой цифры в числе и выбор самого большого."""
highest_num = 0
while True:
    next_num = number % 10
    if next_num > highest_num:
        highest_num = next_num
    number = number // 10
    if number == 0:
        break

print(f'Самая большая цифра в числе {original_number} это {highest_num}')
