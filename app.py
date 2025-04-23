from flask import Flask, render_template, request, jsonify
from tutor import get_feedback

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    score = data.get("score", 0)
    feedback = get_feedback(score)
    return jsonify({"feedback": feedback})

if __name__ == "__main__":
    app.run(debug=True)
