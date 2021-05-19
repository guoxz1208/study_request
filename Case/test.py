# coding = utf -8
import json
import requests

# token = {'Vary': 'Origin, Access-Control-Request-Method, Access-Control-Request-Headers', 'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJ3ZWIiLCJpc3MiOiJzcHJpbmctYm9vdC1wbHVzIiwiZXhwIjoxNjIxMzYwNzEyLCJpYXQiOjE2MjEzMjQ3MTIsImp0aSI6ImRmYTkxYTg2M2Q4OTQ1OGZiYWE5OWVmMmY0ZTg1YzM4IiwidXNlcm5hbWUiOiJhZG1pbiJ9.IjsqH1LyQeD4fZfJEao9u9C3Cu2W-VW01zoxxii0-Fs', 'Content-Type': 'application/json;charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Date': 'Tue, 18 May 2021 07:58:32 GMT', 'Keep-Alive': 'timeout=60', 'Connection': 'keep-alive'}
# token_value = json.dumps(token)
# print(token_value)


url = "http://47.101.48.192:8001/api/login"
login_value = {"username": "admin", "password": "123456"}
res = requests.post(url,json=login_value)
text = res.json()
print(text)
print(json.dumps(text))
token = res.headers
print(token)