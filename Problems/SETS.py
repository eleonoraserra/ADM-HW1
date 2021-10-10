1 INTRODUCTION TO SETS
def average(array):
    # your code goes here
    distance = set(array)
    return sum (distance)/len(distance)

2 NO IDEA
_ = input()
arr = input().split()
like = set(input().split())
dislike = set(input().split())
print(sum((i in like) - (i in dislike) for i in arr))

3 SYMM DIFFERENCE
m= input()
a= set(map(int,input().split()))
n=input()
b= set(map(int,input().split()))

print(*sorted(a.symmetric_difference(b)), sep='\n')

4 SET ADD
set1 = set()
for _ in range(int(input())):
    set1.add(input())

print (len(set1))

5 SET DISCARD...
n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    x = input().split()
    if len(x) == 1:
        s.pop()
    elif x[0] == 'remove' :
        try:
            s.remove(int(x[1]))
        except:
            next
    elif x[0] == 'discard' :
        s.discard(int(x[1]))

print (sum(s))

6 SET UNION
n, set_n, b, set_b = int(input()), set(input().split()), int(input()), set(input().split())
print (len(set_n.union(set_b)))

7 SET INTERSECTION
m, set_m, n, set_n = int(input()), set(input().split()), int(input()), set(input().split())
print (len(set_m.intersection(set_n)))

8 SET DIFFERENCE
m, set_m, n, set_n = int(input()), set(input().split()), int(input()), set(input().split())
print (len(set_m.difference(set_n)))

9 SET SYMM DIFFERENCE
_,a = input(), set(input().split())
_,b = input(), set(input().split())
print(len(a.symmetric_difference(b)))

10 SET MUTATIONS
def handler(a):
    command = input().split()[0]
    new_set = set(map(int,input().split()))
    if command == 'intersection_update':
        a.intersection_update(new_set)
    if command == 'update':
        a.update(new_set)
    if command == 'symmetric_difference_update':
        a.symmetric_difference_update(new_set)
    if command == 'difference_update':
        a.difference_update(new_set)

_,a = input(), set(map(int, input().split()))
for i in range(int(input())):
    handler(a)
print(sum(a))

11 THE CAPTAINS ROOM
k= int(input())
room_number_list = list(map(int,input().split()))
captain_room_number = (sum(set(room_number_list))*k- sum(room_number_list)) // (k-1)
print(captain_room_number)

12 CHECK SUBSET
for _ in range(int(input())):
    line1, line2 = int(input()), set(input().split())
    line3, line4 = int(input()), set(input().split())

    print (line2.issubset(line4))

13 CHECK STRICT SUPERSET
a= set(input().split())
print (all(a>set(input().split()) for _ in range(int(input()))))

