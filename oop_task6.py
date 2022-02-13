import abc

from PyStack import Stack


class InterpreterAbstract(abc.ABC):
    """Code Interpreter"""

    def __init__(self, exp):
        """Accept expression"""
        self.exp = exp

    def execute(self):
        """
        Starts the expression execution engine
        :return: the result of executing the expression
        """
        return self._parse()

    @abc.abstractmethod
    def _parse(self):
        """
        Performs exp parsing.
        Calls _evaluate to evaluate expressions
        :return: the result of expression execution in exp
        """
        return self._evaluate(self.exp)

    @abc.abstractmethod
    def _evaluate(self, exp):
        """
        Evaluates an expression
        :param exp:
        :return: the result of the expression in _parse
        """
        pass


class Interpreter(InterpreterAbstract):
    def __init__(self, exp=None, file=None):
        self.__file = file
        self.__exp = exp
        self.__nums = Stack()
        self.__ops = Stack()  # Stack for operators
        super().__init__(exp)

    def _parse(self):
        if self.__file is not None:
            line_lst = []

            with open(self.__file, 'r', encoding='utf-8') as f:
                lines = f.read()
                lines = lines.strip().split(sep='\n')

                for line in lines:
                    s = ''.join(line.split())
                    s = '(' + s + ')'
                    line_lst.append(self._validate(s))

                return line_lst

        elif self.__exp is not None:
            a = self.__exp.replace(' ', '')
            a = '(' + a + ')'
            return self._validate(a)

        else:
            raise AttributeError('Specify a file name or enter an expression!')

    def _validate(self, exp):
        bks = Stack()  # Stack for brackets

        for char in exp:
            if char == '(':
                bks.push(char)
            elif char == ')':
                bks.pop()

        if bks.is_empty():
            return self._evaluate(exp)

        raise TypeError('Incorrect expression, missing or extra brackets')

    def _evaluate(self, exp):
        ops = ['+', '-', '*', '/', '^']

        for item in exp:
            if item == '(':
                continue

            elif item in ops:
                self.__ops.push(item)

            elif item == ')':
                o = self.__ops.pop()
                val = self.__nums.pop()

                if o == '+':
                    val = int(self.__nums.pop()) + int(val)

                elif o == '-':
                    val = int(self.__nums.pop()) - int(val)

                elif o == '*':
                    val = int(self.__nums.pop()) * int(val)

                elif o == '/':
                    val = int(self.__nums.pop()) / int(val)

                elif o == '^':
                    val = int(self.__nums.pop()) ** int(val)

                self.__nums.push(val)

            else:
                self.__nums.push(item)

        return self.__nums.pop()


interpreter = Interpreter('( 1 +  ((   2+ 3 )   * (    4*   5)))')
print(interpreter.execute())  # 101
interpreter = Interpreter('2+((2*3)/(4^5))')
print(interpreter.execute())  # 2

interpreter = Interpreter(file='exp.txt')
print(interpreter.execute())  # [101, 2]
