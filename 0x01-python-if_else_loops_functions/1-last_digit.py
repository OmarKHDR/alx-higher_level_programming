#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = ((-1 * number) % 10 * -1, number % 10)[number >= 0]
print("Last digit of", number, "is", last, end=" ")
if last == 0:
    print("and is 0")
elif last > 5:
    print("and is greater than 5")
else:
    print("and is less than 6 and not 0")
