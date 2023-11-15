from lib import count_same_elements

# Тестовые данные
lists = [
    [1, 2, 3, 4, 5],
    [3, 4, 5, 6, 7],
    [5, 6, 7, 8, 9]
]

# Вызываем функцию count_same_elements с тестовыми данными
result = count_same_elements(*lists)

# Проверяем результат
expected_result = 5
if result == expected_result:
    print("Тест пройден 🎉")
else:
    print("Тест не пройден ❌")