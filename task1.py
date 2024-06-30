from datetime import datetime

"""
    Рахує кількість днів до поточної дати (якщо вказана дата пізніша за поточну -
    результат від'ємний).

    Параметри:
    date (str): Рядок з датою у форматі YYYY-MM-DD.

    Повертає:
    int: Кількість днів до поточної дати.
    """


def get_days_from_today(date: str) -> int:
    # Конвертація рядка в заданому форматі в об'єкт datetime
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d')

    # Обробка можливих винятків
    except (ValueError, TypeError) as exc:
        print('Error:', exc)

    # Обчислення різниці між датами та повернення атрибута days
    else:
        day_diff = datetime.now() - input_date
        return day_diff.days


print('Кількість днів до поточної дати:', get_days_from_today("2021-10-09"))
