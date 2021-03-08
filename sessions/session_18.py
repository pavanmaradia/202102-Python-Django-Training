"""
Built in functions
    String related Functions,
        upper, lower, title, capitalize, join, split
    Integer related Functions,
        abs, round, pow, div, divmod
    Data Structure related Functions
        min, max, count,len, zip, sorted
    Common Functions,
        sum, id, input, type, isinstance, print

Built in modules
    OS related modules,
        glob,os, sys, socket,shutil
    Mathematical modules,
        math, statistics
    Asynchronousprotocol modules,
        asyncio,asynchat,asyncore
    Security related modules,
        base64,binhex,hashlib
    Date time related modules,
        Calendar,datetime, time
    Common modules,
        argparse, collections, csv, multiprocessing, re, threading, uuid
"""

# x = "123hEllo world"
# print(x.upper())
# print(x.lower())
# print(x.title())
# print(x.capitalize())
# print('-'.join(['a', 'b', 'c']))
# print(x.split(" "))

# print(abs(-1.23))
# print(round(5/3, 3))
# print(pow(2, 5))
#
# mm, ss = divmod(86401, 60)
# hh, mm = divmod(mm, 60)
# print(F"{hh}:{mm}:{ss}")

# x = [1, 3, 5, 10, 3, 34, 40]
# print(min(x))
# print(max(x))
# print(x.count(3))
# print(len(x))
# x = ['key1', 'key2', 'key3', 'key4']
# y = ['value1', 'value2', 'value3']
# z = ['value4', 'value5', 'value6', 'value7']
#
# for _x, _y, _z in zip(x, y, z):
#     print(F"{_x}-{_y}-{_z}")
#
# print('----------------')
# for i in range(0, len(x)):
#     print(F"{x[i]}-{y[i]}-{z[i]}")

# x = 1
# print(type(x))
# print(isinstance(x, int))

# import glob
#
# print(glob.glob('/Users/pavanmaradia/Documents/educart/Python-Django/202102-Python-Django-Training/*/*.py'))

import sys

try:
    print(5/0)
except ZeroDivisionError as error:
    print(error)
    print(sys.exc_info())

import collections

task_1 = 0
task_2 = 1