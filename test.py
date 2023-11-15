from lib import count_same_elements

# Тестовые данные
lists = [
    [1, 2, 3, 4, 5],
    [3, 4, 5, 6, 7],
    [5, 6, 7, 8, 9]
]
lists1 = [
    [10, 2, 30, 4, 135, 15],
    [3, 40, 5, 6, 7, 15],
    [135, 6, 27, 8, 40, 15]
]
lists2 = [
    [1, 2, 3],
    [3, 4, 5],
    [5, 6, 7]
]

# Вызываем функцию count_same_elements с тестовыми данными
assert count_same_elements(*lists) == 5

assert count_same_elements(*lists1) == 4

assert count_same_elements(*lists2) == 2