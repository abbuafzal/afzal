# ! -----> common function for list
l1 = [6, 7, 8, 9, 0]
print(len(l1))

print(max(l1))
print(min(l1))

l1 = [6, 8, 9, "p", "u"]
# print(max(l1)) # ----> error coz its a combination of int and string
# print(min(l1)) # ----> error coz its a combination of int and string

l1 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
# print(min(l1)) # -5

l1 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
# index ()  ---> to get index value of specific element
# print(l1.index(9))

l1 = [6, 6, 6, 7, 8, 9, 0, 8.89, -5, 0.78]
# count() --> how many num of times an element is repeated
# print(l1.count(6))

# ! some functions which is specifically used for list

# To add elelment inside list
# ? Insert(index_value, element)
l1 = [6, 6, 6, 7, 8, 9, 0, 8.89, -5, 0.78]
l1.insert(2, "car")
print(l1)

# ? to delete element from list
l1 = [6, 6, 6, 7, 8, 9, 0, 8.89, -5, 0.78]
#pop()
l1.pop()
print(l1)
# pop(index_value)
l1.pop(4)
print(l1)

# * remove(element) ---> used to delete element directly
l1.remove(8.89)
print(l1)

#* clear() ----> complete delete all element in list
l1.clear()
print(l1)

# del --> to delete
#del l1
print(l1)

# ? ----> join 2 list

l1 = [9, 0, 8]
l2 = ["p", "o", "t", 34]
print(l1+l2)

# or
# exetend() --> to combine 2 list
l1.extend(l2)
print(l1)

# ? -----> copy()
l1 = [6, 7, 8, 9, 3]
l2 = l1.copy
print(l2)
print(l1)

print(id(l1))
print(id(l2))

# ! diff between shallow copy and deep copy
# shallo copy
import copy

l1 = [8, 9, 0, [5, 6],[3, 2, 1]]
l2 = copy.copy(l1)
l1.append(890)
print(l1)
print(l2)

# * deep copy
import copy
l1 = [8,9,0,[5,6],[3,2,1]]
print(l1[-1][1])

l2 = copy.deepcopy(l1)
l1.append('cars')
print(l1)
print(l2)

# ? sort ---> arrange elements in list in ascending or descending order
l1 = [9, 7, 45, 0, -6, 5, 12]
l1.sort()
print(l1)

l1.sort(reverse=True)
print(l1)

l1 = ['z', 'i', 'o', 'p', 9]
#l1.sort()
print(l1)

# list constructor
#list() ---> to convert other collection data type to list
l3 = ((8, 9, 0))
print(list(l3))

# ! ---> nested list

l1 = [8, 9, [0, 8, 7], ["p", "o", 'y'], [8, 't']]
print(l1[-2][1])

print(l1[1:4])
print(l1[1:-1])

# ? to delete "t" from l1
l1[-1].remove('t')
print(l1)

# ? combine these ["p", "o", 'y'],[8, 't'] lists in l1 to ["p", "o", 'y',8, 't']
l1[-2].extend(l1[-1])
l1.pop(-1)
print(l1)

# ! ------> Tuple
# * char of tuple

# 1.) Tuple have to be sourrund by ()
# 2.) the elements inside tuple are not chargable
# 3.) The elements inside tuple are indexed
# 4.) The elements will execute in order
# 5.) It is heterogenous
# 6.) It allow duplicate elements

# * eg:1
t1 = (8, 8, 9, 6, 5.78, [9, 0], (6, 8), "hey", 9+6j)
print(t1)
print(type(t1))

# ? Indexing, slicing are all same as list

t1=8,9
print(type(t1)) # tuple

t2=8,
print(type(t2))  # tuple

# len(), min(), max(), index(), count() --> all same as kist


# Iterate based on index value

l1=[9,8,0,6,5,7,36,54,55,6,43,5,66]
for i in range(0,len(l1)):
    print(l1[i])
# * sort tuple
#t1 = (8, 9,0, 89, 12)
#print(tuple(sorted(t1)))
#print(tuple(sorted(t1, reverse=True)))

# * Iterate list and tuples

# Iterate based on Elements

#l1 = [9, 8, 0, 6, 5]
#for i in l1:
    #print(i)

# * Iterate based on Index value
#l1 = [9, 8, 0, 6, 5]
#for i in range(0,5):
    #print(i)


#l1 = [9, 8, 0, 6, 5]
#print(l1[2])


#t1 (8, 9,0 89,12)
#print(tuple(sorted(t1)))
#print(tuple (sorted (t1, reverse=True)))
# print(len(s1))
# print(max(s1))
# print(min(s1))
# ord() --> used to find the ASCII value of a character
# ord() --> used to find the ASCII value of a character
# replace() --> to replace a specific char in the string
'''
s1= "where are you.?"
print(s1.replace('r','&&'))
'''

# swapace() --> to convert capital to small and small to capital at a time
'''
s1 = "HEY there"
print(s1.swapcase())
'''# join the strings
'''
s1 = "hello"
s2 = "world"
print(s1+s2)
'''# Swapcase()---> to convert capital to small and small to capital

s1="HEY there"
print(s1.swapcase())


# Title() --> to write the string in format of title
s1='never giveUP'
print(s1.title())  # --> Never Giveup


# Capitalize() ---> 1st char of string will be converted to capital

s1='never giveUP'
print(s1.capitalize())

# Join the strings
s1 = "hello"
s2 = 'world'
print(s1+s2)


#s1 = "hello world"
#print(s1.find('z'))
#print(s1.index('z'))


# * join() -->
l1 = ["hey" ,"there"]
print(" ".join(l1))
print("$".join(l1))

s1 = "welcome to all"
# * print(s1.endswith('1'))
# * print(s1.startswith('w'))

# s1 = "67"
# print(type(s1))
# print(s1.isdigit())

# * print the string  in reverse manner
# s1 = "welcome to all"
# print(s1[::-1])

# ! ---> eg:1
# wap to find the number of lower case letters
s1 = "HEY there you are"
count = 0
for i in s1:
    if i.islower():
        count+=1
print("the total num of lower case letters: ",count)


# ! ------> eg:2    r------------> "$"
s1 = 'restarter'
# s1 = "IMAGIN"

# str1 = "bbbbbbyyyybbbbaaioo"
# str2 = "%"



      






