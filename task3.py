import re

"""
    Нормалізує формат телефонного номера (з кодом України).

    Параметри:
    phone_number (str): Рядок з телефонним номером для нормалізації.

    Returns:
    str: Нормалізований номер телефона.
    """


def normalize_phone(phone_number):
    # Видалення всіх символів, які не є цифрами та знаками плюсу
    modified_phone = re.sub(r"[^+0-9]", "", phone_number)

    # Перевірки для нормалізації міжнародного коду
    if modified_phone.startswith('+'):
        return modified_phone

    elif modified_phone.startswith('380'):
        return '+' + modified_phone

    else:
        return '+38' + modified_phone


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
