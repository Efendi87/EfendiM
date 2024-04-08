from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/JC")
def home():
    return "Hello & Welcome to another Episode Of Top Gear"

@app.route("/H")
def index():
    return "Hammond you Idiot"

@app.route("/data")
def data():
    sample_data = {"Name" : "Richard Hammong", "Age" : 58, "Job" : "Car Journalist"}
    return jsonify(sample_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

