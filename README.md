# ООП

## Практикум

#### oop_task1.py Encapsulation
Создайте класс `Point`, который описывает точку с координатами `х` и `y`

_В классе необходимо описать:_

    1.конструктор, который принимает в качестве параметров значения для координат x и y
    2.метод move_to, который принимает в качестве параметров новые значения для координат x и y
    3.метод move_by, который принимает в качестве параметров новые значения для координат x и y относительно текущих значений
    4.свойства для изменения и получения значений координат x и y

_Необходимые условия, которые надо учесть:_

    5.при приведении объекта к строке должна возвращаться строка Я - точка: координата_x x координата_y

__Выводы (Encapsulation):__

    Класс — тип данных описывающий объект

    Объект — тип данных, экземпляр класса

    Метод объекта — сообщение, с помощью которого объекты общаются друг с другом

    Атрибут объекта — хранилище текущего состояния объекта

    Свойство объекта — интерфейс доступа к атрибутам объекта

    Класс — самостоятельный тип. Может иметь свои методы и атрибуты

---
#### oop_task2.py Inheritance


Создайте класс `User` и и его наследника класс `SuperUser`, которые описывают пользователя и супер-пользователя

_В классе `User` необходимо описать:_

    1.конструктор, который принимает в качестве параметров значения для атрибутов name, login и password
    2.свойства для изменения и получения значений атрибутов
    3.метод show_info, который печатает в произвольном формате значения атрибутов name и login
    4.атрибут класса count для хранения количества созданных экземпляров класса User

_Необходимые условия, которые надо учесть:_

После создания объекта

    5.атрибут name доступен и для чтения, и для изменения
    6.атрибут login доступен только для чтения
    7.атрибут password доступен только для изменения

_В классе `SuperUser` необходимо описать:_

    8.конструктор, который принимает в качестве параметров значения для атрибутов name, login, password и role
    9.свойство для изменения и получения значения атрибута role
    10.метод show_info, который печатает в произвольном формате значения атрибутов name, login и role
    11.атрибут класса count для хранения количества созданных экземпляров класса SuperUser

__Выводы (Inheritance):__
    
    - Классы могут расширяться путём наследования

    - Наследования является одним из важных средств повторного использования готового кода в ООП

    - Наследованный класс содержит в себе всё, что указано для всех его родительских классов

    - Переопределение (override) метода — одна из возможностей ООП, позволяющая подклассу обеспечивать 
        специфическую реализацию метода, уже реализованного в одном из суперклассов

    - Объект super используется для обращения к методу суперкласса из подкласса

    - Перегрузка (overload) операторов — один из способов реализации полиморфизма, заключающийся в 
        возможности одновременного существования нескольких различных вариантов применения оператора, 
        имеющих одно и то же имя, но различающихся типами параметров, к которым они применяются.

---

#### oop_task3.py *Game geometric shapes* (Object-Oriented Design, SOLID Principle)


1. Создайте классы `Circle`, `Rectangle` и `Square`, которые реализуют интерфейс `IShape`
2. Создайте класс `Game`, который описывает логику игру

_В классах `Circle`, `Rectangle` и `Square` необходимо описать:_

    - конструктор, который принимает в качестве параметров необходимые значения. 
        Для Круга таковым является его радиус, 
        для Прямоугольника - размеры двух его сторон, 
        для Квадрата - размер сторон.
    - методы, которые определены в интерфейсе IShape
    - метод get_description должен возвращать произвольную строку вида "Я - имя_фигуры параметры"

_В классе `Game` необходимо описать логику игру:_

    - Пользователю называется количество геометрических фигур участвующих в игре
    - Пользователю предлагается начать игру. В случае отказа, печатается строка "Спасибо за участие!"
    - Случайным образом создаётся объект - экземпляр одного из классов
    - Созданному объекту в конструктор передаются необходимые параметры со случайными значениями
    - Пользователю по очереди задаются вопросы касающиеся площади и периметра фигуры, на которые он должен ответить
    - В зависимости от правильности ответа пользователя печатается строка Правильно! или Ошибка! с правильным ответом
    - После каждой пары вопросов пользователю предлагается продолжить игру


