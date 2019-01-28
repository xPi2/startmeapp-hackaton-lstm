import random
import time

import requests

for x in range(1000):
    data = {
        "num_object": random.randint(1, 2),
        "objects": "patera"
    }
    r = requests.post('http://localhost:5000/post/8', json=data)
    print(x)

for x in range(500):
    data = {
        "num_object": 0,
        "objects": "patera"
    }
    r = requests.post('http://localhost:5000/post/8', json=data)
    print(x)

for x in range(700):
    data = {
        "num_object": 1,
        "objects": "patera"
    }
    r = requests.post('http://localhost:5000/post/8', json=data)
    print(x)

for x in range(300):
    data = {
        "num_object": 0,
        "objects": "patera"
    }
    r = requests.post('http://localhost:5000/post/8', json=data)
    print(x)


print("END!")

time.sleep(2)
r = requests.post('http://localhost:5000/clean/')
print("CLEAN")
