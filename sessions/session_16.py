"""
Decorators
    - Function as parameters
    - Nested Function
    - Return function as function return (Closer Function)
    - Decorator syntax
"""

import time
from datetime import datetime

# def div(no_1, no_2):
#     return no_1/no_2
#
# def smartdiv(no_1, no_2):
#     if no_1 < no_2:
#         no_1, no_2 = no_2, no_1
#     return no_1/no_2
#
# print(div(4,2))
# print(div(2,4))
#
# print(smartdiv(4,2))
# print(smartdiv(2,4))
#
# def hi_greetings(name):
#     return F"Hi {name}"
#
#
# def bye_greetings(name):
#     return F"Bye {name}"

# hi = hi_greetings
# bye = bye_greetings
#
# print(hi(name='Dhruv'))
# print(hi(name="Mahesh"))

# def display(func, name):
#     print(func(name))

# display(func=bye_greetings, name='Dhruv')


# def display(name):
#
#     def hello_greetings():
#         print(F"Hello {name}")
#
#     def bye_greetings():
#         print(F"Bye {name}")
#
#     print("Welcome to display function")
#     hello_greetings()
#     print("You are in process")
#     bye_greetings()
#
#
# display(name='Mahesh')


# def display(greet):
#     if greet.lower() == 'hi':
#         return hi_greetings
#     elif greet.lower() == 'bye_':
#         return bye_greetings
#
# func = display(greet='bye_')
# print(func)
# print(func(name='Dhruv'))
# print(func(name='Mahesh'))


# def p_tag_decorator(func):
#     def inner_function():
#         resp = func()
#         return F"<p>{resp}</p>"
#     return inner_function
#
#
# def div_tag_decorator(func):
#     def inner_function():
#         resp = func()
#         return F"<div>{resp}</div>"
#     return inner_function
#
#
# @div_tag_decorator
# @p_tag_decorator
# def hello_world():
#     return "Hello World"
#
#
# @p_tag_decorator
# def bye_world():
#     return "Bye World"


# hello_world = p_tag_decorator(hello_world)
# print(hello_world())
#
# bye_world = p_tag_decorator(bye_world)
# print(bye_world())

# print(hello_world())
# print(bye_world())

# def smart_div(func):
#     def wrapper_function(no_1, no_2):
#         if no_1 < no_2:
#             no_1, no_2 = no_2, no_1
#         resp = func(no_1, no_2)
#         resp = f"{no_1}/{no_2} = {resp}"
#         return resp
#     return wrapper_function
#
# _div =smart_div(div)
#
# print(_div(4,2))
# print(_div(2, 4 ))

def performance_decorator(func):
    def inner_function(*args):
        start_time = datetime.now()
        print(F"Function ({func.__name__}) execution started with {args}")
        response = func(*args)
        print(F"Function ({func.__name__}) execution is completed and "
              F"response is {response}")
        end_time = datetime.now()
        print(F'Function ({func.__name__}) took {end_time - start_time}s')
        return response

    return inner_function


@performance_decorator
def div(*args):
    time.sleep(1)
    return args[0]/ args[1]


@performance_decorator
def multiply(*args):
    time.sleep(2)
    total = 1
    for arg in args:
        total *= arg

    return total


@performance_decorator
def addition(*args):
    time.sleep(3)
    return sum(args)


div(10, 2)
print("=========================")
multiply(3,5,7,89,97,44,332,23,2,3)
print("=========================")
addition(3,5,7,89,97,44,332,23,2,3)


