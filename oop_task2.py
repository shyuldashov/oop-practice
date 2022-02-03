class User:
    count = 0

    def __init__(self, name, login, password):
        self.__name = name
        self.__login = login
        self.__password = password
        __class__.count += 1  # User.count += 1

    def show_info(self):
        return f'Name: {self.__name}\nLogin: {self.__login}\n'

    # атрибут name доступен и для чтения, и для изменения
    @property
    def name(self):
        return self.__name  # чтения

    @name.setter
    def name(self, v):
        self.__name = v  # изменения

    # атрибут login доступен только для чтения
    @property
    def login(self):
        return self.__login  # чтения

    @login.setter
    def login(self, v):
        raise TypeError("==- Error! Can't change login -==")

    # атрибут password доступен только для изменения
    @property
    def password(self):
        return '******'  # чтения

    @password.setter
    def password(self, new_pass):
        self.__password = new_pass  # изменения


class SuperUser(User):
    count = 0

    def __init__(self, name, login, password, role):
        super().__init__(name, login, password)  # User.__init__(self, name, login, password)
        self.__role = role
        self.__class__.count += 1  # or SuperUser.count += 1 or __class__.count += 1
        User.count -= 1  # ...

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, new_role):
        self.__role = new_role

    def show_info(self):
        return super().show_info() + f'Role: {self.__role}\n'


user1 = User('Paul McCartney', 'paul', '1234')
user2 = User('George Harrison', 'george', '5678')
user3 = User('Richard Starkey', 'ringo', '8523')
user4 = User('Richard Starkey', 'ringo', '8523')
user5 = User('Richard Starkey', 'ringo', '8523')
user6 = User('Richard Starkey', 'ringo', '8523')
user7 = User('Richard Starkey', 'ringo', '8523')

admin1 = SuperUser('Mike Lennon', 'm_lennon', '0024300', 'admin')
admin2 = SuperUser('Nicolas Stones', 's_nicola', '124434', 'admin')
admin3 = SuperUser('Nicolas Stones', 's_nicola', '124434', 'admin')
admin4 = SuperUser('Nicolas Stones', 's_nicola', '124434', 'admin')

print('\nuser1.show_info()\n', user1.show_info())
print('admin2.show_info()\n', admin2.show_info())

users = User.count
print('\nAmount users = ', users)
admins = SuperUser.count
print('Amount admins = ', admins)

print('\nUser3 name = ', user3.name)
print('User3 password = ', user3.password)

user3.name = 'Carlos Watson'

total = f'Total users: {users}\nTotal superusers: {admins}'
print(total)

print('\nUser2 login = ', user2.login)
user2.login = 'my_new_login'
