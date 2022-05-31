"""ЗАДАНИЕ 6"""

"""Получение исходных данных."""
while True:
    start_distance = input('Введите первоначальную дистанцию.\n')
    if not start_distance.isdigit():
        print('Нужно ввести числовое значение.')
        continue
    while True:
        desired_distance = input('Введите желаемую дистанцию.\n')
        if not desired_distance.isdigit():
            print('Необходимо ввести число.')
            continue
        desired_distance = int(desired_distance)
        break
    start_distance = int(start_distance)
    break

"""Вычисление результатов."""
iterator = 1
while start_distance < desired_distance:
    print(f'{iterator}-й день: {start_distance:.2f}')
    start_distance += start_distance / 10
    iterator += 1

print(f'Ответ: на {iterator}-й день спортсмен '
      f'достиг результата {desired_distance} км.')
