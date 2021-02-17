"""
Break Statement
Continue Statement
comprehension

"""

# x = [1, 3, 5, 7]
#
# x = []
# for i in range(1, 8):
#     if i % 2 == 1:
#         x.append(i)
#
# print(x)

# x = [2**i for i in range(1, 8) if i % 2 == 1]
# print(x)
#
# y = {i: 2**i for i in range(1, 8) if i % 2 == 1}
# print(y)
'''
01 02 03 04 05
06 07 08 09 10
'''

# print('{:05}'.format(5))

# number = 1
# for i in range(0, 5):
#     for j in range(0, 5):
#         print('{:02}'.format(number), end=" ")
#         number += 1
#     print("")

# x = [2, 34, 3, 10, 11, 5, 20]
# for i in x:
#     if i == 10:
#         print("We found 10 at", x.index(i)+1, 'th position')
#         print(F"We found 10 at {x.index(i)+1}th position')
#         break
#     print(F"number is not 10: {i}")

# for i in x:
#     # print('-----')
#     if i % 2 == 1:
#         # print(F'Number is odd {i}')
#         continue
#     print(i)
#     # print(' 12324 ')

for i in range(1, 7):
    for j in range(1, i+1):
        print(2**j, end=" ")
    print("")
