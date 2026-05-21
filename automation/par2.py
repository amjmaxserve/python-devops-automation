import json

data = {'name': 'John Doe', 'age': 30, 'city': 'New York'}

# write the data to a json fole named output json

with open('output.json', 'w') as file:
    json.dump(data, file)
    print("Data has been written to output.json")

with open('output.json', 'r') as file:
    data = json.load(file)
    print("Data read from output.json:")
    print(data)
    