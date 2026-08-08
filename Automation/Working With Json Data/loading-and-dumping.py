# In this lesson, I will be learning about how to convert json data to dict and vice versa

import json

data_from_api = '{"name": "amot the dev", "age":45, "role":"web dev and automation expert", "salary":4560000}'

# the data can be now be converted to normal python dictionary
dict_data = json.loads(data_from_api)
print(dict_data)

# and at the same time, python dictionaries can also be converted to json
python_dict_data = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None} 

print(json.dumps(python_dict_data))