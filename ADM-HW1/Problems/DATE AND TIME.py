1 CALENDAR MODUEL
import datetime
import calendar

m,d,y = map(int, input().split())
input_date = datetime.date(y,m,d)
print(calendar.day_name[input_date.weekday()].upper())

2 TIME DELTA
import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    time_layout = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, time_layout)
    t2 = datetime.strptime(t2, time_layout)
    return str(int(abs(t1-t2).total_seconds()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
