from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game1")
def game1():
    return render_template("game1.html")

@app.route("/game2")
def game2():
    return render_template("game2.html")

@app.route("/game3")
def game3():
    return render_template("game3.html")

@app.route("/game4")
def game4():
    return render_template("game4.html")

@app.route("/game5")
def game5():
    return render_template("game5.html")

@app.route("/game6")
def game6():
    return render_template("game6.html")

@app.route("/centralised_scoreboard")
def centralised_scoreboard():
    return render_template("centralised_scoreboard.html")  # Adjust as necessary

if __name__ == "__main__":
    app.run(debug=True)
