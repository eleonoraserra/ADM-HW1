1 LIST COMPREHENSION
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

ans = [[i,j,k]
for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k != n]
print(ans)

2 FIND THE RUNNER-UP SCORE
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(set(list(arr)))
    ar = len(arr)
    arr = sorted(arr)
    print(arr[ar-2])

3 NESTED LIST
ms = []
ss = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        ms +=[[name,score]]
        ss +=[score]
    x=sorted(set(ss))[1]

    for n,s in sorted(ms):
        if s == x:
            print(n)

4 FINDING THE PERCENTAGE
marks={}
for _ in range(int(input())):
    line = input().split()
    marks[line[0]]=list(map(float,line[1:]))
print('%.2f'% (sum(marks[input()])/3))

5 LISTS
if __name__ == '__main__':
    N = int(input())
    result=[]
    for n in range(N):
        x=input().split(" ")
        command =x[0]
        if command == 'append':
            result.append(int(x[1]))
        if command == 'print':
            print(result)
        if command == 'insert':
            result.insert(int(x[1]), int(x[2]))
        if command == 'reverse':
            result.reverse()
        if command == 'pop':
            result.pop()
        if command == 'sort':
            result = sorted(result)
        if command == 'remove':
            result.remove(int(x[1]))
6 TUPLES
n = int(input())
print(hash(tuple(map(int,input().split()))))
