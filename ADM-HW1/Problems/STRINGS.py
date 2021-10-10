1.SWAP CASE
def swap_case(s):
    return s.swapcase()

2.CAPITALIZE                -----------1/6 case failed
def solve(s):
    x= s.title()
    return x

3.STRING SPLIT AND JOIN
def split_and_join(line):
    # write your code here
    return "-".join(line.split())

4.WHATS YOUR NAME
def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(first_name, last_name))

5.MUTATIONS
def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]

6.FIND A STRING
def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]

7.STRING VALIDATORS
s = input()
print(any([char.isalnum() for char in s]))
print(any([char.isalpha() for char in s]))
print(any([char.isdigit() for char in s]))
print(any([char.islower() for char in s]))
print(any([char.isupper() for char in s]))

8.TEXT ALIGNMENT
# Replace all ______ with rjust, ljust or center.
thickness = int(input())  # This must be an odd number
c = 'H'

# Top Cone
for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# Top Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Middle Belt
for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))

# Bottom Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Bottom Cone
for i in range(thickness):
    print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(
        thickness * 6))

9.TEXT WRAP
def wrap(string, max_width):
    return textwrap.fill(string, max_width)

10.STRING FORMATTING
def print_formatted(number):
    width = len("{0:b}".format(number))
    for i in range(1, number + 1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))

11.DESIGNER DOOR MAT
height, lenght = map(int, input().split())
for i in range(0, height // 2):
    s = '.|.' * (i * 2 + 1)
    print(s.center(lenght, '-'))
print('WELCOME'.center(lenght, '-'))
for i in range(height // 2 - 1, -1, -1):
    s = '.|.' * (i * 2 + 1)
    print(s.center(lenght, '-'))

12.ALPHABET RANGOLI
def print_rangoli(size):
    import string
    L = 4 * size - 3
    alphabet = string.ascii_lowercase
    for i in list(range(size))[::-1] + list(range(1, size)):
        print('-'.join(alphabet[size - 1:i:-1] + alphabet[i:size]).center(L, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


13.MERGE THE TOOLS
 a = []
    len_a = 0
    for item in string:
        len_a +=1
        if item not in a:
            a.append(item)
        if len_a == k:
            print (''.join(a))
            a = []
            len_a = 0

14.MINION GAME
def minion_game(string):
    vow = 'AEIOU'
    str_lenght = len(string)
    k_score, s_score= 0,0

    for i in range(str_lenght):
        if s[i] in vow:
            k_score += (str_lenght - i)
        else:
            s_score += (str_lenght - i)
    if k_score > s_score:
        print("Kevin", k_score)
    elif k_score < s_score:
        print("Stuart", s_score)
    else:
        print("Draw")

