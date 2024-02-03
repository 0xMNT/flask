from flask import Flask, render_template

app = Flask(__name__)

counter = 0
    
def modify_counter(value):
    global counter
    counter += value
    return counter

@app.route("/")
def index():
    return render_template("index.html", counter=counter)

@app.route("/increase", methods=["POST"])
def increase():
    global counter
    return f"{modify_counter(1)}"

@app.route("/decrease", methods=["POST"])
def decrease():
    global counter
    return f"{modify_counter(-1) if counter >= 1 else counter}"

@app.route("/reset", methods=["POST"])
def reset():
    global counter
    counter = 0
    return f"{counter}"

if __name__ == "__main__":
    app.run(debug=True)
