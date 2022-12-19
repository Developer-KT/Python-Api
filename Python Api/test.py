import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"likes": 118, "name": "Joe", "views": 10000},
    {"likes": 6020, "name": "How to make a REST API", "views": 102000},
    {"likes": 3001, "name": "Tim", "views": 84000}
]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())

# input()

response = requests.get(BASE + "video/2")
print(response.json())