#### SOLID Principle:
    Single Responsibility Principle
    Opened/Closed Principle
    Liscov's Substitution Principle
    Interface Segregation Principle
    Dependency Inversion Principle

__Выводы(Object-Oriented Design, SOLID)__
    
    - Объектно-ориентированное программирование — методология программирования, основанная на представлении 
        программы в виде совокупности объектов,каждый из которых является экземпляром определенного класса,
        а классы образуют иерархию наследования

    - Основные принципы ООП: инкапсуляция, наследование и полиморфизм

    - Объектно-ориентированный дизайн — методология определения поведения 
        классов/объектов и их взаимодействия для решения какой-либо задачи

    - Хороший ООД приложения позволяет при необходимости вносить изменения с минимальными 
        затратами и расширять его без изменения существующего кода

---

#### Сложность алгоритмов (Algorithms)

_"Одно решение - разные алгоритмы"_
    
    1.
    def palindrom_one(string):
        reverse = ""
        i = len(string)-1
        while i >= 0:
        reverse += string[i]
        i -= 1
        if string.lower() == reverse.lower():
            return True
        return False

    2. 
    def palindrom_two(string):
        mid = len(string) // 2
        j = len(string) - 1
        for i in range(mid):
            if string[i] != string[j]:
             return False
            j -= 1  
        return True
    
    3.
    def palindrom_three(string):
        s1 = list(string)
        s2 = s1.copy()
        s2.reverse()
        if s1 == s2:
            return True
        return False

__Выводы__

    - Асимптотический анализ — сравнение затрат времени алгоритмов, 
        выполняющих решение некоторой задачи, при больших объемах входных данных

    - Сложность алгоритма — это функция, позволяющая определить, как быстро 
        увеличивается время работы алгоритма с увеличением объёма данных

    - Основной оценкой роста, встречающейся в асимптотическом анализе является 
        'О-большое' — верхняя асимптотическая оценка роста временной функции

---

#### Алгоритмы поиска (Algorithms)
    
#### _Последовательный (линейный) поиск_

    Элемент   +    -    +/-
    -----------------------------
    Есть      1    n    n/2
    Нет       n    n    n


#### _Последовательный (линейный) поиск для упорядоченного списка_
    
    Элемент   +    -    +/-
    -----------------------------
    Есть      1    n    n/2
    Нет       n    n    n/2


#### _Бинарный поиск_
    
    Элемент   +          -       +/-
    ---------------------------------------
    Есть      1        log n    log n
    Нет       log n    log n    log n


__Выводы__

    
    - Поиск является одной из важнейших процедур обработки структурированной информации

    - Асимптотическая сложность алгоритма линейного поиска — O(n)

    - Асимптотическая сложность алгоритма бинарного поиска для упорядоченных списков — O(log n)

---

#### Рекурсия (Algorithms)
    
#### _Рекурсивный бинарный поиск_
    def binary_search(lst, key):
        if len(lst) == 0:
            return -1
        else:
            mid = len(lst) // 2
            if lst[mid] == key:
                return mid
            else:
                if key < lst[mid]:
                    return binary_search(lst[:mid], key)
                else:  
                    return binary_search(lst[mid+1:], key)

#### _Примеры_
    # Алгоритм Евклида
    def gcd(a, b): 
        if b == 0:
            return  a 
        return  gcd(b, a%b)
    
    # Простая рекурсивная функция
    def question(message):
        if input(message + ': ').lower() == 'всегда':
            return
        else:
            print('Подумайте...')
        question(message)

    question('Ваше кредо?')
    print("Молодец!")


__Выводы__

    - Рекурсивный алгоритм должен вызывать сам себя

    - Все рекурсивные алгоритмы должны иметь базовый случай

    - Рекурсивное решение может быть очень ресурсоёмким

    - Во многих случаях рекурсию можно заменять итерированием

---

#### Алгоритмы сортировки (Algorithms)
    
#### 1. _Сортировка пузырьком_
#### 2. _Сортировка вставками_
#### 3. _Сортировка слиянием_

