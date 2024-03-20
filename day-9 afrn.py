'''
# ! eg:3
class parent:
    name = "sidhu"
    
class child(parent):
        name = "name1"

        def display(self):
            print(self.name)


d= child()
d.display()
''
# ! multilevel inheritance
# ? eg:1
class voice:
    def sound(self):
        print("all the animals have their own voices")

class dog(voice):
    def dog_voice(self):
        print("bark")

class cat(dog):
     def cat_voice(self):
         print("meow")

class parrot(cat):
    def parrot_voice(self):
        print("speak")


all = parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()

''

# ? eg:2
class honda_city:
    def engine_specs(self,cc,hp,torque,fuel_type,num_of_)

#? Eg:2
class honda_city:
    def honda_city_engine_specs (self, cc, Hp, torque, fuel_type, num_of_piston):
        print(cc, Hp, torque, fuel_type, num_of_piston)
    def honda_city_body_specs (self, color, weight, height, length, vehicle_type):
        print(color, weight, height, length, vehicle_type)
        
class amaze(honda_city def amaze_engine_s (parameter) torque: Any ,fuel_type, num_of_piston):
    def amaze_body_specs(self, color, weight, height, length, vehicle_type):
        print(cc, Hp, torque, fuel_type, num_of_piston)
    
class civic(amaze):
    def civic_engine_specs (self, cc, Hp, torque, fuel_type, num_of_piston):
        print(cc, Hp, torque, fuel_type, num_of_piston)

class honda(civic):
    pass
    def civic_body_specs(self, color, weight, height, length, vehicle_type): print(color, weight, height, length, vehicle_type)

honda = Honda()
honda.honda_city_engine_specs (1500, 230, 2979, "petrol", 4)
honda.civic body specs("white", 2000, 5.5, 8, "Hatchback")

''
# ! multiple inheritance
# ? it has multiple parent and 1 child

class while_petrol:
    def function_w(self):
        print("used to airplans")

        

class organic_petrol:
    def function_o(self):
        print("used for bike,cars")

        
class premium_petrol:
    def function_p(self):
        print("sports cars,bikes")

        

class petrol(while_petrol,organic_petrol,premium_petrol):
    def destination(self):
        print("petrols types")


p= petrol()
p.defanition()
p.function_o()

''
# ! eg:2
class addition:
    def add(self,a,b):
        print(a+b)
        
    def mul(self,a,b)
    print(a%b)

        
class subtraction:
    def sub(self,a,b):
        print(a-b)

class multiply:
    def mul(self,a,b):
        print(a*b)

        
class division(addition,subtraction,multiply):
    def div(self,a,b):
        print(a/b)

calc = division()
calc.add(3,4)
calc.mul(4,2)

''

# ! heirarical inheritance

class catagory:
    def weight(self, weight):
        print(weight)

    def display(self,colour,taste):
        print(colour,taste)
        
class Tomato(catagory):
    def tomato_specs(self):
        color="black"
        Taste = "neutral taste"
        self.display(colour,taste)
        
class carrot(catagory):
    def carrot_specs(self):
        color="green"
        taste = "sweet"
        self.display(colour,taste)

c = carrot()
c.carrot_specs()
c.weight("30gms")


t= tomato()
t.tomato_specs()
t.weight("20gms")

''

# ! hybrid inheritance
# ? the combination of above 4 inheritance is called hybrid inheritance
class c1:
    def ma(self):
        print("class1")

class c2(c1):
    def m2(self):
        print("class2")

class c3(c2):
    def m3(self):
        print("class4")

class c4(c3):
    def m4(self):
        print("iam m3 from c4")

class c5(c4):
    def m5(self):
        print("class4")


class c6(c5,c3):
    def m6(self):
        print("class4")

obj = c6()
obj.m3()



''

# ! --------------------------> ploymorphism
# poly - many, morph -----> form
# a funtion which has the ability to perform more than 1 functionality
# then it is considered to be as ploimorphism


# * ploymorphism in builtin funtions
# len()  --------> which is used to find the length of list, tuple,dict etc...
# index()
# max()
# min()
# count()
# pop()
# and more().........
''
# * ploymorphism in operations
# +
print(9+9)
print("k"+'1')
print([1,2,3]+[5,6])
'''
# *
print(6*7)
l1 = {19,28,3,4}
print(*l1)
# def f1(*args)
l1 = [1,2,3,4]
print(l1*10)





















     
