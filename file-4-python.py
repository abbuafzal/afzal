# -----> while loop
# -----> break using while loop

# eg : 1
# 1.) iterate from 20 to 30 and break the loop in 27

i = 20
while i<31:
    print(i)
    i+=1

# 2.)
i = 20
while i<31:
    print(i)
    i+=1

    if i==27:
        break
    

# !-------> continue
# ---->  eg:1
i = 20
while i<31:
    if i==27:
        continue
    print(i)
    i=i+1


#i = 20
#while i<31:
    #i=i+1
    #if  i==27:
#        continue
   # print(i)
   

 # ! eg:5
 #while to iterate from 12 to 22
 # find the sum of all numbers

# i = 12
#sum=0
 #while i<23:
     #sum=sum+i
     #print(sum)
     #i+=1


# ! eg : 6
# find the average of value from 20 to 25

# i=20
# sum = 0
# count = 0
# while i<=30:
#       sum = sum+i
#       count+=1
#print(sum/count)


# ! ---> Eg:1
# Nested for loop
# for row in range(1, 3+1):
#for col in range(1, 4+1):
#print(row, col)

# Eg:2
# * * * *
# * * * *
# * * * *
# * * * *

 # rows = int(input("enter the rows: "))
# cols= int(input("enter the cols: "))

# for row in range(rows):
#       for col in range(cols):
#               print("*", end=" ")
#       print()

# sum = 0
#for row in range(5):
#      for col in range(5):
#           print (row, end=" ")
#       print()



# ! to print stars in right angled triangle

#for row in range(0, 6):
#    for col in range(0, row):
#        print("*", end=" ")
#     print()

# * * * * * *
# *           * 
# *           * 
# *           * 
# *           *
# * * * * * *


for row in range(5):
    for col in range(5):
        if col==0 or col==5-1 or row ==0 or row ==5-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()



#      *
#    * * *
#   * * * *
#  * * * * *

rows = 9

for i in range(rows):
    print(" " * (rows - i - 1), end='')  
    print("*" * (2 * i + 1), end='')    
    print(" " * (rows - i - 8u 1))


# *
# * *

# ? ---> List

# 1.) if the collection of elements are surrounded by Square brackets, it is considered to be list.
# ! ---> Eg:
# l1 = [4, 7, 9, 9.89, "hello", 7+9j, [8, 9, 0]]


# Characteristics of list
# 1.) List have to be surrounded []
# 2.) It is mutable (the elements in the list are changable)
# 3.) Every elements inside list is indexed
# 4.) The elements inside list will be ordered format
# 5.) It can hold duplicate values
# 6.) Its heterogenous

# to acess the elements in list
l1 = [1,4,1,7,89,75,"p","i"]
# print(l1)

# -----> indexing

#in the collection datatyoes like list,tuple,string,the elements will be alloted with
#pre-define unique value called index value

# We have 2 types of indexing
# Positive indexing --> starts with @ from left hand side
# Negative indexing --> starts with -1 from right hand side


#? -----> Positive indexing
# 1st1 = [1, 4, 1, 7,89.7, 7.5, "p", "i"]
# print(1st1[0])
# print(1st1 [4])
# print(1st1 [20]) --> error

# ? -----> Negative indexing
# 1st1 = [1, 4, 1, 7,89.7, 7.5, "p", "i"]
#print (1st1[-1])
# print(1st1 [-5])

# ?----> slicing
lst1 = [1,4,1,7,89,7,7.5,"p","i"]
# lst1[start_index:end_index:step]

# print(lst1[0:4])
#print(lst1[6:8])
#print(lst1[3:6])
#print(lst1[:5])
#print(lst1[3:])
#print(lst1[:])

# print(lst[0:7:1] # lst1[0:7] ---> both are same
# print(lst1[0:7:2])

# trail = int(input())


lst1 = [1,4,1,7,89.7,7.5,"p","i"]
# print(lst1[-4:-1])  




 


                                                        
        








# s1 = "hello world to all"