__Выводы__

    - Алгоритм сортировки — это алгоритм для упорядочивания элементов в какой-либо структуре

    - У каждого алгоритма есть свои преимущества и недостатки

    - Важно выбрать тот алгоритм, который лучше всего подходит для решения конкретной задачи

    - Асимптотическая сложность алгоритмов сортировки вставками — O(n^2)
    
    - Асимптотическая сложность алгоритма сортировки слиянием — O(n log n),
        но требует дополнительного расхода памяти

---

### Структуры данных
#### Основные структуры данных
1. Массив
   * ###### Определение:
     * Структура данных, хранящая набор значений, идентифицируемых
       по индексу или набору индексов, принимающих значения из
       некоторого заданного непрерывного диапазона.
2. Связанный список
   * ###### Определение:
     * Коллекция элементов, каждый из которых хранится на соответсвующей
       позиции, но только по отношению к остальным (не подряд как
       последовательность в массиве) он может хранится в памяти где угодно. 
3. Основной элемент списка - УЗЕЛ
    * ###### УЗЕЛ
      * Это какой-то объект, у которого хранятся данные. У объекта(узел)
        как минимум должны быть две состовляющие:
        1. Значение (сам элемент списка)
        2. Ссылка на следуюзий узел

#### Абстрактные структуры данных

1. Стек
    * ###### Определение:
      * Стек имеет некий интерфейс допустимой операцией:
        Принцип стека Last-In-First-Out (LIFO)
        Есть два стандартных метода:
        1. push(item) - Добавление элемента
        2. pop() - Удаление(Возвращает) элемента

        и другие дополнительные операции,такие как:
      
        3. peek() - Посмотреть элемент
        4. is_empty() - проверить стек пустой или нет
        5. size() - узнать размер стека

2. Очередь
   * ###### Определение:
     * Очередь очень похоже на Стек, но идея в очереди в том, что первым извлекается 
        элемент, который первый вставили, то есть принцип навывается:
       
        Первым пришел, первым ушел - First-In-First-Out (FIFO)

---

#### oop_task4.py Abstract Data Structures (Stack)

Сортировка вагонов


К тупику со стороны пути 1 подъехал поезд. Необходимо сделать так, 
чтобы вагоны поезда шли по порядку попали на путь 2 по порядку 
(сначала первый, потом второй и т.д., считая от головы поезда, 
едущего по пути 2 в сторону от тупика).

При этом известно, в каком порядке изначально идут вагоны поезда.

 * с пути 1 попасть на путь 2, не заезжая в тупик, нельзя.
 * разрешается отцепить от поезда один или сразу несколько первых вагонов и завезти их в тупик
 * часть вагонов из тупика можно вывезти на путь 2
 * первые две операции можно повторять. При этом:
 * каждый вагон может лишь один раз заехать с пути 1 в тупик, а затем один раз выехать из тупика на путь 2
 * заезжать в тупик с пути 2 или выезжать из тупика на путь 1 запрещается


 * Формат входных данных
   * вводятся числа через пробел - номера вагонов в порядке от головы поезда, едущего по пути 1 в сторону тупика. 
     Вагоны пронумерованы натуральными числами от 1, каждое из которых встречается ровно один раз.
 * Формат выходных данных
   * напечатать строку "Вывели", если все вагоны удалось перегнать с пути 1 на путь 2
   * напечатать строку "Не получилось", если перегон вагонов невозможен

----

#### oop_task5.py Abstract Data Structures (Queue)

Объединение танцоров по парам

Дан текстовый файл со списком танцоров. В каждой строке сначала записан пол танцора (М - мальчик, Д - девочка), 
затем – имя и фамилия танцора. Все значения разделены пробелами

_Например:_
    
    # dancers.txt

    Д Зина Корзинкина
    М Вася Пупкин
    М Федя Сумкин
    М Вова Морковкин
    Д Катя Петрова
    М Петя Зайцев
    Д Маша Простоквашина
    М Дима Дрезина
    М Коля Лукошкин
    М Миша Косолапов
    Д Наташа Блинова

_Необходимо:_

