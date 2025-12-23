from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(
        service="service-b",
        status="running"
    )

app.run(host="0.0.0.0", port=5001)
