#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numb = abs(number) % 10
numb = abs(numb)
if number < 0:
    print("last digit of {} is -{} and is less than 6 and not 0".format(number, numb))
elif numb > 5:
    print("last digit of {} is {} and is greater than 5".format(number, numb))
elif numb == 0:
    print("last digit of {} is {} and is 0".format(number, numb)) 
else: 
    print("last digit of {} is {} and is less than 6 and not 0".format(number, numb))
