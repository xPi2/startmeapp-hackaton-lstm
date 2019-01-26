import random
import time

import requests

for x in range(400):
    data = {
        "value": random.randint(1, 2),
        "objeto": "patera"
    }
    r = requests.post('http://localhost:5000/post/8', json=data)
    print(x)

print("END!")