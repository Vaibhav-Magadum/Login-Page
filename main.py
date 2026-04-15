from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Hardcoded login credentials (for demo only)
USERNAME = "admin"
PASSWORD = "1234"

login_page = """
<!doctype html>
<html>
<head>
    <title>Login Page</title>
</head>
<body>
    <h2>Login</h2>
    <form method="POST">
        <label>Username:</label><br>
        <input type="text" name="username" required><br><br>

        <label>Password:</label><br>
        <input type="password" name="password" required><br><br>

        <button type="submit">Login</button>
    </form>

    <p style="color:red;">{{ error }}</p>
</body>
</html>
"""

success_page = """
<!doctype html>
<html>
<head>
    <title>Welcome</title>
</head>
<body>
    <h2>Login Successful 🎉</h2>
    <p>Welcome, admin!</p>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def login():
    error = ""

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD:
            return redirect(url_for("success"))
        else:
            error = "Invalid username or password!"

    return render_template_string(login_page, error=error)


@app.route("/success")
def success():
    return render_template_string(success_page)


if __name__ == "__main__":
    app.run(debug=True)
