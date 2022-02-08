# 2.Рекурсия

# Всё тот же бинарный поиск
def binary_search(lst, key):
    if len(lst) == 0:
        return -1
    else:
        mid = len(lst) // 2
        if lst[mid] == key:
            return mid
        else:
            if key < lst[mid]:
                return binary_search(lst[:mid], key)
            else:
                return binary_search(lst[mid + 1:], key)


# Простой пример рекурсии
def question(message):
    if input(message + ": ").lower() == 'always':
        return
    else:
        print("Think...")
    question(message)


question("Is your credo")
print("Well done!")


# Алгоритм Евклида
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# Число Фибоначчи
def fib(n):  # O(n)
    a, b = 0, 1

    for _ in range(n - 1):
        a, b = b, a + b

    return a


# Число Фибоначчи + список чисел
def fib_lst(n):
    f_lst = [0, 1, 1]
    for i in range(3, n):
        f_lst.append(f_lst[i - 1] + f_lst[i - 2])
    return f_lst[len(f_lst) - 1]