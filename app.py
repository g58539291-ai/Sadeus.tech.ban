import os
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY", "dev-only-change-me")
SITE_PASSWORD = os.environ.get("SITE_PASSWORD", "")

@app.route("/")
def index():
    return render_template("login.html")

@app.post("/login")
def login():
    password = request.form.get("password", "")

    if SITE_PASSWORD and password == SITE_PASSWORD:
        session["authenticated"] = True
        return redirect("/domination")

    return redirect("/")

@app.route("/domination")
def domination():
    return render_template("domination.html")

@app.route("/report")
def report():
    if not session.get("authenticated"):
        return redirect("/")
    return render_template("report.html")
def report():
    return render_template("report.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)
