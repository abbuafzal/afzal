# ! -------> Tasks

# write the code for the below tasjs using function
# 1.)d1 = {"shirt": 1000, "pant": 1500, "Shoes": 900, "handkey": 30}
# a.) Find the min ans max priced product
# b.) Find the product starts with "s" and "S"

# 2.) Find the n = 67, is strong number or not

# 3.) l1 = [1,2,3,4,5,6]
# n=2 --> [5,6, 1,2,3,4]
# n=3 --> [4,5,6, 1,2,3]

# Task 1
def find_min_max_price(products):
    min_price = min(products.values())
    max_price = max(products.values())
    return min_price, max_price

def find_products_starting_with_s(products):
    s_products = [product for product in products.keys() if product.lower().startswith('s')]
    return s_products

# Task 2
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def is_strong_number(n):
    sum_of_factorials = sum(factorial(int(digit)) for digit in str(n))
    return sum_of_factorials == n

# Task 3
def rotate_list(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]

# Example usage
d1 = {"shirt": 1000, "pant": 1500, "Shoes": 900, "handkey": 30}
print("Min and Max priced product:", find_min_max_price(d1))
print("Products starting with 's' or 'S':", find_products_starting_with_s(d1))

n = 67
print(n, "is a strong number:", is_strong_number(n))

l1 = [1, 2, 3, 4, 5, 6]
n_values = [2, 3]
for n in n_values:
    print("Rotated list for n =", n, ":", rotate_list(l1, n))


# ! Method riding
# * polymorphism in classes

class bank:
    def ratio(self):
        print("All banks has repo rate")
        
class SBI(bank):
    def ratio(self):
        print("SHI rate is 9%")
        

class IOB(bank):
    def ratio(self):
        print("IOB rate is 7.5%")

i = IOB()
i.ratio()

s = SBI()
s.ratio()

class c1:
    def f1(self):
        print("class 1")

class c2(c1):
    def f1(self):
        super().f1()
        print("class 2")

obj1 = c2()
obj2 = c1()


def display(a):
    a.f1()
display(obj1)
display(obj2)

# * changing the functionality of builtin functions
a = 9
b = 6
print(a+b)
print(a._add_(b)) # ? dunder method or mafic method


int()
print(a._sub_(b))
len()

