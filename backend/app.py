from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
# Allow requests only from example.com and localhost:3000
# CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})
CORS(app)


@app.route("/", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, World!"})


@app.route("/prompt", methods=["POST"])
def post():
    data = request.get_json()
    return jsonify({"data": data})


if __name__ == "__main__":
    app.run(debug=True)
