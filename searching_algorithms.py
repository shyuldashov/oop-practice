# АЛГОРИТМЫ

# 1.Алгоритмы поиска

# Последовательный (линейный) поиск
def linear_search(lst, key):
    for idx, item in enumerate(lst):
        if key == item:
            return idx  # Возврат индекса первого найденного элемента
    return -1  # Последовательность не содержит искомое


# Последовательный (линейный) поиск для упорядоченного списка
def ordered_linear_search(lst, key):
    for idx, item in enumerate(lst):
        if item == key:
            return idx
        elif item > key:  # Если полученный элемент больше искомого элемента возвращается False
            return -1
        return -1


# Бинарный поиск (семейства: Разделяй и Властвуй)
def main_binary_search(lst, key):
    first = 0
    last = len(lst) - 1

    while first <= last:
        mid = (first + last) // 2
        if lst[mid] == key:
            return mid
        else:
            if key < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return -1


# Related questions

# 1. Как работает enumerate()
