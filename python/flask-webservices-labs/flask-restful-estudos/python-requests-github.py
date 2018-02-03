import requests

#endpoint = "https://api.github.com/teams"
endpoint = "https://api.github.com/events"
rq = requests.get(endpoint)

print("status-code:")
print(rq.status_code)
print("headers:")
print(rq.headers['content-type'])
print("text:")
print(rq.text)
print("json:")
print(rq.json())