import os

from flask import Flask, jsonify, redirect, render_template, request, url_for

app = Flask(__name__)

expenses = []


@app.route("/")
def home():
    total = sum(expense["amount"] for expense in expenses)

    return render_template(
        "index.html",
        expenses=expenses,
        total=total,
        commit=os.getenv("RENDER_GIT_COMMIT", "local"),
    )


@app.route("/add", methods=["POST"])
def add_expense():
    description = request.form.get("description", "").strip()
    amount_text = request.form.get("amount", "").strip()
    paid_by = request.form.get("paid_by", "").strip()
    people_text = request.form.get("people", "").strip()

    if not description or not amount_text or not paid_by or not people_text:
        return "All fields are required.", 400

    try:
        amount = round(float(amount_text), 2)
        people = int(people_text)
    except ValueError:
        return "Amount must be a number and people must be a whole number.", 400

    if amount <= 0:
        return "Amount must be greater than 0.", 400

    if people < 1:
        return "Number of people must be at least 1.", 400

    share = round(amount / people, 2)

    expenses.append(
        {
            "description": description,
            "amount": amount,
            "paid_by": paid_by,
            "people": people,
            "share": share,
        }
    )

    return redirect(url_for("home"))


@app.route("/api/expenses")
def api_expenses():
    return jsonify(expenses)


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", 5000)),
        debug=True,
    )
