"""Написать скрипт для расчета корреляции Пирсона между
двумя случайными величинами (двумя массивами). Можете
использовать любую парадигму, но рекомендую использовать
функциональную, т.к. в этом примере она значительно
упростит вам жизнь.

"""
from statistics import mean


def correlation_coefficient(number_list_x: list, number_list_y: list) -> float:
    """Pearson correlation coefficient."""
    mean_list_x = mean(number_list_x)
    mean_list_y = mean(number_list_y)
    return sum(
        map(lambda x, y: (x - mean_list_x) * (y - mean_list_y),
            number_list_x, number_list_y)) / (
        sum(
            map(lambda x: (x - mean_list_x) ** 2, number_list_x)) * sum(
            map(lambda y: (y - mean_list_y) ** 2, number_list_y))) ** 0.5


list_x = [1, 2, 3, 4, 5]
list_y = [2, 3, 6, 8, 10]
print(correlation_coefficient(list_x, list_y))
