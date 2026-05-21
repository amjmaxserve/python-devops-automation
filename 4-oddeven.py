# Taking user input 

user_input = int(input("Enter an Integer: "))

# checking if the number is odd or even
if user_input % 2 == 0:
    print(f"{user_input} is an even number.")
else:
    print(f"{user_input} is an odd number.")

# Using loops to print number from 1 to user input number 

print("Numbers from 1 to", user_input)
for i in range(1,user_input + 1):
    print(i)

