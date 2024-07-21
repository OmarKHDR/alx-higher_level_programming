#!/usr/bin/python3
"""crazy code"""


class MyInt(int):
    """ class with ducked up methods"""

    def __init__(self, val) -> None:
        """init
            args: val
        """
        self.val = val

    def __eq__(self, obj) -> bool:
        """ ==
            args:
            obj
        """
        return self.val != obj

    def __ne__(self, obj) -> bool:
        """ !=
            args:
            obj
        """
        return obj == self.val
