import random
import time

import requests

for x in range(1000):
    data = {
        "value": random.randint(1, 2),
        "objeto": "patera"
    }
    r = requests.post('http://localhost:5000/post/8', json=data)
    print(x)

for x in range(500):
    data = {
        "value": 0,
        "objeto": "patera"
    }
    r = requests.post('http://localhost:5000/post/8', json=data)
    print(x)

for x in range(700):
    data = {
        "value": 1,
        "objeto": "patera"
    }
    r = requests.post('http://localhost:5000/post/8', json=data)
    print(x)

for x in range(300):
    data = {
        "value": 0,
        "objeto": "patera"
    }
    r = requests.post('http://localhost:5000/post/8', json=data)
    print(x)


print("END!")

time.sleep(2)
r = requests.post('http://localhost:5000/clean/')
print("CLEAN")
