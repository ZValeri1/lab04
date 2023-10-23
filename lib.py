def count_same_elements(*lists):
    frequency = {}
    for lst in lists:
        for element in lst:
            if element in frequency:
                frequency[element] += 1
            else:
                frequency[element] = 1
    return sum(value > 1 for value in frequency.values())

from lib import count_same_elements

# Пример использования функции
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

result = count_same_elements(list1, list2, list3)
print(result)  # Вывод: 3