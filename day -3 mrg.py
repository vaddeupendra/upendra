# ! Eg:3
# ? Take values of length and breadth of a
# ? from user and check if it is square or not.
# lenth = int(input())
# length = int(input())
# if length==breadth:
#      print("its a square")
# else:
#     print("its not square")
 
# ! Eg:4
# ? Accept the age of 4 people and display the oldest one.
#1 Eg:4
Python program to check whether the I given integer is a multiple of both 5 and 7

 n = int(input("enter the number: "))
 if n%5==0 and n%7==0:
     print("yes")
 else:
     print("no")

 ! Eg:5
 Write a program to accept the cost price of a bike and display the road tax to be paid
 according to the following criteria:
           Cost price (in Rs)                           tax
           > 100000                                     15 % + discount 6%
           > 50000 and < 100000                         10%
           <= 50000                                     5%

# price = int(input("enter the price: "))
# amount = 0
# if price>=100000:
#     discount = price*(6/100)
#     value = price-discount
#     tax=value*(15/100)
#     total=value+tax
 
# else:
#     tax price* (5/100)
#     total price+tax
# print("The onroad cost of bike is: ",total)



#1-------> if elif else
#Eg:1
a = 7
h = 9
c = 3
if a>b and a>c:
print("A is greater")
elif boa and b>c:
print("B is greater")
else:
print("C is greater")



# A school has following rules for grading system:
# a. Below 25 -F
# b. 25 to 45 -E
# c. 45 to 50 -D
# d. 50 to 60 -C 
# e. 60 to 80 -B
# f. Above 80 -A
# ask user to enter marks and print the corresponding grade,



mark int(input("Enter mark: "))
If mark>=80 and mark<=100:
    print("A")
elif mark>=60 and mark<80:
    print("B")
elif mark>=50 and mark<60:
    print("C")
elif mark >=40 and mark<50:
    print("D")
else:
    print("Fail")


    
#!--> short hand if else
# Eg:1
a = 9
b = 60
# if a>b:
#     print("A")
# else:
#     print("B")
#? --> using short hand if else
# * Rules
# 1.) statement inside the if condition have to be present at first
# 2.) elif cannot be used in short hand if else
# 3.) Always it have to end with else

# print("A") if a>b lse print("B")


# ! code to check the given char is vowel or consonent
 char = input("enter the char:")
# if char="a" or char 'e' or char'1' or charo or char =='u':
#      print("is a vowel")
# else:
4      print("its consonent")
# ? or

str1 = "aeiouAEIOU"
if char in str1:
       print("vowel")
else:
       print("consonnt")


# ? using shorthand if else
# char input("Enter the char: ")
# stri "aeiouAEIOU"
# print("vowels") if char in str1 else print("consonent")


# print("a is greater") if a>b and b>a else print("b is greater")
# if b>a and b>c else print("c is greater")



 







