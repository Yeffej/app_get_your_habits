from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/habits")
def get_all_habits():
    habits = {
        "length": 3,
        "list": ["habit 1", "habit 2", "habit 3"]
    }
    return jsonify(habits)

if __name__ == '__main__':
    app.run(debug=True)