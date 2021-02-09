"""
Operators
    Arithmetic ( +, -, *, /, %, **, // )
    Comparison ( ==, !=, <, >, <=, >= )
    Assignment ( =, +=, -=, *=, /=, %=, **=, //= )
    Logical ( and, or, not )
    Membership ( in, not in )
    Identity ( is, is not)

Conditional/Control Statement
    if
    if-else
    if-elif-else
    nested if-else

Assignment:
    1) find maximum number from 3 variables and also handle same values
    2) find minimum number from 3 variables and also handle same values
"""

no_1 = 10
no_2 = 40
no_3 = 40
#
# print(F'no_1: {no_1}')
# print('no_2: {}'.format(no_2))
# print('no_3: ', no_3)
# print('Addition: ', no_1 + no_2 + no_3)
# print('Subtraction: ', no_1 - no_3)
# print('Multiplication: ', no_1 * no_2)
# print('Division: ', no_1/ no_2)
# print('Modulus: ', no_1 % no_2)
# print('Power: ', no_1 ** no_2)
# print('//: ', no_1//no_2)
#
# print(no_1 == no_2)
# print(no_1 != no_2)
# print(no_1 < no_2)
# print(no_1 > no_2)
# print(no_1 <= no_2)
# print(no_1 >= no_2)

# print(no_1)
# no_1 **= 4  # no_1 = no_1 + 2
# print(no_1)

# print(no_1 == no_2 and no_2 < no_3)
# print(no_1 == no_2 or no_2 > no_3)
# print(not no_1 == no_2)

# x = [1, 2, 3, 4, 5, 6]
#
# print(6 in x)
# print(7 not in x)

# var_true = True
#
# print(no_1 is True, id(var_true), id(True))
# print(var_true == True, id(var_true), id(True))


"""
if (<condition> and
      <condition>  ):
    <statement_1>
    <statement_2>
    
<statement_3>
"""

# if no_1 == no_2:
#     print('No 1 and No 2 are equal')
#     print('No 1 and No 2 are equal')
#     print('No 1 and No 2 are equal')
#     print('No 1 and No 2 are equal')
#     print('No 1 and No 2 are equal')
#
# elif no_2 < no_3:
#     print("No 2 is greater then No 3")
#     print("No 2 is greater then No 3")
#     print("No 2 is greater then No 3")
#
# else:
#     print('No 1 and No 2 are not equal')
#     print('No 1 and No 2 are not equal')


# if (no_1 == no_2) {
# print('No 1 and No 2 are equal')
# print('No 1 and No 2 are equal')
# print('No 1 and No 2 are equal')
# print('No 1 and No 2 are equal')
# }

# var_str = input("Enter any fruit name: ")
# if var_str == 'apple':
#     print(F"I like {var_str}")
# elif var_str == 'orange':
#     print(F"I like {var_str}")
# else:
#     print(F"I don't like {var_str}")


if no_1 < no_2:
    if no_2 < no_3:
        print('No 3 is maximum')
    else:
        print('No 2 is maximum')
else:
    if no_1 < no_3:
        print('No 3 is maximum')
    else:
        print('No 1 is maximum')