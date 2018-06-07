from datetime import datetime
from decimal import Decimal
def hello(name):
    print(name)
a = 0xd
b = 1.0
c = 'a'
d = True
e = b'abc'
f = "日本語".encode('utf-8')
g = None
h = [1, 'a', ]
i = (1, 2, '3',)
j = {a: 1, b: 'a', }
k = hello
l = datetime(2014, 6, 9, 10, 30, 10)
m = Decimal('0.1')

print('type = {} \t a = {}'.format(type(a), a))
print('type = {} \t b = {}'.format(type(b), b))
print('type = {} \t c = {}'.format(type(c), c))
print('type = {} \t d = {}'.format(type(d), d))
print('type = {} \t e = {}'.format(type(e), e))
print('type = {} \t f = {}'.format(type(f), f))
print('type = {} \t g = {}'.format(type(g), g))
print('type = {} \t h = {}'.format(type(h), h))
print('type = {} \t i = {}'.format(type(i), i))
print('type = {} \t j = {}'.format(type(j), j))
print('type = {} \t k = {}'.format(type(k), k))
print('type = {} \t l = {}'.format(type(l), l))
print('type = {} \t m = {}'.format(type(m), m))
print(type(type(Decimal(0.1))))

print(0.1+0.1+0.1-0.3)
print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3'))
print(Decimal('0.1'))
print(Decimal(0.1))
print(0.1)

if True:
    if True:
        print(''''asdf
        asdf
asdfn
        a''')

