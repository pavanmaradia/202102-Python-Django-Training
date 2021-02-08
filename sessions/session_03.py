"""
Data Structure:
    List
    Tuple
    Dictionary
    Set
    Array

Assignment:
    1. Create a list of dictionary with following details
        name, birthdate, age, location
        at least 10 list elements
    2. do the intersection of two sets
    3. do the union for 10 sets
    4. find the different from two sets

Monday: Operators, conditional statements, looping statements
"""
VAR_LIST = [1, 3, 4, 2, 1, 1, 1, 2, 1]  # [] # list()

var_int = 2

"""
VAR_LIST.append(var_int)
print(VAR_LIST)
VAR_LIST.sort()
print(VAR_LIST)
# VAR_LIST.pop(1)
# print(VAR_LIST)
# print(VAR_LIST.count(1))

# VAR_LIST.clear()
VAR_LIST.extend(['a', 'b', [1, 2, 3]])
print(VAR_LIST)



print(VAR_TUPLE)


VAR_TUPLE = (1, 4, 6, 'string')

VAR_DICT = {
    'key1': 1,
    'key2': 2
} # dict()

VAR_DICT['key3'] = VAR_LIST
VAR_DICT[VAR_TUPLE] = 'test'
print(VAR_DICT)

# print(VAR_DICT.get('key4', 'key4 is not present in your dictionary'))

VAR_DICT.pop('key3', None)
print(VAR_DICT)
VAR_DICT.update({
    'key5': 'value4',
    'key6': [1, 24]
})

print(VAR_DICT)


VAR_SET_1 = {1, 2, 3, 1, 1, 1, 1, 1} # set()
VAR_SET_2 = {1, 4, 5, 6}

print(VAR_SET_2.intersection(VAR_SET_1))
"""

from array import array

a = array('f', [1.2, 2.3, 3.14])
print(a)
