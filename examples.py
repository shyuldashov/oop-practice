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
