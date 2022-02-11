from PyQueue import Queue


class DanceFloor:
    def __init__(self, file):
        self.__boy = Queue()
        self.__girl = Queue()
        self.__read_file(file)

    def __read_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            read = f.readlines()

            for line in read:
                dancer = line.strip().split(" ")
                if dancer[0].lower() == 'м':
                    self.__boy.enqueue(dancer)
                elif dancer[0].lower() == 'д':
                    self.__girl.enqueue(dancer)

    def dance(self):
        print(f"Образовались следующие пары:")

        while True:
            if self.__girl.size() and self.__boy.size() != 0:
                print(f"\n{self.__boy.dequeue()[1]} и {self.__girl.dequeue()[1]}")

            elif self.__girl.size() == 0 and self.__boy.size() > 0:
                print(f"\nМальчиков в очереди: {self.__boy.size()} и первый из них — {self.__boy.front()[1]}")
                break
            elif self.__boy.size() == 0 and self.__girl.size() > 0:
                print(f"\nДевочек в очереди: {self.__girl.size()} и первый из них — {self.__girl.front()[1]}")
                break
            else:
                print(f"\nВсе нашли свою пару и все счастливы!!!")
                break


process = DanceFloor('dancers.txt')
process.dance()
