from flask import Flask, make_response, render_template, request
from database import Database

app = Flask(__name__)
db = Database("database.json")

@app.route("/api/add_score", methods=["POST"])
def home():
    username = request.form.get("username")
    score = request.form.get("score")
    db.add_score(username, score)
    return make_response("ok")

if __name__ == "__main__":
    app.run(debug=True)

