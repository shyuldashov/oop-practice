# СТЕК
class Stack:
    def __init__(self):
        self.__data = list()

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        if len(self.__data) > 0:
            return self.__data.pop()
        return None

    def peek(self):
        if len(self.__data) > 0:
            # return self.__data[-1]
            return self.__data[len(self.__data) - 1]
        return None

    def is_empty(self):
        return len(self.__data) == 0
        # if len(self.__data) > 0:
        #     return True
        # return False

    def size(self):
        return len(self.__data)

    def show(self):
        print(f"\n".join(str(v) for v in self.__data))


# # Простой пример: проверка полиндрома
def is_palindrome(word):
    word = word.lower().replace(" ", "")
    r_word = ""

    stack = Stack()

    for char in word:
        stack.push(char)

    while not stack.is_empty():
        r_word += stack.pop()

    return word == r_word


print(is_palindrome("Civic"))
print(is_palindrome("HeLlo"))
print(is_palindrome("А роза упала на лапу Азора"))


#  Концепция сбалансированных скобок
# №1
def bracket_checker(string):
    stack = Stack()

    for char in string:
        if char == '(':
            stack.push(char)
        else:
            if stack.is_empty():
                return False
            else:
                stack.pop()

    if stack.is_empty():
        return True
    return False


print('Bracket checker: ', bracket_checker("((((()))))"))  # True
print('Bracket checker: ', bracket_checker("((3((( )))))"))  # False


def brackets_checker(s):
    stack = Stack()

    open_allowed = '([{'
    close_allowed = ')]}'

    def matches(opened, closed):
        try:
            return open_allowed.index(opened) == close_allowed.index(closed)
        except:
            return False

    for char in s:
        if char in open_allowed:
            stack.push(char)
        else:
            if not matches(stack.pop(), char):
                return False

    if stack.is_empty():
        return True
    return False


print('Bracket checker: ', brackets_checker("([{}])"))  # True
print('Brackets checker: ', brackets_checker("{[([{()}])]}"))  # True
print('Bracket checker: ', brackets_checker("([}]{}])"))  # False

# Преобразование из десятичной в двоичную систему
import math


def convertor(dec, base=2):
    stack = Stack()

    allowed = '0123456789ABCDEF'

    while dec > 0:
        stack.push(dec % base)
        dec = math.floor(dec / base)
    s = ""
    while not stack.is_empty():
        # s += str(stack.pop())
        s += allowed[stack.pop()]
    return s


print(convertor(196))  # 11000100
print(convertor(196, 8))  # 304
print(convertor(196, 16))  # C4


def fact(num):
    stack = Stack()

    while num > 1:
        stack.push(num)
        num = num - 1

    prod = 1

    while stack.size() > 0:
        prod *= stack.pop()

    return prod


print(fact(0))  # 1
