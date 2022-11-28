from flask import Flask, make_response, render_template, request
from database import Database

app = Flask(__name__)
db = Database("database.json")

@app.route("/api/add_score", methods=["POST"])
def add_score():
    username = request.json["username"]
    score = request.json["score"]
    db.add_score(username, score)
    return make_response("ok")

@app.route("/api/get_score", methods=["GET"])
def get_score():
    username = request.args.get("username")
    scores = {}
    try:
        scores = db.get_score(username)
    except KeyError:
        pass

    return make_response(scores)

if __name__ == "__main__":
    app.run(debug=True)

