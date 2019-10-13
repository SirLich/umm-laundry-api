import time
import json
import random

'''
This script emulates machines turning on and off naturally.
Run this script, and the json file `machine.json` will be edited to reflect
the machine status "running" changing.

If this script isn't run, the data served up via the Flask server will be static
'''


WASHER_TIME = 0.5 #minutes, how long do washers run before turning off
DRYER_TIME = 0.5 #minutes, how long do dryers run before turning off
TICK_RATE = 4 #seconds, how many seconds to pause between updating the system
MACHINE_START_CHANCE = 0.1 #Random number from 0-1 is generated each tick.
                           # If the num < MACHINE_START_CHANCE, then the machine'
                           # Will start runnin. This must be tuned based on TICK_RATE

expiration_time = {}

def get_expiration_time(id):
    return expiration_time[id]

def set_expiration_time(id, type):
    if(type == "washer"):
        expiration_time[id] = time.time() + (WASHER_TIME * 60)
    else:
        expiration_time[id] = time.time() + (DRYER_TIME * 60)

ticks = 0
while(True):
    print("Tick:" + str(ticks))
    ticks += 1
    with open("machines.json", 'r') as f:
        dict = json.load(f)
        updated = False
        for machine in dict:
            id = machine["id"]

            #machine is running
            if(machine["running"] == True):
                #The machine is ready to expire
                if(time.time() > get_expiration_time(id)):
                    del expiration_time[id]
                    print(machine["name"] + " stopped!")
                    machine["running"] = False
                    updated = True
            #The machine isn't running
            else:
                #The machine randomly started itself :p
                if(random.random() < MACHINE_START_CHANCE):
                    set_expiration_time(id, machine["type"])
                    machine["running"] = True
                    print(machine["name"] + " started!")
                    updated = True

    #The dict has been updated, we need to update the file
    if(updated):
        with open('machines.json', 'w') as json_file:
            json.dump(dict, json_file)

    #Now sleep. We only need to update every so often.
    time.sleep(TICK_RATE)
