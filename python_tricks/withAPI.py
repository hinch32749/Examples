# Написание красивых API с менеджерами контекста
import functools


class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 4
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 4

    def print(self, text):
        print(' ' * self.level + text)


with Indenter() as indent:
    indent.print('Hello!')
    with indent:
        indent.print('Great!')
        with indent:
            indent.print('Bounjurna!')
    indent.print('Hey')


