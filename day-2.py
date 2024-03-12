# a,b =78
# print(a,b)
# a,b,c = 9,4,6,7
# print(a,b,c)
102
103 # a, b, c = 9 8, 7, 8
104 # pri (variable) c: tuple[Literal[7], Literal[8]]
105
106 a, b = c = 7
107 print(a)
108 print(b)
109 print(c)
115 a = 7
116 b = 5
117
118 # Eg:1
119 # temp=a #temp=7
120 # a=b \# a = 5
121 # b=temp \# b = 7
122
123 # # a = 5 b = 7
124 # print(a, b)
125 
129 # a=a-b #a=12-5=7
130
131 # print(a, b)
132
133 # a, b=b, a # only in python
134 # print(a, b)
135
136 a=a*b
137 b=a/b
138 a=a/b
139 print(a, b)

34 # print(a, b)
35
36 # a=a*b \# a = 35
37 # b=a/b \# b = 35/7 = 5
38 # a=a/b \# a = 35/5 = 7
39 # print(int(a), int(b))
40
41 # id() --> used to find the memory address of the variable
42 a = 7
43 b = 8
44 print(id(a))
45 print(id(b))


146
147 # ----> Keywords
148 # Keywords are reserved words which provides special meaning to
149 # compiler or interpretor
150
151 import keyword
152
print(keyword.kwlist)
153
154
155import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
print(type (keyword.kwlist))

#!----> literals
# Literal is the constant value asssigned to a variable
# A variable is considers to be constant when it is defines
# in caps
# a= 78 # a is variable
# A=78 # A is constant




# hash() --> it creates a hash value for constant datatypes and
72 # provides error for non constant datatypes
73 n1 89+7j
74 print(hash(n1))
75
76 f1 [7, 8, 9]
77 print(hash(f1)) # error --> list ids non constant or mutable datatype
# n * (1 = 89 + 7j)
# print(hash(n1))
# f * 1 = [7, 8, 9]
# print(hash(f1)) # error --> list is non-constant or mutable datatype
# a = 9
b = 9
# b = 90
# print(id(a))
# print(id(b))
185 #!----> Operators

186 # ? Opeartors are symbols which is used to perfeorm various opearions
187 #? bewtween 2 or more operands
188
189 # Arithmatic
190 # Assignment
191 # Logical 1
192 # Relational or comparison
# Bitwise
194 # Identity
195 # Membership
196
197
# Arithmatic
198

# todo - Arithmatic ->+,-,*,/,%, //, **
98 # Eg:1
99
#a= 8
00 # b = 6
01 # c = 9
02 #print(a+b+c)
03
04 # input() --> used to get the runtime input
05 n1 = input("Enter the value: ")
  print(n1)



