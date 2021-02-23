"""
Abstraction
Encapsulation -> public, protected, private
Inheritance -> single, multi-level, multiple
Polymorphism -> overloading and overriding -> operator and method
"""

# class Encap(object):
#
#     def __init__(self):
#         self.public = None
#         self._protected = None
#         self.__private = None


# e = Encap()
# e.public = 'Hi'
# print(e.public)
# print(e._protected)
# print(e.__private)


class BaseClass:
    my_var = "This is my string"

    def my_method(self):
        print("You are in Base Class")


class DerivedA(BaseClass):
    # def __init__(self):
        # self.my_method()
        # print(self.my_var)

    def derived_a_method(self):
        print("You called derived class method")


# class DerivedB(DerivedA):
#     var_derived_b = "test"
#
#     def main(self):
#         print(self.var_derived_b)
#         self.my_method()
#         self.derived_method()

class DerivedB(BaseClass):
    def derived_b_method(self):
        print("You are in derived b method")

class DerivedC(DerivedA, DerivedB):
    def main(self):
        self.derived_a_method()
        self.derived_b_method()

DerivedC().main()