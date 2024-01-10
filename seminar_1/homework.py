"""Задача №1.
Дан список целых чисел numbers. Необходимо написать в императивном стиле
процедуру для сортировки числа в списке в порядке убывания.
Можно использовать любой алгоритм сортировки.
Задача №2.
Написать точно такую же процедуру, но в декларативном стиле."""


def sort_list_imperative(numbers: list) -> list:
    """Imperative paradigm."""
    numbers_length: int = len(numbers)
    for i in range(numbers_length):
        for j in range(numbers_length - i - 1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    return numbers


def sort_list_declarative(numbers: list) -> list:
    """Declarative paradigm."""
    numbers.sort(reverse=True)
    return numbers
