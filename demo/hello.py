#!/usr/bin/env python3

name = input("Please input your name:")
print(r"Hello, \n", name)
print('''Wow,
long time no see''')
s1 = 'today is %s, I got %d ￥.' % ("Wednesday", 1000)
print(s1)


def my_abs(x):
    if x >= 0:
        return x
    if x < 0:
        return -x


print(my_abs(-19))


def find_min_max(data):
    for i, value in enumerate(data):
        print('-- ', value, ' ++ ', i)


L = [1, 2, 22, 0]
find_min_max(L)