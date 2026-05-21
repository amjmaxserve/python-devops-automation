
# simple python print function
print("Hello python")

# integer 
a = 45
#string
b ='Arjun'

# float 
c = 3.14

print(a, b, c)

s = "this code made by arjun's"
print(s)

# single multiline string

s = '''
    this bat is Arjun's
    arjunmj
    amjmaxserve
'''

print(s)

# boolean data type

is_valid = True
has_permission = False

print(is_valid, has_permission)


# List 
# list is mutable in the sense we can change values even after created...

a = [1, 2, 3, 'Arjun', True]

print(type(a))

print(a)

#  tuple
# Immutable we canno't change the values of touple 

b = (1, 2, 3, 'Arjun', True)
print(type(b))
print(b)

# Dictonaries

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(type(my_dict))
print(my_dict['name'])
print(my_dict['age'])
print(my_dict['city'])


# Set 
# Set remove duplicate items and show the repeated value only once...
my_set = { 1,2,2,3,3,3,4,5}

print(type(my_set))
print(my_set)


#---------------------------------------------------

x = 5
y = 7

addition = x + y
sub = y - x
multiply = x * y
division = y / x

print('value of x = ', x , 'value of y = ', y)
print('x + y = ', addition)
print('y - x = ', sub)
print(' x * y = ',multiply)
print('y / x = ', division)

my_list = [1,2,3,4,5,'arjun']
print(my_list)

print(my_list[3])

my_list[0] = 'devops'

print(my_list)

my_touple = (1,2,3,4,5,67,'amjmaxserve')
print(my_touple)

print(my_touple[4])

# my_touple[4] = 234

# print(my_touple)

## Error touple does not support item assignemnt