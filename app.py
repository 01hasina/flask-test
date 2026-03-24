from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World from my first project on Flask, Hasina is in the place!UPDATED"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)