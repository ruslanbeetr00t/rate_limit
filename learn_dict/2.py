import json
import requests
from ratelimit import limits
import time

FIFTEEN_MINUTES = 900


@limits(calls=1, period=FIFTEEN_MINUTES)
def firt_try(url='https://jsonplaceholder.typicode.com/todos/1'):
    try:
        while True:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(response.json(), time.ctime())
    except KeyboardInterrupt:
        print('ok')
    except requests.exceptions.ReadTimeout as e:
        print(e)

firt_try()



