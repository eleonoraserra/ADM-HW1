1
N, X = input().split()
A = list()
for _ in range(int(X)):
    B = map(float, input().split())
    A.append(B)
for i in zip(*A):
    print( sum(i)/len(i) )

2 ATHLETE - SORT SORT
import math
import os
import random
import re
import sys

n, m = map(int, input().split())
rows = [input() for _ in range(n)]
k = int(input())
for row in sorted(rows, key=lambda row: int(row.split()[k])):
    print(row)

3 GINSORT
S = list(input())

LETTERS = []
low = []
up = []
DIGITS = []
odd = []
even = []

for c in S:
    if c.isalpha():
        LETTERS.append(c)
    if c.isnumeric():
        DIGITS.append(c)

for s in LETTERS:
    if s.isupper():
        up.append(s)
    else:
        low.append(s)

for n in DIGITS:
    n = int(n)
    if n % 2 == 1:
        n = str(n)
        odd.append(n)
    else:
        n = str(n)
        even.append(n)

A = "".join(sorted(low) + sorted(up) + sorted(odd) + sorted(even))
print(A)