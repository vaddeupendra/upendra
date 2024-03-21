'''
# ? Eg:1
# ! method riding
# * ploymorphism in classes

class bank:
    def ratio(self):
        print("all banks has repo rate")
          
class SBI(bank):
    def ratio(self):
        print("SHI rate is 9%")

class IOB(bank):
    def ratio(self):
        print("IOB rate is 7.5%")

i = IOB()
I.ratio()

s = SBI()
s.ratio()
''
# ? eg: 2
class usa:
    def langauge(self):
        print("english")

    def capital(self):
        print("washington dc")

class india(usa):
    def langauge(self):
        print("none")

    def capital(self):
        print("new delhi")


i = india()
i.langauge()
i.capital()

''

# ? Eg:1
# ! method riding
# * ploymorphism in classes

class bank:
    def ratio(self):
        print("all banks has repo rate")
          
class SBI(bank):
    def ratio(self):
        print("SHI rate is 9%")

class IOB(bank):
    def ratio(self):
        print("IOB rate is 7.5%")

i = IOB()
I.ratio()

s = SBI()
s.ratio()
''
# ? eg:3

polymorphism using objects

''
c1,c2 ---> = print(c1), print(c2)
f1,f2

''
class c1:
    def f1(self):
        print("class 1")

class c2(c1):
    def f1(self):
        super().f1()
        print("class 2")

obj1 = c2()
obj1.f1()

obj2 = c1()
obj2.f1()

''

# ? eg:4

class c1:
    def f1(self):
        print("class 1")

class c2(c1):
    def f1(self):
        print("class 2")

obj1 = c2()
obj2 = c1()


def display(a):
    a.fa()
display(obj1)
display(obj2)

''
# *  changing the funtionality of builtin funtions

a = 9
b = 6
print(a+b)
print(a.__add__(b)) #? dunder method or 
''
class shoopping:
    def __item_list(self,l1):
        self.items =(l1)
        
    def __len__(self):
        length = len(self.items)
        return length
s = shooping([1,2,3,4,5])
print(len(s))
''
# ! ---> method overloading
# ! eg:1
class suming:
    def add(self,a,b):
        print(a+b)

    def add(self,a,b,c):
        print(a+b+c)

s = suming()
s.add(4,3) # ! ------> error
s.add(4,5,1)

'''

# ! eg:2
class summing:
    def add(self, a=none, b=none, c=none):
        if a!=none and b!=none and c!=n0ne:
            print(a+b+c)
        elif a!=none and b!=none:
             print(a+b)
        else:
             print(a)
obj = summing()
obj.add(2)
obj.add(3,4)
obj.add(1,2,3)

















