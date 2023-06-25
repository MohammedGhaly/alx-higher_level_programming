#!/usr/bin/python3
"""
contains 'MyList' class
"""


class MyList(list):
    """
    class that inherits from list
    """

    def print_sorted(self):
        """
        sorts a list of integers
        """

        print(sorted(self))
