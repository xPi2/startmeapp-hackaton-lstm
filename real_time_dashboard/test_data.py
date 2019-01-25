import random
import time

import requests

for x in range(50):
    data = {
        "value": random.randint(0, 3),
        "objeto": "patera"
    }
    r = requests.post('http://localhost:5000/post/8', json=data)
    time.sleep(1)
    print(x)
