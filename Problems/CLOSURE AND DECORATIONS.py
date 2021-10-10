1 STANDARDIZE MOBILE NUMBER
def wrapper(f):
    def fun(l):
        f(['+91 ' + a[-10:-5] + ' ' + a[-5:] for a in l])
    return fun


2 DECORATORS 2
import operator
def person_lister(f):
    def inner(people):
        return map(f, sorted(people, key=lambda x: int(x[2])))
    return inner
