
# Eg:1,
##def profile(name, age, place):
##    txt ="My name is{}. Iam {} years old.Iamfrom {}."
##    print(name,  age, place)
##profile("mani", 22, "ndl")

# Eg:2,
# ? Function with return statement

# ! return 
# ? Function with return statement
#1.) A variable declared inside the function can be accessed outside the function
#using return
#2.) return does not prrint anything
#3.) we cannot write any code below return statement

##def f1():
##    z = 8
##f1()
##print(z) # error ---->cannot use outside the function

##def f1(a, b):
##    c = a*b
##    return c
###print(f1(6, 8))
##obj = f1(6, 8)
##obj1 = f1(4, 6)
##
##def gracemark(object):
##    print(object+4)
##gracemark(obj)
##gracemark(obj1)

# ? problem:1;
#123

##def palindrom(n):
##    string = str(n)
##    rev = str(n)[::-1]
##    if string==rev:
##        print(n, "palindrom")
##    else:
##        print("Not palindrom")
##a= int(input("Enter the value: "))
##palindrom(a)

#? Based on the declaration of parameter
#? functions are divided into 5 catagories

# postal args
# keywords args
# defalt args
# variable length args
# keyword variable length args

# * Positional args
#Eg:1;
##def profile(name, phone, mark):
##    txt ="My name is {}. My phone number is {}. I got {} marks."
##    print(txt.format(name, phone, mark))
##
##    profile(9704984013, "mani", 92)

##Keyword args
##Eg:1
##? To overcome the disadvantage of position args, we use keyword arg
##? It is the process of initialising the paremeter with the args while calli function

# ? function

##def profile(name, phone, mark):
##    txt "My name is {). My phone number is (). I got () marks."
##    print(txt.format(name, phone, mark))
##    
##profile(name="sid", mark=96, phone-1234567890)

# todo ---> Exception of keywords args function
##def profile(name, phone, mark):
##    txt = "My name is {}.My phone number is {}.I got {} marks"
##    print(txt.format(name, phone, mark))
##
##profile("sid", marks=98, phone=9704984013)

# * Default args
# Eg:1;
##def profile(name, phone, place="nandyal"):
##    txt = "My name is {}.My phone number is {}.I am from{}."
##    print(txt.format(name, phone, place))
##
##profile("mani",7842684013,"nandyal")

##def profile(name, phone, place="nandyal"):
##    if(place=="nandyal" or place!="nandyal" or place != "kadapa"):
##       txt = "My name is {}.My phone number is {}.I am from{}."
##       print(txt.format(name, phone, place))
##    else:
##         print("not eligible" )
##profile("mani",7842684013,)

#Exception
##def profile(name, phone, place="nandyal"):
##    
##    if(place=="nandyal" or place!="nandyal" or place != "kadapa"):
##       txt = "My name is {}.My phone number is {}.I am from{}."
##       print(txt.format(name, phone, place))
##    else:
##         print("not eligible" )
##profile("mani",7842684013,)

# ! Eg:1;

##name = "mani",'name2','name3'
##def profile(*name):
##    for val in name:
##        print("My name is",val)
##profile("mani", 'name2', 'name3') 

# ! Eg:2;
##def profile(*name, age):
##    for val in name:
##        print("My name is", val, "may age is", age)
##profile(28, "sod", 'name2', 'name3')#---->age has no args

 #          (or)
##def profile(*name, age):
##    for val in name:
##        print("My name is", val, "may age is", age)
##profile(28, "sod", 'name2', 'name3')

# * keyword variable length args
# kwargs---> which is usde to provid the args in the form of key value pair.
# ! Eg:1;
##def price(**price_list):
##    print(price_list)
##
##print(shirt=1000, iphone=80000)

##d1 = {"a":100, "b":200, "c":300}
##d1 = dict("a":100, "b":200, "c":300)
##print(d1)

#n = 5
#{1:1, 2:4, 3:9, 4:16, 5:25}

#n = int(input("enter the number: "))

##def dict1(n):
##    d1 = {}
##    for val in range(1, n+1):
##        d1[val] = val**2
##    print(d1)
##dict1(5)

# !---------> object oriented programming
# The paradigms of objectes oriented programming are

##class
##objects
##inheritance
##polymarphism
##abstraction
##encapsulation

# ! class is a blue print of an object
#l1 = [1,2,3,4,5,6]

# ?Eg:1
##class c1:
##    name = "mani"
##    print(name1)

# ?Eg:2
##calss person:
##    name = "mani"

##c = person() # c os object
#The process of creation of an object is called as instantiation
##print(c.name)

# ?Eg:3;
#create of a method
#when the funtion is created with a class is called as method

##class person:
##    def display(person): # it is a methodaasd
##        print("Hello welcome to classes")

##p = person()
##p.display()

# ?Eg:4;
# ! Method with parameter

##class person:
##    def display(person, name, age):
##        print(name, age)
##        
##p = person()
##p.display()  

# ?Eg:5;
##class person:
##    fname = "mani" #attribute or static variable
##    lname = "T"
##    def display(SELF):
##        print(self.frame+" "+self.lname)

##p = person()
##p.first_name() 
##p.full_name()

# ?Eg:6;
 #constructors  -->__init__()
# This is a special method which has the ability to execute to itself without
# calling it manullay through the process of instantiation

##class profile:
##    def __init__(self): # constructor method
##        print("hey")
##p = profile() # throught this process
##p.__init__()







