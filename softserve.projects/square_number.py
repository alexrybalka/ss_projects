from functools import lru_cache


class WrongNumberError(TypeError):
    def __init__(self, *args, **kwargs):
        TypeError.__init__(self, *args, **kwargs)


class SquareNumber:
    """ Return all the numbers which square is less than the number you enter.
    Number should be integer.

    """
    def __init__(self, entered):
        if validator(entered):
            self.number = int(entered)
        else:
            print(self.__doc__)

    @lru_cache(maxsize=32)
    def create_sequence(self):
        sequence = filter(lambda x: x ** 2 < self.number, range(1, self.number))
        return list(sequence)

    @staticmethod
    def validator(number):
        if len(number) == 1:
            try:
                number = int(number)
                return True
            except WrongNumberError:
                return False
        else:
            return False


if __name__ == "__main__":
    number = input("Enter number for what you want get a square sequence: ")
    a = SquareNumber(number)
    print(a.create_sequence())
