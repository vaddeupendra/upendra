# ! --------> common funtions for list
'''
l1 = [6,7,8,9,0]
# print(len(l1))
''
# print(max(l1))
# print(min(l1))
''
# l1 = [6,7,8,9,"p","u"]
#print(max(11))# --> error coz its a combination of int and string
#print(min(11)) # --> error coz its a combination of int and string

#11 [6, 7, 8, 9, 0, 8.89, -5, 0.78]
#print(min(11)) # -5
''


# 11 = [6, 7, 8, 9, 8, 8.89, 5, 0.78]
# index()---> to get index value of specific element
# print(l1.index(9))
''
# 11 = [6,6,6, 7, 8, 9, 8, 8.89, -5, 0.78]
# count() --> how many num of times an element is repeated
# print(l1.count(6))
''


#!  some functions which is specifically used for list

# To add element inside list
# ? insert(index value, element)---> to add element at specific îndex position
l1 = [6,6,6, 7, 8, 9, 8, 8.89, 5, 8.78]
l1. insert(2, "cars")
print(11)
''

# pop(index_value) ----> used to delete element at specific index
# l1.pop(4) # 4 is index value
# print(l1)
''




# *remove(element) --> used to delete element directly
# l1. remove(8.89)
# print(11)
''


#* clear() --> to complete delete all element in list
l1.clear()
print(l1)
''

# del-> to delete the list
# del 11 #or del (11)
# print(11)

# ?----> join 2 lists.
''
l1 = [9, 0, 8]
l2=["p", "o", "t", 34]
print(l1+l2)
''


# ? -------> copy()
l1 = [6, 7, 8, 9, 3]
l2 = l1.copy()
print(l2)
print(l1)
    
print(id(l1))
print(id(l2))
''

#! diff between shallow copy and deep copy
* shallow copy
Import copy
l1 = [8, 9, 8, [5, 6], [3, 2, 1]]
l2 = copy.copy (l1)
l1.append(890)
print(l1)
print(l2)
''
# * deep copy
import copy
l1 = [8, 9, 8, [5, 6], [3, 2, 1]]
print(11[-1][1]) ----> to index nested list
''


# l2 = copy.deepcopy(l1)
l1[-1].append('cars')
print(l1)
print(l2)
''
# ? sort ----> arrange elements in list in ascending or descending order
l1 = [9,7,45,0,-6,5,5,12]
l1. sort() # to arrange in ascending order
print(l1)

# l1. sort (reverse=true) # to sort in descending order
print(l1)
''
# ? list constructer
* list() --> to conver other collection datatype to list
l3 = ((8,9,0))
print(list(l3))

l4 = (*,9)
print(list(l4))
''

# ! ----> nested list
l1 = [8,9,[0,8,7],["p","o",'y'],[8,'t']]
print(l1[-2][1]) # ---> 0

print(l1[1:4])
print(l1[1:-1])

# ? to delete "t" from l1
l1[-1].remove('t')
print(l1)
''
# ? combine these ["p","o','y'],[8,'t'] lists in l1 to ["p","o",'y',8,'t']
l1[-2].extend(l1[-1])
l1.pop(-1)
print(l1)

''
# ! -------> tuple
# *char of tuple

# 1.) tuple to be surrounded by ()
# 2.) the elements inside tuple are not changable
# 3.) the elements inside tuple are indxed
# 4.) the element will execute in order
# 5.) it is heterogenous
# 6.) it allow duplicate elements

# eg:
t1 = (8,8,9,6,5.78,[9,0](6,8), "hey",9+6j)
print(t1)
print(type(t1))
''

# ? indexing, slicing are all same as list

l1 = (8)
print(type(l1)) # int
      


l1 = (8,)
print(type(l1)) # tuple

t1 = 8,9
print(type(t1)) # tuple

t2 = 8,
print(type(t2)) # tuple

len(), min(),max(), index(), count()---> all as list
''

# to add element inside tuple ----> cannot add
# cannot delete any element from tuple

# * jion 2 tuples
t1 = (8,9,0)
t2 = (6,7,8)
print(t1+t2)
''

# * to add all element inside list and tuple
# sum()
l1 = (8,9,7,6)
print(sum(l1))
''
# * sort tuple
t1 = (8,9,0,89,12)
print(tuple(sorted(t1)))
print(tuple(sorted(t1,reverse=true)))

'''
# * iterate based on index value
l1 = [9,8,0,6,5,8,56]
for i in range(0,len(l1)):
    print(l1[i])















