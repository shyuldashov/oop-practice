class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __repr__(self):
        return f'Я - точка: {self.__x} x {self.__y}'

    def move_to(self, x, y):
        self.__x = x
        self.__y = y

    def move_by(self, x, y):
        self.__x += x  # self.__x = self.__x + x
        self.__y += y  # self.__y = self.__y + y

    # def get_x(self):
    #     return self.__x
    #
    # def set_x(self, value):
    #     self.__x = value
    #
    # def get_y(self):
    #     return self.__y
    #
    # def set_y(self, value):
    #     self.__y = value
    #
    # x = property(get_x, set_x)
    # y = property(get_y, set_y)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value


point = Point(10, 20)

print(point)  # Я - точка: 10 x 20

point.move_to(100, 200)
print(point.x, ' : ', point.y)  # 100  :  200

point.move_by(10, 20)
print(point.x, ' : ', point.y)  # 110  :  220

point.x = 30
point.y = 40
print(point)  # Я - точка: 30 x 40
