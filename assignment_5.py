"""ЗАДАНИЕ 5"""

"""Получение входных данных и проверка, что они числа."""
while True:
    revenue = input('Введите выручку фирмы.\n')
    if not revenue.isdigit():
        print('Выручка должна быть в виде числа.')
        continue
    while True:
        cost = input('Введите издержки фирмы.\n')
        if not cost.isdigit():
            print('Издержки должны быть в виде числа.')
            continue
        cost = int(cost)
        break
    revenue = int(revenue)
    break

"""Вычисление разницы."""
result = revenue - cost

"""Вывод вердикта на основе разницы."""
if result > 0:
    print(f'Фирма получает прибыль в размере {result}.')
    """Вычисление рентабельности."""
    profitablity = (result / revenue) * 100
    print(f'Рентабельность равна {profitablity:.1f}%.')
    """Получение количества сотрудников."""
    while True:
        employees = input('Введите количество сотрудников.\n')
        if not employees.isdigit():
            print('Нужно ввести число.')
            continue
        employees = int(employees)
        if employees == 0:
            print('Число сотрудников не может быть равно нулю.')
            continue
        break
    """Расчет прибыли на сотрудников."""
    profit_to_employee = result / employees
    print(f'Прибыль фирмы на одного сотрудника: {profit_to_employee:.0f}')
else:
    print(f'Фирма терпит убытки в размере {result}.')
