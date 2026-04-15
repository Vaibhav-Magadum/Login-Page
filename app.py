import os
import secrets

from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", secrets.token_hex(16))

# In-memory user store for demonstration purposes
users = {
    "admin": generate_password_hash("admin123"),
}


@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if not username or not password:
            flash("Please fill in all fields.", "error")
            return render_template("login.html")

        if username in users and check_password_hash(users[username], password):
            session["username"] = username
            flash("Login successful!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password.", "error")

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        if not username or not password or not confirm_password:
            flash("Please fill in all fields.", "error")
            return render_template("register.html")

        if password != confirm_password:
            flash("Passwords do not match.", "error")
            return render_template("register.html")

        if username in users:
            flash("Username already exists.", "error")
            return render_template("register.html")

        users[username] = generate_password_hash(password)
        flash("Registration successful! Please log in.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        flash("Please log in first.", "error")
        return redirect(url_for("login"))
    return render_template("dashboard.html", username=session["username"])


@app.route("/logout")
def logout():
    session.pop("username", None)
    flash("You have been logged out.", "success")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG", "false").lower() == "true")
