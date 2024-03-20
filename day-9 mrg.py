'''
# ? Eg:1
# 0,1,1,2,3,5,8
n1 =0
n2 =1
ans =0+1 ==>1

n1 = 1
n2 = 1
ans = 1+1 ==> 2

n1 = 1
n2 = 2
ans = 1+2 ===>3

n1 = 2
n2 = 3
ans = 2+3 = 5

# ! find the 8th fibanochi number
num : 8
n1 = 0
n2 = 1

for val in range(num):
ans = n1+n2
n1 = n2
n2 = ans
print(ans)


''

# ? Eg:2
s1 = "hello how are you"
s2 = "hello how is"

s1 = s1.split(" ")
s2 = s2.split(" ")

for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)

''

# ? Eg:1
# 0,1,1,2,3,5,8
n1 =0
n2 =1
ans = 0+1 ===> 1

n1 = 1
n2 = 1
ans = 1+1 ==> 2

n1 = 1
n2 = 2
ans = 1+2 ===>3

n1 = 2
n2 = 3
ans = 2+3 = 5

# ! find the 8th fibanochi number
num : 8
n1 = 0
n2 = 1

for val in range(num):
ans = n1+n2
n1 = n2
n2 = ans
print(ans)
''

# ! constructors
# ? Eg:3
# * unparametarised constructer
class profile:
    def __init__(sel):
        print("hello world")

obj = profile()
obj. __init__()
''
# ? Eg: 4
# * parametarised constructor
class profile:
    def __init__(self,id,name,age):
        print(id,name,age)

obj = profile(1,"sid", 29)

''

# ? Eg:5
class c1:
    name = "sid"
    place = "abc"

    def m1(self):
        print(self.name,self.place)

object =c1()
object.m1()
''
# ? eg:5
class c1:
    email = "sid@gmail.com"

#    def m1(self):
        name = "sid"
        place("cbe")
print(name,place)
print(self.email)

# object = c1()
# object.m1()

''
# ? Eg:6
class c1:
    def ml(self):
        name = "sid"
        age = 28
        return name, age
    def display(self):
        # ! print(name, age)
        # ! print(self.name, self.age)
        print(self.m1())
        
''
# ? eg:7
# ? to use the variable inside the constructor in another methods
class class1:
    # email = "sid@gmail.com"     # static variable
    def __init__(self):
        self.name = "sid"        # instance variable
        self.email = "sid@gmail.com"
        # return name,email # error ----> cannot use return with constructor

    def display(self):
        print(self.name,self.email)


c1 = class1()
c1.display()

''

# ! ---------> inheritance
# the process of utilising the methods and attributes of parent class
# throught the object of child class it is called as inheritance

# ? 5 types of inheritance
# single inheritance
# multilevel inheritance
# multiple inheritance
# hybrid inheritance
# heirarichal inheritance
''
# * single inheritance
# ? it has only one parent class and only ane child class
# ! eg:1
class parent:
    def m1(self):
        print("iam parent class")

parent.m1()

class child:
    def m2(self):
        print("iam child class")
''
# ? eg: 2
class parent(child):
    def m1(self):
        print("iam parent class")

class child(parent):
    def m2(self):
        print("iam child class")

p = parent()
p.m2()


obj = child()
obj.m1()
        
 '''
# ? Eg:3
class c1:
    def __init__(self):
        print("iam constructor from parent class")

# class child1(c1):
#     pass

# obj = child()














        
