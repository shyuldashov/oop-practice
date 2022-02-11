# ОЧЕРЕДЬ
class Queue:
    def __init__(self):
        self.__data = list()

    def enqueue(self, item):
        self.__data.append(item)

    def dequeue(self):
        if len(self.__data) > 0:
            return self.__data.pop(0)
        return None

    def back(self):
        if len(self.__data) > 0:
            return self.__data[len(self.__data) - 1]
        return None

    def front(self):
        if len(self.__data) > 0:
            return self.__data[0]
        return None

    def is_empty(self):
        return len(self.__data) == 0

    def size(self):
        return len(self.__data)

    def clear(self):
        self.__data = list()

    def show(self):
        print(f", ".join(str(v) for v in self.__data))


# Game Hot Potato
def hot_potato(names, num):
    queue = Queue()

    for name in names:
        queue.enqueue(name)
    queue.show()
    eliminated = ''

    while queue.size() > 1:

        for i in range(int(num)):
            queue.enqueue(queue.dequeue())

        queue.show()
        eliminated = queue.dequeue()
        print(f"Player {eliminated} is out of the game")

    return queue.dequeue()


n = ['Alex', 'Sara', 'Mike', 'Julia']
winner = hot_potato(n, 5)
print(f"Winner {winner}!")


# Sorting students in ascending classes
def sorting(lst):
    q9 = Queue()
    q10 = Queue()
    q11 = Queue()

    for item in lst:
        student = item.split(' ')
        if int(student[0]) == 9:
            q9.enqueue(student[1])
        elif int(student[0]) == 10:
            q10.enqueue(student[1])
        elif int(student[0]) == 11:
            q11.enqueue(student[1])

    while q9.size() > 0:
        print('9 ', q9.dequeue())
    while q10.size() > 0:
        print('10 ', q10.dequeue())
    while q11.size() > 0:
        print('11 ', q11.dequeue())


s_lst = ['9 Wilhelmina', '10 Brendan', '11 Marva', '10 Fedora', '10 Cosima', '9 Brenna', '11 Charlene', '9 Genie']
sorting(s_lst)

import math
from random import randrange


class RadixSort:
    def __init__(self, n):
        self.__bins = list()
        self.__num = n
        for i in range(10):
            self.__bins.append(Queue())

    def distribute(self, digit):
        for i in range(10):
            if digit == 1:
                self.__bins[self.__num[i] % 10].enqueue(self.__num[i])
            else:
                self.__bins[math.floor(self.__num[i] // 10)].enqueue(self.__num[i])

    def collect(self):
        i = 0
        for digit in range(10):
            while not self.__bins[digit].is_empty():
                self.__num[i] = self.__bins[digit].dequeue()
                i += 1

    def show(self):
        return "".join(str(self.__num))


nums = [randrange(100) for i in range(10)]


rs = RadixSort(nums)
print("Before: ", rs.show())  # [9, 86, 6, 40, 23, 59, 73, 91, 2, 80]
rs.distribute(1)
rs.collect()
print("Middle: ", rs.show())  # [40, 80, 91, 2, 23, 73, 86, 6, 9, 59]
rs.distribute(10)
rs.collect()
print("After: ", rs.show())  # [2, 6, 9, 23, 40, 59, 73, 80, 86, 91]
