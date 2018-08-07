class Chess(object):
    def __init__(self, height=0, width=0):
        self.height = int(height)
        self.width = int(width)
        self.white = '* '
        self.black = ' *'
        self.result = ''

    def set_white_elements(self, white=str):
        self.white = white

    def set_black_elements(self, black=str):
        self.black = black

    def create_board(self, number):
        while number > 1:
            self.result += ''.join(f"{self.white}" * number, "\n")
            self.result += ''.join(f"{self.black}" * number, "\n")
            number -= 2
        while number == 1:
            self.result += ''.join(f"{self.white}" * number, "\n")
            self.result += ''.join(f"{self.black}" * number, "\n")
            number -= 1
        return self.result


class ChessBoard(Chess):
    """ Enter 2 parameters of a chessboard as a number: height and width.

    """

    def __str__(self):
        return f"Height: {self.height}, Width: {self.width}"

    def __call__(self):
        counter, end = divmod(self.height, 2)
        try:
            Chess.create_board(counter)
            Chess.create_board(end)
        except TypeError:
            return self.__doc__


if __name__ == "__main__":
    chess = ChessBoard(7, 9)
