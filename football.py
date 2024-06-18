# def foo():
#     try:
#         return 1

#     finally:
#         return 3


# print(foo())
from typing import Any


class Tester:
    def __init__(self, id):
        self.id = str(id)
        id = "224"


tester = Tester(12)
print(tester.id)
