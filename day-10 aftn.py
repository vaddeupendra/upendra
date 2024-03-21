'''
# ! ---------->
# the process of hiding the implimentation details is abstraction

# ? eg:1
from abc import ABC,abstraction
class shapes(ABC):
    def sides(self):
        print('all shapes have sides except circle')

class triangle:
    def triangle_sides(self):
        print("3 sides")

class square:
    def square(self):
        print("4 sides")

tr = triangle()
tr.triangle_slides()
tr.name()

''
def decor(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner()

@decor
def greet():
    return 'good morning'
print(greet)


#Rules to define abstract class1
#1.) Abstract class cannot be instantiated
#2.) from abc import ABC, abstractmethod
#3.) subclass the normal class with ABC
#4.) convert the normal method inside the abstract class to abstract method
#5.) all the child classes have to be subclassed with abstract class
#6.) The abstract method should be present in the
#child classes

''

class login(password):
    def validate(self,name,password):
        if super().pwd() == password:
            print("welcome",name, '!!')
            print("login successfull")
        else:
            print("please check the password")

login = login()
name = input("enter the name:")
pwd = input("enter the password: ")
login.validate(name,pwd)

''
# ! encapsulation
# * -----> eg:1
class car:
    __name = "bmw" # private variable
    print(__name)
    
c1 = car()
print(c1.name) # error
c1.name = "audi"
print(c1.name) # error

''
# * -----> eg:2
# ? accessing private date outside the class
class c1:
    __phone = '7698456237'

    def display(self):
        print(self.__phone)
c = c1()
c.display()
''

# * ------> eg:3
# ? declare private method
class class1:
    def m1(self):# private method
        print("iam private method")
        
    def __init__(self):
        self.__m1()
c = class1()
c.__m1() # errror

''
# ? nested class
class class1:
    class class2:
        name = "sidhu"

        def display(self):
            print(self.name)
    obj = class2()

obj = class1()
obj.obj1.display()


'''
# ? -----> tasks

# Write the code for the below tasks using function
#1.) d1 {"shirt": 1000, "pant": 1500, "Shoes": "900", "handkey": 30}

d1 = {"shirt": 1000, "pant": 1500, "Shoes": 900, "handkey": 30}
for val in d1:
    if d1 [val] == min(d1.values()):
        print(val)
for val in d1:
    if d1 [val] == max(d1.values()):
        print(val)
for val in d1:
    if val.startswith('s') or val.startswith('S'):
        print(val)








        

