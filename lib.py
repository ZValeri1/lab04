def count_same_elements(*lists):
    frequency = {}
    for lst in lists:
        for element in lst:
            if element in frequency:
                frequency[element] += 1
            else:
                frequency[element] = 1
    return sum(value > 1 for value in frequency.values())



# Пример использования функции

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

list4 = [10, 2, 30, 4, 135, 15]
list5 = [3, 40, 5, 6, 7, 15]
list6 = [135, 6, 27, 8, 40, 15]

list7 = [1, 2, 3]
list8 = [3, 4, 5]
list9 = [5, 6, 7]


result = count_same_elements(list1, list2, list3)
print(result)  # Вывод: 5
result = count_same_elements(list4, list5, list6)
print(result)  # Вывод: 4
result = count_same_elements(list7, list8, list9)
print(result)  # Вывод: 2