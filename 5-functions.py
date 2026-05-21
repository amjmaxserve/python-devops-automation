'''
Functions are reusable unit in sourcecodes. 

make code more efficient 
'''


def greet(name):
    print(f"Hello, {name}!!!")

greet('arjun')
greet('anu')


# Addition function...
def addition(x, y):
    return x+y

print(addition(3,5))
print(addition(345,555))


# is even check 
def is_even(num):
    return num % 2 == 0

# is odd check 
def is_odd(num):
    return num % 2 != 0

# find the squre of the number
def squre(num):
    return num ** 2

# test the functions 

num = 10

if is_even(num):
    print(f"{num} is even")
else:
    print(f"{num} is odd")

print(f"the squre of {num} is: {squre(num)}.")


    

