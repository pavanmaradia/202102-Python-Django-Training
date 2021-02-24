"""
super
Diamond Problem amd MRO
Polymorphism -> overloading and overriding -> operator and method
"""


# class A(object):
#     def __init__(self, test):
#         self.base_var = test
#
#     def display(self):
#         print(F"Base var: {self.base_var}")
#
#
# class B(A):
#
#     def __init__(self, test):
#         super().__init__(test)
#         self.derive_var = 'B class'
#
#     def display(self):
#         print(F"Base variable: {self.base_var}")
#         print(F"Derived variable : {self.derive_var}")
#
#
# b = B(test='This is test')
# b.display()


# class A:
#     def display(self):
#         print('Class A')
#
#
# class B(A):
#     def display(self):
#         print('Class B')
#
#
# class C(A):
#     def display(self):
#         print('Class C')
#
#
# class D(B, C):
#
#     def __init__(self):
#         self.__class__.__bases__ = (C, B)
#         self.display()
#         self.__class__.__bases__ = (B, C)
#         self.display()
#     def display(self):
#         print('Class D')
# D()

# def test(no_1, no_2):
#     return no_1 + no_2
#
# def test(no_1, no_2, no_3):
#     return no_1 + no_2 + no_3


# def test(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total
#
# resp = test(1, 2, 3, 4)
#
# print(resp)

# def addition(var_1, var_2):
#     return var_1 + var_2
#
# resp = addition([1, 2], [3,4])
# print(resp)


# class Employee(object):
#     training_batch = "202002"
#
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = F"{self.first_name.lower()}.{self.last_name.lower()}@google.com"
#
#     def full_name(self):
#         return F"{self.first_name} {self.last_name}"
#
#
# f_name = input('Enter First Name: ')
# l_name = input('Enter Last Name: ')
#
# e = Employee(first_name=f_name, last_name=l_name)
# Employee.training_batch = "2020 Feb"
# e.training_batch = "2020 Feb"
# e2 = Employee(first_name="Dhruv", last_name="Sharma")
# print(e.full_name())
# print(e.training_batch)
# print(e.email)
#
# print(e2.full_name())
# print(e2.training_batch)
# print(e2.email)


