#!/usr/bin/python3
"""

a module that includes 'text_indentation' function

"""


def text_indentation(text):
    """ Functoin to print a text with 2 new lines after specific ".:?"

   Args:
        text:
           input string

    Returns:
        Success

    Raises:
        TypeError: If the text isn't a string


    """

    err_msg = "text must be a string"
    if type(text) is not str:
        raise TypeError(err_msg)

    tmp = text[:]

    for sep in ".:?":
        text_list = tmp.split(sep)
        tmp = ""
        for element in text_list:
            element = element.strip(" ")
            tmp = element + sep if tmp is "" else tmp + "\n\n" + element + sep
    print(tmp[:-3], end="")
