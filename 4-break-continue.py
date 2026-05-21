print('break is used here..')
for i in range(10):
    if i == 5:
        break
    print(i)


print('continue used here...')
for i in range(10):
    if i == 5:
        continue
    print(i)


# For loops in dictionary
person = {'name': 'john', 'age': 30, 'city': 'new york'}

for key,value in person.items():
    print(f'{key}:{value}')



