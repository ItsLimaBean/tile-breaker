import json


class Database:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.scores = None

        self.read()

    def read(self):
        with open(self.filename, "r") as file:
            self.scores = json.load(file)

    def add_score(self, username, score):
        if username in self.scores:
            self.scores[username].append(score)
        else:
            self.scores[username] = [ score ]

        self.save()

    def get_score(self, username):
        if username is None:
            return self.scores
        else:
            return { username: self.scores[username] }

    def save(self):
        content = json.dumps(self.scores, indent=4)
        with open(self.filename, "w") as file:
            file.write(content)