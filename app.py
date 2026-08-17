from flask import Flask, render_template, request, redirect
from datetime import datetime
import socket
import os
import sqlite3

app = Flask(__name__)

DATABASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "expenses.db"
)


def get_db():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_db()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


@app.route("/")
def home():

    connection = get_db()

    expenses = connection.execute("""
        SELECT * FROM expenses
        ORDER BY id DESC
    """).fetchall()

    total = connection.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM expenses
    """).fetchone()[0]

    connection.close()

    return render_template(
        "index.html",
        expenses=expenses,
        total=total,
        hostname=socket.gethostname(),
        environment=os.getenv("ENVIRONMENT", "Development"),
        current_time=datetime.now()
    )


@app.route("/add", methods=["POST"])
def add_expense():

    description = request.form.get("description")
    amount = request.form.get("amount")
    category = request.form.get("category")

    if description and amount and category:

        try:
            amount = float(amount)

            connection = get_db()

            connection.execute("""
                INSERT INTO expenses
                (description, amount, category)
                VALUES (?, ?, ?)
            """, (description, amount, category))

            connection.commit()
            connection.close()

        except ValueError:
            pass

    return redirect("/")


@app.route("/delete/<int:index>")
def delete_expense(index):

    connection = get_db()

    connection.execute(
        "DELETE FROM expenses WHERE id = ?",
        (index,)
    )

    connection.commit()
    connection.close()

    return redirect("/")


@app.route("/health")
def health():

    return {
        "status": "UP",
        "application": "Expense Tracker",
        "environment": os.getenv(
            "ENVIRONMENT",
            "Development"
        )
    }

if __name__ == "__main__":

    init_db()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )