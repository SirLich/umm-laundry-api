from flask import render_template
from flask import send_from_directory
from flask import jsonify
from flask import make_response
from app import app
import json

# EXAMPLE MACHINE JSON
# {
# 	"id": "c4499d38-f937-11e9-8874-902b34113095",
# 	"name": "chummy-beige-dollar",
# 	"type": "washer",
# 	"running": false,
# 	"status": "normal"
# 	"room_id": "gay"
# }

# Local list of machines. This list is generated based on the updates to /update_machine
# A fresh instantiation of the app will have no machines. Machines can be added manually by pushing an "I'm awake" request.
# Otherwise, machines will be added as they change state.
machines = {}

# Home route, used to provide information about the API
@app.route('/')
def home():
    m = """
    Welcome to the laundry API! \n
    The following routes are available: \n\n
    /rooms \n
    /machines \n
    /rooms/{room}/machines \n
    /machines/{machine} \n
    /update_machine
    """

    response = make_response(m)
    response.headers["content-type"] = "text/plain"
    return response

# Returns static list of rooms. This list can be edited as needed in the config
@app.route('/rooms')
def get_rooms():
    return jsonify(app.config['ROOMS'])

# Returns all machines that the system knows about.
@app.route('/machines')
def get_machines():
    return jsonify(machines)

# Returns machines, sorted by room.
@app.route("/rooms/<room>/machines")
def get_room(room):
    output_dict = [x for x in machines if x['room_id'] == room]
    return jsonify(output_dict)

# Returns a specific machine.
@app.route('/machines/<machine>')
def get_machine(machine):
    output_dict = [x for x in machines if x['id'] == machine]
    return jsonify(output_dict)

# Update the status of new machines. 
# New machines can be "added" by simply bringing them online, and setting up IFTTT rules for it.
@app.route('/update_machine', methods=['POST'])
def update_machine():
    if request.method == 'POST':
        try:
            raw = request.json
            id = raw["id"]
            machines[id] = raw
            return '', 200
        except:
            "Something went wrong"
    else:
        abort(400)