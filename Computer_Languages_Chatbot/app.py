from flask import Flask, render_template, request, jsonify
from chatbot_data import get_reply

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = str(data.get("message", "")).strip()
    if not message:
        return jsonify({"reply": "Please type a question first."})
    return jsonify({"reply": get_reply(message)})

if __name__ == "__main__":
    app.run(debug=True)
