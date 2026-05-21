# Json manipulation
import json

json_data = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_data)

print(data)

print(data['name'])
print(data['age'])

data['country'] = 'USA'
data['age'] = 28

print(data)

updated_json_data = json.dumps(data)
print(updated_json_data)

#-------------------------------------------------------------
