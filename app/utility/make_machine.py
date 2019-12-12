import uuid
import random
import json

# pip3 install namegenerator
import namegenerator

'''
This script is used to generate new machines.
'''

dict = {}
dict["id"] = str(uuid.uuid1())
dict["name"] = input("Enter a machine name: ")
dict["type"] = input("Enter type: (washer or dryer): ")
dict["running"] = False
dict["status"] = "normal"
dict["room_id"] = input("Enter room: (gay, independence, green_prairie, the_apartments, blakely, pine, spooner): ")
print()
print(dict)
