import sys
import argparse

from itertools import product
from functools import lru_cache


class Tickets:

    @lru_cache(maxsize=32)
    def __init__(self):
        self.tickets = list(product(range(10), repeat=6))


class LuckyMoscowTicket(Tickets):

    def __init__(self):
        super(LuckyMoscowTicket, self).__init__()

    def lucky_counter(self):
        return len(list(filter(lambda x: sum(x[:3]) == sum(x[3:]), self.tickets)))


class LuckyPieterTicket(Tickets):

    def __init__(self):
        super(LuckyPieterTicket, self).__init__()

    def lucky_counter(self):
        return len(list(filter(lambda x: sum(x[::2]) == sum(x[1::2]), self.tickets)))


if __name__ == '__main__':
    a = LuckyMoscowTicket()
    print(a.lucky_counter())
    b = LuckyPieterTicket()
    print(b.lucky_counter())