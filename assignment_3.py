"""ЗАДАНИЕ 3"""

"""Получение ввода и проверка, что получено число."""
while True:
    number = input('Введите некое число.\n')
    if number.isdigit():
        break
    print('Нужно ввести число.')

"""Формирование чисел nn и nnn от полученного числа n."""
second_number = int(number*2)
third_number = int(number*3)

"""Вычисление суммы."""
final_number = int(number) + second_number + third_number

print(f'Сумма {number}+{second_number}+{third_number} равна {final_number}')
