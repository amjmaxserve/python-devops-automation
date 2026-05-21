
# Modules in means calling variables or function from another python file 
# we use import command to import other files or modules to our functions...

import math_operations

a = math_operations.add(5,6)

print(f"the addition result of 5 and 6 is: {a}")
print(f" the subtraction function result is {math_operations.subtract(7,4)}")

print(f" the multiplication function result is {math_operations.multiply(7,4)}")

print(f" the division function result is {math_operations.divide(10,5)}")

print(f" the division function result is {math_operations.divide(7,0)}")


x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

b = math_operations.multiply(x, y)

print(f"the multiplication result of x and y is: {b}")