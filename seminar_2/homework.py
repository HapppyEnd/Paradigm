"""Условие:
На вход подается число n.
● Задача:
Написать скрипт в любой парадигме, который выводит на экран таблицу
умножения всех чисел от 1 до n. """

n: int = int(input('Enter number: '))
for number in range(1, n+1):
    print(*range(number, number*n+1, number), sep='\t')
