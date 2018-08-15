class FiboSequence:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    @staticmethod
    def get_fibo_sequence(number):
        bottom_up = [None] * (number + 1)
        bottom_up[1] = 1
        bottom_up[2] = 1
        for i in range(3, number+1):
            bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
        return bottom_up[:number]

    def show_fibo_sequence(self):
        to_return = get_fibo_sequence(self.end)
        return to_return[self.start:]


a = FiboSequence(2, 23)
print(a.show_fibo_sequence())
