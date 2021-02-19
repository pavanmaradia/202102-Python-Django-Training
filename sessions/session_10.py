"""
Class
"""

'''
class <ClassName>(<BaseClass/es>):
    <class_variables>
    
    def __init__(self):  
        <statement>
    
    def method(self):
        <statement>
'''


# class MyFirstClass:
#     """ This is my first class and I am in demo"""
#
#     def main(self):
#         print("Hello from main method of class MyFirstClass.")
#
# _class = MyFirstClass()
# _class.main()

class MySecondClass:

    def __init__(self):
        # self.name = None
        print('You are in init method')

    def main(self, name):
        self.name = name
        print(F"name: {self.name}")
        print("Hello from main method of class MyFirstClass.")

    def __del__(self):
        print(F"Deleting {self.name}")


_class = MySecondClass()
_class.main(name="Dhruv")
_class.name ='Mahesh'
print(_class.name)
_class.main(name='Pavan')