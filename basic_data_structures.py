# Основной элемента списка - узел
class Node:
    def __init__(self, data):
        self.__data = data  # data (value)
        self.__next = None  # link to next item

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, node):
        self.__next = node


# node = Node(101)
# print(node.get_data())  # 101

# Связанный список
class LinkedList:
    idx = None  # index item

    def __init__(self):
        self.__head = None
        self.__tail = None

    def is_empty(self):
        return self.__head is None

    def add(self, item):
        node = Node(item)
        node.set_next(self.__head)  # The new node refers to None
        self.__head = node

        if self.__tail is None:
            self.__tail = node

    def size(self):
        current = self.__head
        count = 0
        while current is not None:
            current = current.get_next()
            count += 1

        return count

    def search(self, item):
        current = self.__head
        while current is not None:
            if current.get_data() == item:
                return True
            else:
                current = current.get_next()
        return False

    def remove(self, item):
        current = self.__head
        prev = None

        while True:
            if current.get_data() == item:
                break
            else:
                prev = current
                current = current.get_next()
        if prev is None:
            # remove the first node
            self.__head = current.get_next()
        else:
            prev.set_next(current.get_next())

    def append(self, item):
        node = Node(item)
        current = self.__tail
        current.set_next(node)
        self.__tail = node

    def index(self, item):
        if self.__head is None:
            return -1

        current = self.__head
        idx = 0

        while True:
            if current.get_data() == item:
                return idx
            else:
                current = current.get_next()
            idx += 1

    def __repr__(self):
        if self.__head is None:
            return '[]'

        current = self.__head
        out = '[' + str(current.get_data()) + ', '
        while not current.get_next() is None:
            current = current.get_next()
            out += str(current.get_data()) + ', '
        return out + ']'


my_lst = LinkedList()

my_lst.add(101)
my_lst.add(43)
my_lst.add(95)
my_lst.add(28)
my_lst.add(6)

print(my_lst.is_empty())  # False
print(my_lst.size())  # 5

print(my_lst.search(95))  # True
print(my_lst.search(5))  # False

print(my_lst)  # 6, 28, 95, 43, 101, ]

my_lst.remove(6)
print(my_lst)  # [28, 95, 43, 101, ]

my_lst.append(15)
print(my_lst)  # [28, 95, 43, 101, 15, ]
