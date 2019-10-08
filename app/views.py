from flask import render_template
from flask import send_from_directory
from flask import jsonify
from flask import make_response
from app import app
import json

@app.route('/')
def home():
    m = """
    Welcome to the laundry API! \n
    The following routes are available: \n\n
    /rooms \n
    /machines \n
    /rooms/{room}/machines \n
    /machines/{machine} \n
    """

    response = make_response(m)
    response.headers["content-type"] = "text/plain"
    return response

@app.route('/rooms')
def get_rooms():
    return send_from_directory(app.config['STATIC_FOLDER'], "rooms.json")

@app.route('/machines')
def get_machines():
    return send_from_directory(app.config['STATIC_FOLDER'], "machines.json")

@app.route("/rooms/<room>/machines")
def get_room(room):
    with open(app.config['STATIC_FOLDER'] + "/machines.json", 'r') as f:
        input_dict = json.load(f)

    output_dict = [x for x in input_dict if x['room_id'] == room]

    return jsonify(output_dict)

@app.route('/machines/<machine>')
def get_machine(machine):
    with open(app.config['STATIC_FOLDER'] + "/machines.json", 'r') as f:
        input_dict = json.load(f)

    output_dict = [x for x in input_dict if x['id'] == machine]
    return jsonify(output_dict)
