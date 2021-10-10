1 COLL.COUNTER
from collections import Counter

n = int(input())
s = Counter(map(int, input().split()))
x = int(input())
total = []
for i in range(x):
    a, b = map(int, input().split())
    if s[a] > 0:
        total.append(b)
        s.subtract(Counter([a]))
    else:
        pass
print(sum(total))

2 DEF.DICT TUTORIAL
from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(lambda: -1)
for i in range(1, n + 1):
    word = input()
    d[word] = d[word] + ' ' + str(i) if word in d else str(i)
for _ in range(m):
    print(d[input()])

3 COLL.NAMEDTUPLE
from collections import namedtuple

n = int(input())
a = input()
totale = 0
Student = namedtuple('Student', a)
for _ in range(n):
    student = Student(*input().split())
    totale += int(student.MARKS)
print('{:.2f}'.format(totale / n))

4 COLL.ORDER DICT
from collections import OrderedDict

d = OrderedDict()
for _ in range(int(input())):
    item, space, quantity = input().rpartition(' ')
    d[item] = d.get(item, 0) + int(quantity)
for item, quantity in d.items():
    print(item, quantity)

5 COLL.DEQUE
from collections import deque

d = deque()
for _ in range(int(input())):
    eval('d.{0}({1})'.format(*input().split(), ''))
print(*d)

6 COMPANY LOGO
import collections

s = sorted(input().strip())
s_counter = collections.Counter(s).most_common()

s_counter = sorted(s_counter, key=lambda x: (x[1] * -1, x[0]))
for i in range(0, 3):
    print(s_counter[i][0], s_counter[i][1])

7 PILING UP
for t in range(int(input())):
    l = int(input())
    sides = list(map(int, input().split()))
    i = 0
    while i < l - 1 and sides[i] >= sides[i + 1]:
        i += 1
    while i < l - 1 and sides[i] <= sides[i + 1]:
        i += 1
    print('Yes' if i == l - 1 else 'No')

8 WORD ORDER
from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    distinct_words_and_count = OrderedDict()

    for _ in range(n):
        word = input()

        if word in distinct_words_and_count:
            # keep count of words
            distinct_words_and_count[word] += 1
            continue

        distinct_words_and_count[word] = 1

    print(str(len(distinct_words_and_count)) + '\n' +
          ' '.join(list(map(str, distinct_words_and_count.values()))))
