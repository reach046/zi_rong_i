from flask import Flask, request, jsonify
import random
import string

app = Flask(__name__)

rooms = {}

def make_code():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))


@app.route("/create", methods=["POST"])
def create_room():

    data = request.json
    host_ip = data["host_ip"]

    code = make_code()

    rooms[code] = host_ip

    return jsonify({
        "room_code": code
    })


@app.route("/join", methods=["POST"])
def join_room():

    data = request.json
    code = data["room_code"]

    if code in rooms:
        return jsonify({
            "host_ip": rooms[code]
        })
    else:
        return jsonify({
            "error": "Room not found"
        })


app.run(host="0.0.0.0", port=5000)