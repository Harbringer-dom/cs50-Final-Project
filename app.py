from flask import Flask, render_template, request, redirect, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

import sqlite3

app = Flask(__name__)
app.secret_key = "dev"


def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def login_required(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


@app.route("/")
def dashboard():
    db = get_db()
    if "user_id" not in session:
        return redirect("/login")

    user_id = session["user_id"]

    # Monthly expense total
    total_expense = db.execute(
        """
        SELECT COALESCE(SUM(amount), 0)
        FROM expenses
        WHERE user_id = ?
        AND strftime('%Y-%m', date) = strftime('%Y-%m', 'now')
    """,
        (user_id,),
    ).fetchone()[0]

    # Study stats
    total_tasks = db.execute(
        """
        SELECT COUNT(*) FROM study_tasks2
        WHERE user_id = ?
    """,
        (user_id,),
    ).fetchone()[0]

    completed_tasks = db.execute(
        """
        SELECT COUNT(*) FROM study_tasks2
        WHERE user_id = ? AND completed = 1
    """,
        (user_id,),
    ).fetchone()[0]

    pending_tasks = total_tasks - completed_tasks

    # Category breakdown
    category_summary = db.execute(
        """
        SELECT category, SUM(amount) as total
        FROM expenses
        WHERE user_id = ? GROUP BY category ORDER BY total DESC
    """,
        (user_id,),
    ).fetchall()

    return render_template(
        "dashboard.html",
        total_expense=total_expense,
        total_tasks=total_tasks,
        completed_tasks=completed_tasks,
        pending_tasks=pending_tasks,
        category_summary=category_summary,
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if not username or not password:
            flash("Username and password required", "error")
            return redirect("/register")

        hash = generate_password_hash(password)

        db = get_db()
        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)",
                       (username, hash))
            db.commit()
            flash("Registration successful! Please login.", "success")
            return redirect("/login")
        except ValueError:
            flash("Username already exists. Choose another.", "error")
            return redirect("/register")

    return render_template("register.html")


# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            flash("Username and password required", "error")
            return redirect("/login")

        db = get_db()
        user = db.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()

        if user and check_password_hash(user["hash"], password):
            session["user_id"] = user["id"]
            flash(f"Welcome back, {username}!", "success")
            return redirect("/")

        flash("Invalid username or password", "error")
        return redirect("/login")

    return render_template("login.html")


# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/study", methods=["GET", "POST"])
@login_required
def study():
    user_id = session["user_id"]
    db = get_db()

    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        due_date = request.form.get("due_date")

        if not title:
            flash("Task title is required", "error")
            return redirect("/study")

        if not due_date:
            flash("Due date is required", "error")
            return redirect("/study")

        sql = "INSERT INTO study_tasks2 (user_id, title, description, due_date) VALUES (?, ?, ?, ?)"
        db.execute(sql, (user_id, title, description, due_date))
        db.commit()
        flash("Task added successfully!", "success")

        return redirect("/study")

    tasks = db.execute(
        "SELECT * FROM study_tasks2 WHERE user_id = ? "
        "ORDER BY completed, due_date",
        (user_id,),
    ).fetchall()

    return render_template("study.html", tasks=tasks)


@app.route("/delete_task/<int:task_id>")
@login_required
def delete_task(task_id):
    db = get_db()
    db.execute(
        "DELETE FROM study_tasks2 WHERE id = ? AND user_id = ?",
        (task_id, session["user_id"]),
    )
    db.commit()
    flash("Task deleted successfully", "success")
    return redirect("/study")


@app.route("/toggle_task/<int:task_id>")
@login_required
def toggle_task(task_id):
    db = get_db()
    user_id = session["user_id"]

    task = db.execute(
        "SELECT completed FROM study_tasks2 WHERE id = ? AND user_id = ?",
        (task_id, user_id),
    ).fetchone()

    if task is None:
        return "Task not found", 404

    new_status = 0 if task["completed"] else 1

    db.execute(
        "UPDATE study_tasks2 SET completed = ? WHERE id = ? AND user_id = ?",
        (new_status, task_id, user_id),
    )
    db.commit()

    return redirect("/study")


@app.route("/expenses", methods=["GET", "POST"])
@login_required
def expenses():
    user_id = session["user_id"]
    db = get_db()

    if request.method == "POST":
        category = request.form.get("category")
        amount = request.form.get("amount")
        date = request.form.get("date")
        note = request.form.get("note")

        if not category or not amount or not date:
            flash("Category, amount, and date are required", "error")
            return redirect("/expenses")

        try:
            amount = float(amount)
            if amount <= 0:
                flash("Amount must be greater than zero", "error")
                return redirect("/expenses")
        except ValueError:
            flash("Amount must be a valid number", "error")
            return redirect("/expenses")

        db.execute(
            "INSERT INTO expenses (user_id, category, amount,date,note)"
            " VALUES (?, ?, ?,?,?)",
            (user_id, category, amount, date, note),
        )
        db.commit()
        flash(f"Expense of ₹{amount} added to {category}", "success")

        return redirect("/expenses")

    # GET request - handle category filter
    category_filter = request.args.get("category")
    if category_filter:
        expenses_list = db.execute(
            "SELECT id, category, amount, date, note "
            "FROM expenses WHERE user_id = ? AND category = ? "
            "ORDER BY date DESC",
            (user_id, category_filter),
        ).fetchall()

        total = db.execute("SELECT SUM(amount) FROM expenses "
                           "WHERE user_id = ? AND category = ?",
                           (user_id, category_filter)).fetchone()[0]
    else:
        expenses_list = db.execute(
            "SELECT id, category, amount, date, note "
            "FROM expenses WHERE user_id = ? ORDER BY date DESC",
            (user_id,),
        ).fetchall()

        total = db.execute(
            "SELECT SUM(amount) FROM expenses WHERE user_id = ?", (user_id,)
        ).fetchone()[0]

    if total is None:
        total = 0

    return render_template(
        "expenses.html",
        expenses=expenses_list,
        total=total,
        category_filter=category_filter,
    )


@app.route("/delete_expense/<int:expense_id>")
@login_required
def delete_expense(expense_id):
    db = get_db()
    db.execute(
        "DELETE FROM expenses WHERE id = ? AND user_id = ?",
        (expense_id, session["user_id"]),
    )
    db.commit()
    flash("Expense deleted successfully", "success")
    return redirect("/expenses")


if __name__ == "__main__":
    import os

    # Production: Use gunicorn (via Procfile)
    # Development: Use debug mode
    debug_mode = os.environ.get("FLASK_ENV") != "production"
    app.run(debug=debug_mode)
