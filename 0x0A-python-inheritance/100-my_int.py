#!/usr/bin/python3
"""
contains rebel class 'MyInt'
"""


class MyInt(int):
    """
    a class that inherits from int
    has opposite logic of operators '==' and '!='
    """
    def __init__(self, value: int) -> None:
        pass

    def __eq__(self, __value: object) -> bool:
        return not super().__eq__(__value)

    def __ne__(self, __value: object) -> bool:
        return not super().__ne__(__value)
