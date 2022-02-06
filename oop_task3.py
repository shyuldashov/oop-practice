import abc
import random
from random import randint


class InterfaceShape(abc.ABC):
    """Interface for implementing geometric shapes"""

    @abc.abstractmethod
    def get_perimeter(self):
        """Returns the perimeter of the shape"""
        pass

    @abc.abstractmethod
    def get_area(self):
        """Returns the area of the shape"""
        pass

    @abc.abstractmethod
    def get_description(self):
        """Returns a description of the shape"""
        pass


class Circle(InterfaceShape):
    PI = 3.14

    def __init__(self, radius):
        self.__radius = radius
        self.__name = f"I'm a circle, my radius is = {self.__radius}"

    def get_perimeter(self):
        return 2 * self.__class__.PI * self.__radius

    def get_area(self):
        return self.__class__.PI * self.__radius ** 2

    def get_description(self):
        return self.__name


class Rectangle(InterfaceShape):

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__name = f"I'm a rectangle, my width is {self.__width} and my length is {self.__height} "

    def get_perimeter(self):
        return 2 * (self.__width + self.__height)

    def get_area(self):
        return self.__width * self.__height

    def get_description(self):
        return self.__name


class Square(InterfaceShape):

    def __init__(self, side):
        self.__side = side
        self.__name = f"I'm a square, my sides are = {self.__side}"

    def get_perimeter(self):
        return 4 * self.__side

    def get_area(self):
        return pow(self.__side, 2)

    def get_description(self):
        return self.__name


class Game:
    QUESTIONS = 3

    @staticmethod
    def get_shape():  # creates and returns an instance of the desired class
        shape = random.choice([Circle, Square, Rectangle])
        if shape == Circle:
            return Circle(randint(2, 18))

        if shape == Square:
            return Square(randint(3, 12))

        if shape == Rectangle:
            return Rectangle(randint(2, 10), randint(3, 18))

    @staticmethod
    def calculate(desc, msg, ans):  # asks questions and accepts and verifies answers
        print(desc)
        user_ans = input(f"Specify my {msg}: ")
        if ans == float(user_ans):
            print(f"Right!")
        else:
            print(f"Wrong! Right answer is {ans}")

    @classmethod
    def run(cls):  # calls the "get_shape" and "calculate" methods
        shape = cls.get_shape()
        cls.calculate(shape.get_description(), 'area', shape.get_area())
        cls.calculate(shape.get_description(), 'perimeter', shape.get_perimeter())

    @classmethod
    def play(cls):  # starts the main loop and calls the "run" method
        print(f"Hi! We are geometric shapes and we have {cls.QUESTIONS} questions")
        while True:
            playing = input("Start the game? Y/N: ")
            if playing.lower() == 'n':
                break
            cls.run()
        print("See you!")


Game.play()
