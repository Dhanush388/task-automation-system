print("Flask app")

from flask import Flask, render_template, request, redirect
from app.services.auth_service import login_user, register_user
from app.services.task_service import add_task, view_tasks, complete_task

app = Flask(__name__)

current_user = None


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    global current_user

    username = request.form["username"]
    password = request.form["password"]

    user_id = login_user(username, password)

    if user_id:
        current_user = user_id
        return redirect("/dashboard")

    return "Invalid login"


@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]

    register_user(username, password)
    return redirect("/")


@app.route("/dashboard")
def dashboard():
    if not current_user:
        return redirect("/")

    tasks = view_tasks(current_user)
    return render_template("dashboard.html", tasks=tasks)


@app.route("/add_task", methods=["POST"])
def add():
    title = request.form["title"]
    desc = request.form["desc"]
    deadline = request.form["deadline"]
    priority = request.form["priority"]

    add_task(current_user, title, desc, deadline, priority)

    return redirect("/dashboard")


@app.route("/complete/<int:task_id>")
def complete(task_id):
    complete_task(task_id)
    return redirect("/dashboard")


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001,debug=True)