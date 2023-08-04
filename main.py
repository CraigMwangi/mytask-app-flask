from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    login_required,
    logout_user,
    current_user,
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_ckeditor import CKEditor
from flask_bootstrap import Bootstrap
import os
import smtplib
from forms import AddTask
from sqlalchemy.orm import relationship
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///todo.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
app.config["SECRET_KEY"] = "secret"
ckeditor = CKEditor(app)
Bootstrap(app)


class Tasks(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    # Create Foreign Key, "tasks.id" refers to the table-name of Tasks.
    task = db.Column(db.String(250), nullable=False)
    priority = db.Column(db.String(250), nullable=False)
    category = db.Column(db.String(250), nullable=False)
    deadline = db.Column(db.Date(), nullable=False)
    date_added = db.Column(db.Date(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)


with app.app_context():
    db.create_all()

@app.route("/add", methods=["GET", "POST"])
def add_task():
    form = AddTask()
    if request.method == "POST":
        if form.validate_on_submit():
            date = datetime.now().date()
            print(date)
            new_task = Tasks(
                task=form.add_task.data,
                priority=form.task_priority.data,
                category=form.category.data,
                deadline=form.deadline.data,
                date_added=date,
                completed=False,
            )
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for("tasks"))
    return render_template("addtasks.html", form=form)


@app.route("/", methods=["GET", "POST"])
def tasks():
    tasks = Tasks.query.filter_by(completed=False).all()
    return render_template("index.html", tasks=tasks)


@app.route("/completed_tasks", methods=["GET", "POST"])
def completed_tasks():
    tasks = Tasks.query.filter_by(completed=True).all()
    return render_template("completed_tasks.html", tasks=tasks)


@app.route("/mark_completed/<int:task_id>", methods=["POST"])
def mark_completed(task_id):
    task = Tasks.query.get(task_id)
    task.completed = True
    db.session.commit()
    return redirect(url_for("tasks"))


@app.route("/delete_task/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    task = Tasks.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("tasks"))


if __name__ == "__main__":
    app.run(debug=True)
