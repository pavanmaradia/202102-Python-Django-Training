"""
Create class Property
Override default class methods
Iterators
"""


# class Employee(object):
#
#     def __init__(self, **kwargs):
#         self.first_name = kwargs.get('first_name', "")
#         self.last_name = kwargs.get('last_name', "")
#         self.skill_sets = kwargs.get('skills')
#
#     @property
#     def email(self):
#         return F"{self.first_name.lower()}.{self.last_name.lower()}@google.com"
#
#     @property
#     def full_name(self):
#         return F"{self.first_name.lower()}.{self.last_name.lower()}"
#
#     def __add__(self, other):
#         skills = []
#         if self.skill_sets:
#             skills.extend(self.skill_sets)
#         if other.skill_sets:
#             skills.extend(other.skill_sets)
#
#         return list(set(skills))
#
#
# payload_1 = {
#     'first_name': 'Dhruv',
#     'last_name': 'Sharma',
#     'skills': ['Manage People', 'Manage Project', 'Manage Budget', 'Manage Scope']
# }
# e1 = Employee(**payload_1)
# print(e1.email)
#
# payload_2 = {
#     'first_name': 'Mahesh',
#     'last_name': 'Trlu',
#     'skills': ['Client Communication', 'Demo', 'Coding', 'Manage Customer']
# }
# e2 = Employee(**payload_2)
# print(e2.email)

# print(e1 + e2)


# for i in range(1, 10):
#     print(i)

# x = [1, 2, 3, 4, 5]
# y = iter(x)
#
# print(y.__next__())
# print(y.__next__())
# print(y.__next__())

# class MyRange:
#
#     def __init__(self, *args):
#         if len(args) == 3:
#             self.start = args[0]
#             self.end = args[1]
#             self.step = args[2]
#         elif len(args) == 2:
#             self.start = args[0]
#             self.end = args[1]
#             self.step = 1
#         elif len(args) == 1:
#             self.start = 0
#             self.end = args[0]
#             self.step = 1
#         else:
#             raise KeyError
#
#     def __iter__(self):
#         if self.step > 0:
#             self.start -= 1
#         elif self.step < 0:
#             self.start += 1
#         return self
#
#     def __next__(self):
#         if self.start < self.end and self.step > 0:
#             self.start += self.step
#             return self.start
#         elif self.start > self.end and self.step < 0:
#             self.start += self.step
#             return self.start
#         else:
#             raise StopIteration
#
#
# for i in MyRange(1):
#     print(i)
#
# print('---------')
# for i in range(1):
#     print(i)