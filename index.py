import requests
import random
import string
import json

print("code by github.com/kitidev")
repeat = int(input("repeat count: "))

url = "https://highrise.game/web/api"

def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))

for x in range(0, repeat): 
    data = {
        "_type": "CreateHighriseUserRequest",
        "username": (random_char(20)), #username cannot exceed 20 characters
        "email": (random_char(20)) + "@highrise.game",
        "password": (random_char(15)) #password need more than 5 characters
    }

    requests.packages.urllib3.disable_warnings()
    response = requests.post(url, verify=False, json=data)

    try:
        response_json = response.json()
        print("Account create! Id: " + response_json['user_info']['user_id'] + ", Username: " + response_json['user_info']['username'])
    except json.decoder.JSONDecodeError:
        print("ERROR")
print("done!")
