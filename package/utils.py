import math

import datatable as dt


def hello(name: str) -> str:
    return f'Hello {name}'


class Numbers:
    def __init__(self):
        self.zero = 0
        self.one = 1

    def add(self, a: int, b: int) -> int:
        return a + b


class DataTable:
    def __init__(self):
        self.DT = dt.Frame(A=range(5), B=[1.7, 3.4, 0, None, -math.inf], stypes={"A": dt.int64})
