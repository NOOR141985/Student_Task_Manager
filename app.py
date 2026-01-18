from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary in-memory storage (later we’ll use SQLite)
tasks = []

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title")
    if title:
        tasks.append(title)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
    
