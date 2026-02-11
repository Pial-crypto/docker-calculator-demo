from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def health():
    return "Version updated 🚀"



@app.route("/add")
def add():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    return jsonify(result=a + b)

@app.route("/sub")
def sub():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    return jsonify(result=a - b)

@app.route("/mul")
def mul():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    return jsonify(result=a * b)

@app.route("/div")
def div():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 1))
    if b == 0:
        return jsonify(error="Division by zero"), 400
    return jsonify(result=a / b)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
