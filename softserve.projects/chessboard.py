class ChessBoard:
    """ Enter 2 parameters of a chessboard as a number: height and width.

    """

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.white = ' '
        self.black = '*'
        self.result = []
        self.validate()

    def validate(self):
        if all((isinstance(self.width, int), isinstance(self.height, int))):
            return True
        else:
            return self.__doc__

    def set_white_elements(self, white):
        self.white = white

    def set_black_elements(self, black):
        self.black = black

    def create_board(self, number):
        line = ''
        if self.height % 2 == 1:
            for i in range(self.width):
                if i % 2 == 1:
                    line += ' {}'.format(self.black)
                else:
                    line += '{} '.format(self.white)
                self.result.append(line)
        else:
            for i in range(self.width):
                if i % 2 == 1:
                    line += '{} '.format(self.white)
                else:
                    line += ' {}'.format(self.black)
                self.result.append(line)
        return self.result

    def __str__(self):
        return 'Height: {}, Width: {}'.format(self.height, self.width)

    def show_board(self):
        counter, end = divmod(self.height, 2)
        self.create_board(counter)
        self.create_board(end)


if __name__ == '__main__':
    chess = ChessBoard(7, 9)
    chess.show_board()
