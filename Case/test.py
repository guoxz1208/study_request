# coding = utf -8
import json

expData = "{'code': 200, 'success': True}"
print(type(expData))
data = json.loads(expData)
print(type(data))
print(data)