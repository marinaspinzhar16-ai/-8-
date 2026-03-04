import re
from typing import Callable


def generator_numbers(text: str):
    """
    Генерує всі дійсні числа з тексту.
    Числа відокремлені пробілами.
    """
    pattern = r"\b\d+\.\d+\b"

    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable):
    """
    Обчислює суму всіх чисел,
    використовуючи передану функцію-генератор.
    """
    return sum(func(text))
