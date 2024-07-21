#!/usr/bin/python3
"""crazy code"""


class MyInt(int):
    def __init__(self, val) -> None:
        self.val = val

    def __eq__(self, obj) -> bool:
        return self.val != obj

    def __ne__(self, obj) -> bool:
        return obj == self.val
