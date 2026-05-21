
# taking user input and printing 
a = float(input("Enter a number: "))
print("user enterd the number: ", a)


# If-else condition

age = int(input("Enter your age: \n"))
if age >= 18:
    print("User is Adult")

else:
    print("User is minor")


# For multiple condition

score = int(input("Enter your score: \n"))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print('Grade is: F')


# Nested if condition

x = 10
y = 5

if x > y:
    print('X is greater than y')
    if x > 15:
        print('x is also greater than 15')
    else: 
        print('x is not greater than 15')
else:
    print('x is not greater than y')


