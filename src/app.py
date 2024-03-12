from flask import Flask
app = Flask(__name__)

@app.route("/ping")
def pong():
    return "pong"

@app.route("/factorial")
def factorial():
    res = 1
    for n in range(1, 11):
        res *= n
    return str(res)

if __name__ == "__main__":
    app.run()