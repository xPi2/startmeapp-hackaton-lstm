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

time.sleep(5)

for x in range(300):
    data = {
        "value": 3,
        "objeto": "patera"
    }
    r = requests.post('http://localhost:5000/post/8', json=data)
    print(x)


time.sleep(2)
for x in range(500):
    data = {
        "value": 3,
        "objeto": "patera"
    }
    r = requests.post('http://localhost:5000/post/8', json=data)
    print(x)

print("END!")

time.sleep(2)
r = requests.post('http://localhost:5000/clean/')
print("CLEAN")
