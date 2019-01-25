import random
import time

import requests

listdata = [

    {
        "value": 0,
        "objeto": "patera"
    },

    {
        "value": 0,
        "objeto": "patera"
    },
    {
        "value": 0,
        "objeto": "patera"
    },
    {
        "value": 0,
        "objeto": "patera"
    },
    {
        "value": 0,
        "objeto": "patera"
    },
    {
        "value": 0,
        "objeto": "patera"
    },
    {
        "value": 0,
        "objeto": "patera"
    },

    {
        "value": 0,
        "objeto": "patera"
    },
    {
        "value": 0,
        "objeto": "patera"
    },
    {
        "value": 0,
        "objeto": "patera"
    },
    {
        "value": 0,
        "objeto": "patera"
    },

    {
        "value": 0,
        "objeto": "patera"
    },
    {
        "value": 0,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 0,
        "objeto": "patera"
    },
    {
        "value": 0,
        "objeto": "patera"
    },
    {
        "value": 0,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 1,
        "objeto": "patera"
    },
    {
        "value": 2,
        "objeto": "patera"
    },
    {
        "value": 2,
        "objeto": "patera"
    },
    {
        "value": 2,
        "objeto": "patera"
    },
    {
        "value": 2,
        "objeto": "patera"
    },
    {
        "value": 2,
        "objeto": "patera"
    },
    {
        "value": 2,
        "objeto": "patera"
    },
    {
        "value": 2,
        "objeto": "patera"
    },
    {
        "value": 2,
        "objeto": "patera"
    },
    {
        "value": 2,
        "objeto": "patera"
    },
    {
        "value": 2,
        "objeto": "patera"
    },
    {
        "value": random.randint(0, 3),
        "objeto": "patera"
    },
    {
        "value": random.randint(0, 3),
        "objeto": "patera"
    },
    {
        "value": random.randint(0, 3),
        "objeto": "patera"
    },
    {
        "value": random.randint(0, 3),
        "objeto": "patera"
    },
    {
        "value": random.randint(0, 3),
        "objeto": "patera"
    },
    {
        "value": random.randint(0, 3),
        "objeto": "patera"
    },
    {
        "value": random.randint(0, 3),
        "objeto": "patera"
    },
    {
        "value": random.randint(0, 3),
        "objeto": "patera"
    },
    {
        "value": random.randint(0, 3),
        "objeto": "patera"
    },
    {
        "value": random.randint(0, 3),
        "objeto": "patera"
    },
    {
        "value": random.randint(0, 3),
        "objeto": "patera"
    },
    {
        "value": random.randint(0, 3),
        "objeto": "patera"
    },
    {
        "value": random.randint(0, 3),
        "objeto": "patera"
    },
    {
        "value": random.randint(0, 3),
        "objeto": "patera"
    },
    {
        "value": random.randint(0, 3),
        "objeto": "patera"
    },
    {
        "value": random.randint(0, 3),
        "objeto": "patera"
    },
    {
        "value": random.randint(0, 3),
        "objeto": "patera"
    },
    {
        "value": random.randint(0, 3),
        "objeto": "patera"
    },
    {
        "value": random.randint(0, 3),
        "objeto": "patera"
    },
    {
        "value": random.randint(0, 3),
        "objeto": "patera"
    },
    {
        "value": random.randint(0, 3),
        "objeto": "patera"
    },
    {
        "value": random.randint(0, 3),
        "objeto": "patera"
    },

]

for x in listdata:
    data = {
        "value": random.randint(0, 3),
        "objeto": "patera"
    }
    r = requests.post('http://localhost:5000/post/8', json=data)
    time.sleep(1)
    print(x)
