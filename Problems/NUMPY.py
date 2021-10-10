1 EYE IDENTITY
import numpy
print(str(numpy.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))

2 ARRAYS
import numpy
def arrays(arr):
    # complete this function
    # use numpy.array
    return(numpy.array(arr[::-1], float))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

3 SHAPE AND RESHAPE
import numpy
a=numpy.array(list(map(int,input().split())))
a.shape=(3,3)
print(a)

4 TRAMPOSE AND FLATTEN
import numpy
N, M = map(int, input().split())
array = numpy.array([input().strip().split() for _ in range(N)], int)
print (array.transpose())
print (array.flatten())

5 CONCATENATE
import numpy

a, b, c = map(int,input().split())
array_1 = numpy.array([input().split() for _ in range(a)],int)
array_2 = numpy.array([input().split() for _ in range(b)],int)
print(numpy.concatenate((array_1, array_2), axis = 0))

6 ZERO AND ONES
import numpy
x= list(map(int,input().split()))
print(numpy.zeros(x,int), numpy.ones(x,int), sep='\n')

7 ARRAY MATH
import numpy
N, M = map(int, input().split())
A, B = (numpy.array([input().split() for _ in range(N)], dtype=int) for _ in range(2))
print(A+B, A-B, A*B, A//B, A%B, A**B, sep='\n')

8 FLOOR, CEIL AND RINT
import numpy
numpy.set_printoptions(sign=' ')
A = numpy.array(input().split(),float)
print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))

9 SUM AND PROD
import numpy
N, M = map(int, input().split())
x = numpy.array([input().split() for _ in range(N)],int)
print(numpy.prod(numpy.sum(x, axis=0), axis=0))

10 MIN AND MAX
import numpy
N, M = map(int, input().split())
print(numpy.array([input().split() for _ in range(int(N))], int).min(1).max())

11 MEAN, VAR AND STD
import numpy
N,M = map(int,input().split())
x = []
for i in range(N):
    y = list(map(int,input().split()))
    x.append(y)

x= numpy.array(x)
numpy.set_printoptions(legacy='1.13')
print (numpy.mean(x, axis = 1))
print (numpy.var(x, axis = 0))
print (numpy.std(x))















12 DOT AND CROSS
import numpy

N = int(input())
A = numpy.array([input().split() for _ in range(N)], int)
B = numpy.array([input().split() for _ in range(N)], int)
print(numpy.dot(A, B))

13 INNER AND OUTER
import numpy
A = numpy.array(input().split(), int)
B = numpy.array(input().split(), int)
print(numpy.inner(A,B), numpy.outer(A,B), sep='\n')

14 POLYNOMIALS
import numpy
P = [float(x) for x in input().split()]
x = float(input())
print(numpy.polyval(P, x))

15 LINEAR ALGEBRA
import numpy
print(round(numpy.linalg.det(numpy.array([list(map(float,input().split())) for _ in range(int(input()))])),2))
