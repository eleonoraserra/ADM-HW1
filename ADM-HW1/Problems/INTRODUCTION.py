SAY HELLO WORLD WITH PYTHON
print("Hello, World!")

PYTON IF-ELSE
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input().strip())

if N % 2 != 0:
    print ("Weird")
else:
    if N >= 2 and N <= 5:
        print ("Not Weird")
    elif N >= 6 and N <=20:
        print ("Weird")
    elif N >= 20:
        print ("Not Weird")

ARITHMETIC OPERATORS
if __name__ == '__main__':
    a = int(input())
    b = int(input())

print (a + b)
print (a - b)
print (a * b)

PYTHON DIVISION
if __name__ == '__main__':
    a = int(input())
    b = int(input())

print (a // b)
print (a / b)

LOOPS
if __name__ == '__main__':
    n = int(input())

for i in range(0,n):
    print (i**2)

WRITE A FUNCTION
def is_leap(year):
    leap = False

    # Write your logic here
    if year%4 == 0:
        leap = True
        if year%100 == 0 and  year%400 != 0:
            leap = False
    return leap

PRINT A FUNCTION
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1) :
        print(i,end='', sep='')