* создать и описать класс DanceFloor, которому в конструктор передаётся имя файла
* в классе DanceFloor создать и описать метод dance, который должен напечатать информацию 
  о получившихся парах и о тех танцорах, которые остались без пары (их количество и имя первого танцора в очереди)
* Учтите, что:
    * мальчики танцуют только с девочками
    * девочки танцуют только с мальчиками

---
#### oop_task6.py The final task of OOP (Expression interpreter)
*__Создание простого интерпретатора арифметических выражений__*

Выражения содержат только целые числа, операторы и круглые скобки.

_Допустимые операторы в выражении:_

    +: сложение
    -: вычитание
    *: умножение
    /: деление
    ^: возведение в степень

Операторы не имеют приоритетов, приоритеты задаются круглыми скобками. 
Для удобства единое выражение тоже заключено в скобки.

Таким образом, результатом выражения `(1+((2+3)*(4*5)))` будет `101`, а выражения `(2+((2*3)/(4^5)))` будет `2`.
    
    import abc
    
    class InterpreterAbstract(abc.ABC):
        '''Интерпретатор кода'''
    
        def __init__(self, code):
            '''Принимает код'''
            self.code = code
    
        def execute(self):
            '''Запускает механизм исполнения кода
            Возвращает результат исполнения кода'''
            return self._parse()
    
        @abc.abstractmethod
        def _parse(self):
            '''Осуществляет парсинг кода.
            Вызывает _evaluate для исполнения выражений
            Возвращает результат исполнения кода в excecute''' 
            pass
    
        @abc.abstractmethod
        def _evaluate(self, code):
            '''Осуществляет вычисление выражения
            Возвращает результат выражения в _parse'''      
            pass    

Используя абстрактный класс `InterpreterAbstract` создайте и опишите класс `Interpreter`

* конструктор класса должен принимать код в виде строки.
* метод _parse должен разобрать строку кода посимвольно и передать её на исполнение методу _evaluate
* метод _evaluate должен вычислить выражение и вернуть его результат.


    interpreter = Interpreter('(1+((2+3)*(4*5)))')
    print(interpreter.execute()) # 101
    
    interpreter = Interpreter('(2+((2*3)/(4^5)))')
    print(interpreter.execute()) # 2

*__Подсказка__*

* вам надо создать два стека: для чисел и операторов
* продвигаясь по коду:
  * при нахождении числа добавляйте его в стек для чисел
  * при нахождении опрератора добавляйте его в стек для операторов
  * при нахождении символа ):
     * извлеките последний оператор из стека операторов
     * извлеките два последних числа из стека чисел
     * произведите над числами соответствующую операцию
     * добавьте результат операции в стек для чисел
* когда символы в коде закончатся, извлеките значение из стека 
чисел - это и будет результат всего выражения


*__Дополнительно 1__*

До сих пор мы игнорировали пробелы в коде, однако они могут присутствовать.
Например: `(1 + ( (   2 + 3 )*(  4  *5) )  )`
Сделайте так, чтобы код работал при любом количестве пробелов.
Заодно избавьтесь от первой и последней круглых скобок, что бы конечный пользователь о них не думал:
    
    interpreter = Interpreter('1 + ( ( 2 + 3 ) * ( 4 * 5 ) )')


*__Дополнительно 2__*

Измените конструктор, чтобы он мог принимать не только строку кода, но и файл с кодом.
В файле каждое выражение должно располагаться на отдельной строке.
В этом случае результатом выполнения кода должен быть список с результатами каждого выражения.
Например, если содержимое файла выглядит так:

    # exp.txt

    1 + ( ( 2 + 3 ) * ( 4 * 5 ) )
    2 + ( ( 2 * 3 ) / ( 4 ^ 5 ) )

то

    interpreter = Interpreter(file='code.txt')
    print(interpreter.execute()) # [101, 2]

*__Дополнительно 3__*

До этого момента, мы считали, что все скобки открыты, закрыты и вложены друг в друга правильно, однако это может быть не так.
Добавьте метод `_validate`, который будет перед исполнением кода проверять его сбалансированность скобок.
В случае нарушения баланса скобок, метод должен выбросить исключение об ошибке и завершить работу нашего интерпретатора.
