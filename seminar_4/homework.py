"""Написать скрипт для расчета корреляции Пирсона между
двумя случайными величинами (двумя массивами). Можете
использовать любую парадигму, но рекомендую использовать
функциональную, т.к. в этом примере она значительно
упростит вам жизнь.

"""
from statistics import mean


def correlation(number_list_x: list, number_list_y: list) -> float:
    """Pearson correlation coefficient."""
    mean_lst1 = mean(number_list_x)
    mean_lst2 = mean(number_list_y)
    return sum(
        map(lambda x, y: (x - mean_lst1) * (y - mean_lst2),
            number_list_x, number_list_y)) / (
        sum(
            map(lambda x: (x - mean_lst1) ** 2, number_list_x)) * sum(
            map(lambda y: (y - mean_lst2) ** 2, number_list_y))) ** 0.5


list_x = [1, 2, 3, 4, 5]
list_y = [2, 3, 6, 8, 10]
print(correlation(list_x, list_y))
