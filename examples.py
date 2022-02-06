class Ninja:
    """
    This class was created simply as an example of "method overriding"
    :eq
    :lt
    :gt
    """

    def __init__(self, age):
        self.__age = age

    def __eq__(self, obj):
        return self.__age == obj.__age

    def __lt__(self, obj):
        return self.__age < obj.__age

    def __gt__(self, obj):
        return self.__age > obj.__age


Mike = Ninja(15)
Don = Ninja(12)
Leo = Ninja(20)
Raff = Ninja(15)

print('Mike == Raff: ', Mike == Raff)
print('Don > Leo: ', Don > Leo)
print('Raff < Leo: ', Raff < Leo)


class BabesNinja(Ninja):
    def __init__(self, age, name):
        self._name = name
        super().__init__(age)  # Ninja.__init__(self, age)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


Michelangelo = BabesNinja(4, 'Michelangelo')
Donatello = BabesNinja(2, 'Donatello')
Leonardo = BabesNinja(10, 'Leonardo')
Raphael = BabesNinja(8, 'Raphael')

print(Michelangelo.name)
print(Donatello.name)
print(Leonardo.name)

Leonardo.name = "Jr.Leo"
print(Leonardo.name)

import abc


class MyAbstractClass(abc.ABC):

    @abc.abstractmethod
    def my_method(self):
        pass


class MyClass(MyAbstractClass):

    def __init__(self):
        pass

    def my_method(self):
        pass


obj = MyClass()
print(obj)


#  Liskov's Substitution Principle¶
class Bird:
    def __init__(self):
        pass

    def fly(self):
        print('Flew...')


def flew(bird):
    if isinstance(bird, Bird):
        bird.fly()


class Falcon(Bird):
    pass


falcon = Falcon()
flew(falcon)


class Ostrich(Bird):
    pass


ostrich = Ostrich()
flew(ostrich)  # is a bug


# # Fix a bug
# class InterfaceBird(abc.ABC):
#     @abc.abstractmethod
#     def eat(self):
#         pass
#
#     @abc.abstractmethod
#     def walk(self):
#         pass
#
#     @abc.abstractmethod
#     def tweet(self):
#         pass
#
#     # @abc.abstractmethod  # is a bug
#     # def fly(self):
#     #     pass
#
#
# # fix a bug
# class InterfaceFlyingBird(InterfaceBird):
#
#     @abc.abstractmethod
#     def fly(self):
#         print('Flew...')
#
#
# def flew2(bird):
#     if isinstance(bird, InterfaceFlyingBird):
#         bird.fly()
#
#
# class Falcon2(InterfaceFlyingBird):
#     def eat(self):
#         print('Ate...')
#
#     def fly(self):
#         print('Flew...')
#
#
# class Ostrich2(InterfaceBird):
#
#     def eat(self):
#         print('Ate...')
#
#
# ostrich = Ostrich()
