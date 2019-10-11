import uuid
import random
import json
import namegenerator

def make_machine():
    dict = {}
    dict["id"] = str(uuid.uuid1())
    dict["name"] = namegenerator.gen()
    dict["type"] = random.choice(["washer", "dryer"])
    dict["running"] = random.choice([True, False])
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
