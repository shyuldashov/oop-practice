# Example 1 : Exponentiation

def pow_one(base, exp):  # T() = 1 + 2n --> O(n)
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result


def pow_two(base, exp):  # T() = 1 + log n --> O(log n)
    result = 1
    while exp > 0:
        if exp % 2 == 0:
            base *= base
            exp //= 2  # log
        else:
            result *= base
            exp -= 1
    return result


# Example 2 : Mini practice

def one(array):  # T() = 1 + n^2 + 1 --> O(n^2)
    result = 0
    for i in array:
        for j in array:
            result += i * j
    return result


def two(array):  # T() = 1 + n + n --> 2n --> O(n)
    result = 0
    for i in array:
        result += 1
    for j in array:
        result -= 1
    return result


def three(n):  # T() = log n --> O(log n)
    while n > 0:
        n += 2
        n //= 2  # log
    return n


def four(n):  # T() = 1 + n + 2 * n + 2 --> 3 + 2n^2 --> O(n^2)
    sum_ = 0
    for i in range(n):
        j = 0
        cnt = 50 * n
        while j < cnt:
            j += 1
            sum_ += 1
    return sum_


def five(n):  # T() = n + 1 + 1 --> O(n)
    for i in range(n):
        while i % 2 != 0:  # this is equivalent to the "if" : const
            print(i)
            i -= 1
        print("Done")


def six(n):  # T() = n * n^2 + 1 --> O(n^3)
    for i in range(n):
        cnt = n * n
        for j in range(cnt):  # this loop is equivalent to a constant
            if j == 4:
                return -1
            print("Done")


# Example 3
def anagram(s1: str, s2: str):  # T() 1 + 1 + 1 + n + n + n + 1 = 4 + 3n --> O(n)
    """
    An anagram of a string is another string that contains the same characters, only the order of
    characters can be different. For example, “triangle” and “integral” are an anagram of each other

    :param s1:
    :param s2:
    :return: str
    """

    if len(s1) != len(s2):  # const
        return "The length of the string is not equivalent"

    s1_lst = list(s1)  # const
    s2_lst = list(s2)  # const

    s1_lst.sort()  # n
    s2_lst.sort()  # n

    for i in range(len(s1)):  # n
        if s1_lst[i] != s2_lst[i]:  # const
            return "These strings are not an anagram"

    return "These strings are an anagram"


print(anagram('listen', 'silent'))  # These strings are an anagram

print(anagram('triangle', 'integral'))  # These strings are an anagram

print(anagram('abc', 'dabcf'))  # The length of the string is not equivalent

print(anagram('abc', 'xyz'))  # These strings are not an anagram
