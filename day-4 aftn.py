'''
for row in range(5):
    for col in range(5):
        print(row, end=" ")
    print()
''
for row in range(6):
    for col in range(7):
        print("*", end=" ")
    print()
'''

#! to print starts in right angled triangle


'''

for row in range(0,6):
    for col in range(0,row+1):
        print("*" , end= " ")
    print()

''
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

for row in range(0,6):
    for col in range (row,6):
        print("*" , end= " ")
    print()

''
# * * * * * *
# *         *
# *         *
# *         *
# *         *
# * * * * * *

for row in range(5):
    for col in range(5):
        if col==0 or col==5-1 or row ==0 or row ==5-1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
''

            
      
#       *  
#     * * * 
#   * * * * *  
# * * * * * * *

 



for row in range(0, 5):
    for col in range(0, 6):
        if ((row==0 and col==3) or (row==1 and (col>=2 and col<=4) or
                                  (row==2 and (col>=1 and col<=5)))) :
           print("*", end="")
        else:
           print(" ", end="")
    print()
''
# *
# * *
# *   *
# *     *
# *       *
# *         *
# * * * * * * *

for row in range (0,7):
    for col in range(0,8):
        if (row==0 and col==2 or (row==0 and (col>1 and col<=8) or
                                    (row==1 and (col>=1 and col<=8)))):
            print(" *", end=" ")
        else:
            print(" ", end=" ")
    print()



!---> Datatypes
Primary
Number --> int, float complex
String
Boolean
None
Collection
List
tuple
set
dictionary



''

# ?-----> List

#1.) if the collection of elements are sorounded by square brackets,it is consider
to be list 
#! eg:
    # 11 [4, 7, 9, 9.89, "hello", 7+9j, [8, 9, 9]]

    



# * charactristics of list
# 1.) list have to be sorrrounded by []
# 2.) It is mutable (the elements in the list are changable)
# 3.) Every element inside list is indexed
# 4.) The elements inside list will be ordered format
# 5.) It can hold duplicate values.
# 6.) Its heterogenous


''

# To access the elements in list
l1 = [1,4,1,7,89,7.5, "P", "i"]
print(l1)

''
#--> Indexing
# In the collection datatypes like list, tuple, string, the elements will be alloted
# with pre-defined unique value called index value

#We have 2 types of indexing
# Positive indexing ----> starts with Ø from left hand side
# Negative indexing---> starts with 1 from right hand side


''


# ?--> Positive indexing
# 1st1 = [1, 4, 1, 7,89.7, 7.5, "p", "i"]
# print(lst1[0])
# print(1st1[4])
# print(1st1[20]) --> error


#?----> Negative indexing
#lst1= [1, 4, 1, 7,89.7, 7.5, "p", "i"]
print(lst1[-1])
print(1st1[-5])

''


# ? ----> slicing
lst1 = [1, 4, 1, 7,89.7, 7.5, "p","1"]
# 1st1[start_index:end_index:step]

print(lst1[0:4])
print(lst1[6:8])
print(lst1[3:6])
print(lst1[:5])
print(lst1[3:])
print(lst1[:])


print(lst1[0:7:1]) # lst1[0:7] ---> both are same
print(lst1[0:7:2])

''


lst1 = [1, 4, 1, 7,89.7, 7.5, "p", "i"]
print(lst1[-4:-1])
print(lst1[-1:-4]) --> []
print(lst1[-7:-1])
print(lst1[-7:-1:2]
''

# ! To insert ot add element inside list

# append() --> used to add elelement at last position of list
# l1 = [9, 8, 0, 6]
# l1.append("car")
# print(l1)

 
'''

# n = int(input("enter the number of inputs: "))
# for i in range(0, n):
#     a, b = list(map(int, input().split()))
#     print(a, b)

