"""
Unnamed Parameter
pass function as parameter
return function from function
"""

'''
*args = list arguments 
**kwargs = dictionary arguments
'''


# def greetings(*param):
#     if param and len(param) == 2:
#         print(F"{param[0]} {param[1]}")
#     elif param:
#         print(F"Hello {param[0]}")
#     else:
#         print("Hello World")

# params = ["Hello", "Pavan"]
#
# greetings(*params)

#
# def greetings(**kwargs):
#     if kwargs:
#         print(F"{kwargs.get('greet', 'Hello')} {kwargs.get('name', 'World')}")
#     else:
#         print("Hello World...!!!!")
#
# greetings(**{ 'greet': 'Hi'})


# def hello_greetings():
#     return "Hello World"
#
#
# def bye_greetings():
#     return "Bye World"
#
#
# def logger_function(func):
#     print('logger function call')
#     response = func()
#     print(response)
#     print('Function called successfully.')
#
# logger_function(hello_greetings)
# logger_function(bye_greetings)


def greetings():
    return "Hello world"

def function(func):

    return func

greet_func = function(greetings)

resp = greet_func()
print(resp)