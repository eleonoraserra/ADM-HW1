1 HEX COLOR CODE
import re
for _ in range(int(input())):
    matches = re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', input())
    if matches:
        print(*matches, sep='\n')

2 HTML PARSER PT.1
import re
N = int(input())
s = ""

for i in range(N):
    s += input()
s = re.sub(r"(?:<!--(.|\s)*?(?:-->))", "", s)
tags = re.compile(r"(?<=<)(?:.*?)(?=>)").findall(s)

for tag in tags:
    if tag[0] == "/":
        print("End   :", tag[1:])
    else:
        atts = re.compile(r"([\w-]+)(?:=[\"'](.*?)[\"'])?").findall(tag)
        if tag[-1] == "/":
            print("Empty :", atts[0][0])
        else:
            print("Start :", atts[0][0])

        for i in range(1, len(atts)):
            at = atts[i][0]
            if atts[i][1] == '':
                no = 'None'
            else:
                no = atts[i][1]
            print("-> {} > {}".format(at, no))

3 HTML PARSER pt.2
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def handle_comment(self, data):
        l = len(data.split('\n'))
        if l > 1:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        if data.strip():
            print(data)

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)

html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()

4 GROUP,GROUPS,GROUPDICT
import re
m = re.search(r'([a-zA-Z0-9])\1', input().strip())
print(m.group(1) if m else -1)

5 RE.SPLIT
regex_pattern = r"[.,]+"

6 RE.FINDALL AND RE.FINDITER
import re
vow = 'aeiou'
cons = 'qwrtypsdfghjklzxcvbnm'
match = re.findall(r'(?<=[' + cons + '])([' + vow + ']{2,})(?=[' + cons + '])', input(), flags=re.I)
print('\n'.join(match or ['-1']))

7 RE.START AND RE.END
import re

string = input()
substring = input()

layout = re.compile(substring)
m = layout.search(string)
if not m: print('(-1, -1)')
while m:
    print('({0}, {1})'.format(m.start(), m.end() - 1))
    m = layout.search(string, m.start() + 1)

8 REGEX SUBSTITUTION
import re
for _ in range(int(input())):
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', input()))

9 VAIDATING ROMAN NUMBERS
regex_pattern = r'M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[VX]|V?I{0,3})$'

10 VALIDATING PHONE NUMBERS
import re
[print('YES' if re.match(r'[789]\d{9}$', input()) else 'NO') for _ in range(int(input()))]

11 VALIDATING AND PARSING EMAIL ADDRESSES
import re
pattern = r'^<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>$'
for _ in range(int(input())):
    name, email = input().split(' ')
    if re.match(pattern, email):
        print(name, email)

12 VALIDATING UID
import re

for _ in range(int(input())):
    u = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', u)
        assert re.search(r'\d\d\d', u)
        assert not re.search(r'[^a-zA-Z0-9]', u)
        assert not re.search(r'(.)\1', u)
        assert len(u) == 10
    except:
        print('Invalid')
    else:
        print('Valid')

13 VALIDATING CREDIT CARD NUMBERS
import re

pattern = re.compile(
    r'^'
    r'(?!.*(\d)(-?\1){3})'
    r'[456]\d{3}'
    r'(?:-?\d{4}){3}'
    r'$')
for _ in range(int(input().strip())):
    print('Valid' if pattern.search(input().strip()) else 'Invalid')

14 VALIDATING POSTAL CODES
regex_integer_in_range = r'^[1-9][\d]{5}$'	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r'(\d)(?=\d\1)'	# Do not delete 'r'.
import re
P = input()
print (bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

15 MATRIX SCRIPT
import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    message = ""
for column in range(m):
    for row in range(n):
        message += matrix[row][column]
print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", message))

16 DETECT HTML TAGS
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print('-> {} > {}'.format(*attr)) for attr in attrs]

html = '\n'.join([input() for _ in range(int(input()))])
parser = MyHTMLParser()
parser.feed(html)
parser.close()

17 DETECT FLOATING NUMBER
from re import match, compile

pattern = compile('^[-+]?[0-9]*\.[0-9]+$')
for _ in range(int(input())):
    print(bool(pattern.match(input())))
