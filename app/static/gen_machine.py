import uuid
import random
import json
import namegenerator

'''
This script is used to generate the contents of machines.json

If you want to get new data, you can replace the contents of machines.json
with `[]`, than you can run via `python3 gen_machines.json`

The data in make_machine() can be set as you wish.
'''
def make_machine():
    dict = {}
    dict["id"] = str(uuid.uuid1())
    dict["name"] = namegenerator.gen()
    dict["type"] = random.choice(["washer", "dryer"])
    dict["running"] = False
    dict["status"] = "normal"
    dict["position"] = { "x": 0, "y": 0}
    dict["room_id"] = random.choice(["gay", "independence", "green_prairie", "the_apartments", "blakely", "pine", "spooner"])
    return dict

m = int(input("How many machines? "))

for i in range(m):
    with open('machines.json', 'r') as json_file:
        data = json.load(json_file)
        data.append(make_machine())

    with open('machines.json', 'w') as json_file:
        json.dump(data, json_file)
