#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = str(number)
length = len(number_str)
last_digit = int(number_str[length - 1])

if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
elif last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number} is {last_digit} and is less "
          f"than 6")
