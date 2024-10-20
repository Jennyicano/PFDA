# following lecture json
#Author Jenny Ibanez

import json
data ={
    'name': 'joe',
    'age':21,
    "student": True
}
jsonSting = json.dumps(data)
print(data)
print(jsonSting)