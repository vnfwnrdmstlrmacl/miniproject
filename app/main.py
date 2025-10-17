# 간단한 Flask 웹 애플리케이션 예제
from flask import Flask, jsonify, request

app = Flask(__name__)

def add(a, b):
    return a + b

@app.route("/", methods=["GET"])
def hello():
    return jsonify({"message": "Hello from miniproject!"})

@app.route("/add", methods=["GET"])
def add_route():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return jsonify({"result": add(a, b)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

