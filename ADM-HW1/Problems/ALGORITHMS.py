1 BIRTHDAY CAKE
import math
import os
import random
import re
import sys

# Complete the 'birthdayCakeCandles' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
def birthdayCakeCandles(candles):
    candles.sort()

    result = candles.count(candles[len(candles)-1])
    return result

2 NUMBER LINE
import math
import os
import random
import re
import sys

# Complete the 'kangaroo' function below.
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#
def kangaroo(x1, v1, x2, v2):
    if x1 < x2 and v1 < v2:
        return 'NO'
    else:
        if v1!=v2 and (x2-x1)%(v2-v1)==0:
            return 'YES'
        else:
            return 'NO'

3 ADVERTISING
import math
import os
import random
import re
import sys

# Complete the 'viralAdvertising' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.

def viralAdvertising(n):
    Advtotal = 5

    totLikes = 0
    for day in range(n):
        Likes = Advtotal // 2
        totLikes += Likes
        Advtotal = Likes * 3

    return totLikes

4 INSERTION SORTING 1
import math
import os
import random
import re
import sys
# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    prova = arr[-1]

    for ind in range(len(arr) - 2, -1, -1):
        if arr[ind] > prova:
            arr[ind + 1] = arr[ind]
            print(" ".join(map(str, arr)))
        else:
            arr[ind + 1] = prova
            print(" ".join(map(str, arr)))
            break
    if arr[0] > prova:
        arr[0] = prova
        print(" ".join(map(str, arr)))

5 INSERTION SORT 2
import math
import os
import random
import re
import sys
# Complete the insertionSort2 function below.
def insertionSort1(n, arr):
    prova = arr[n]
    for ind in range(n - 1, -1, -1):
        if arr[ind] > prova:
            arr[ind + 1] = arr[ind]
        else:
            arr[ind + 1] = prova
            break
    if arr[0] > prova:
        arr[0] = prova

def insertionSort2(n, arr):
    for ind in range(1, len(arr)):
        insertionSort1(ind, arr)
        print(" ".join(map(str, arr)))

6 RECURSIVE DIGIT SUM
import math
import os
import random
import re
import sys

def superDigit(n, k):
    digits = map(int, list(n))
    return get_superDigit(str(sum(digits) * k))

def get_superDigit(p):
    if len(p) == 1:
        return int(p)
    else:
        digits = map(int, list(p))
        return get_superDigit(str(sum(digits)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()