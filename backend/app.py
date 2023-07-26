from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, World!"})


@app.route("/prompt", methods=["POST"])
def post():
    data = request.get_json()
    return jsonify({"data": data})
