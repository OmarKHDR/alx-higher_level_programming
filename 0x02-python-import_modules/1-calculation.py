#!/usr/bin/python3
if __name__ == '__main__':
    import calculator_1 as cal
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, cal.add(a, b)))
    print("{} - {} = {}".format(a, b, cal.sub(a, b)))
    print("{} * {} = {}".format(a, b, cal.mul(a, b)))
    print("{} / {} = {}".format(a, b, cal.div(a, b)))

"""
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
"""
