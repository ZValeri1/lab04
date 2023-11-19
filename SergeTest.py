from lib import count_same_elements

testLists1 = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [1, 4, 6, 21, 20, 45, 1, 4, 12, 8]
]
testLists2 = [
    [5, 11, 12, 13, 14, 15, 16, 17, 18, 19],
    [20, 5, 21, 22, 23, 24, 25, 26, 27, 28, 29],
    [30, 37, 31, 32, 33, 34, 35, 36, 5, 38, 39],
    [40, 50, 41, 42, 43, 44, 45, 46, 47, 48, 49, 5]
]
testLists3 = [
    [2, 5, 2, 8, 5, 3, 2],
    [1, 1, 3, 7, 3, 1, 9],
    [4, 6, 2, 4, 7, 2, 6],
    [8, 3, 8, 1, 5, 3, 8],
    [6, 9, 7, 6, 4, 9, 2]
]

try:
    assert count_same_elements(*testLists1) == 6
except AssertionError:
    print("testLists1 не пройден")

try:
    assert count_same_elements(*testLists2) == 1
except AssertionError:
    print("testLists2 не пройден")

try:
    assert count_same_elements(*testLists3) == 9
except AssertionError:
    print("testLists3 не пройден")
