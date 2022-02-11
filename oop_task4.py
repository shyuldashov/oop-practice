from PyStack import Stack

"""
К тупику со стороны пути 1 подъехал поезд. 
Необходимо сделать так, чтобы вагоны поезда шли по 
порядку попали на путь 2 по порядку (сначала первый, 
потом второй и т.д., считая от головы поезда, едущего 
по пути 2 в сторону от тупика).
"""


# train = 1 5 2 4 3  # Well done!
# train = 1 5 3 4 2  # Failing...
def redirect(train):
    stack = Stack()
    train = train.split()
    train = list(map(int, train))
    needed = 1

    for i in train:
        stack.push(i)
        if i == needed:
            stack.pop()
            needed += 1

        while stack.size() > 0:
            if stack.peek() == needed:
                stack.pop()
                needed += 1
            else:
                break

    if stack.is_empty():
        print("Well done!")
    else:
        print("Failing...")


while True:
    t = input("Enter wagon numbers: ")
    if t == '0':
        break
    redirect(t)
