"""
Looping statements
    while
    for
    for else

Assignments:
    1. Print 1-10 using for loop
    2. Print 1-30 odd numbers
    3. Print table of 10
       10 x 01 = 10
       10 x 02 = 20
       10 x 03 = 30
    4. Print table of 17
"""

# list_1 = [] # list()
# list_2 = [] # list()
#
# list_3 = list_1
# if list_1 == list_2:
#     print("list_1 == list_2 : True")
#
# if list_1 is list_2:
#     print("list_1 is list_2 : True")
# else:
#     print("list_1 is list_2 : False", id(list_1), id(list_2))
#
# if list_3 == list_1:
#     print("list_3 == list_1 : True", id(list_1), id(list_3))
#
# if list_3 is list_1:
#     print("list_3 is list_1 : True", id(list_1), id(list_3))

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y = {'key_1': 'value_1', 'key_2': 'value_2', 'key_3':'value_3'}
"""
for <iter> in <iterable_object>:
    <for statement>
    <for statement>
    <for statement>
"""
# for(int a; a<10; a++) {}
# for a in x:
#     print(a, end=" ")

# print(list(y.items())[0])
# for key, value in y.items():
#     print(F'Key -> {key}: Value -> {value}')

"""
while <condition>:
    <while statement>
    <while statement>
"""
'''
Output :
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

i = 2
j = Error

print(1 * 5)
=====================
1 2 3 4 5
2 4 6 8 10
'''
# index = 11
# while index <= 10:
#     print(index)
#     index += 1


x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]

for i in x:
    print(i)
    # if i == 3:
    #     break
else:
    print('For loop is completed')

