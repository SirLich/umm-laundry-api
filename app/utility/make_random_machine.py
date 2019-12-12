import uuid
import random
import json
import namegenerator

'''
This script is used to generate new random machines.
'''
def make_machine():
    dict = {}
    dict["id"] = str(uuid.uuid1())
    dict["name"] = namegenerator.gen()
    dict["type"] = random.choice(["washer", "dryer"])
    dict["running"] = False
    dict["status"] = "normal"
    dict["room_id"] = random.choice(["gay", "independence", "green_prairie", "the_apartments", "blakely", "pine", "spooner"])
    return dict

print()
print(make_machine())