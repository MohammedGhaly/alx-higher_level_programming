#!/usr/bin/python3
if "__main__" == __name__:
    import hidden_4
    for element in dir(hidden_4):
        if not ('__' in element and (element.index('__') == 0)):
            print(element)
