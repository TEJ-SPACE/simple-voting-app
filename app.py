from flask import Flask, request, render_template

app = Flask(__name__)

votes = {
    "Option A": 0,
    "Option B": 0,
    "Option C": 0
         }

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        selected_option = request.form.get("vote")
        if selected_option in votes:
            votes[selected_option] += 1
    return render_template("index.html", options=votes.keys())

@app.route("/results")
def results():
    return render_template("results.html", votes=votes)

@app.route("/reset", methods=["POST"])
def reset_votes():
    global votes
    votes = {option:0 for option in votes}
    return render_template("results.html", votes=votes)

if __name__ == "__main__":
    app.run(debug=True)
