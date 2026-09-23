import pytest

from app import app, expenses


@pytest.fixture
def client():
    app.config["TESTING"] = True
    expenses.clear()

    with app.test_client() as test_client:
        yield test_client

    expenses.clear()


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json == {"status": "ok"}


def test_add_expense(client):
    response = client.post(
        "/add",
        data={
            "description": "Dinner",
            "amount": "900",
            "paid_by": "Shivani",
            "people": "3",
        },
    )

    assert response.status_code == 302
    assert len(expenses) == 1
    assert expenses[0]["description"] == "Dinner"
    assert expenses[0]["amount"] == 900
    assert expenses[0]["share"] == 300


def test_invalid_expense_rejected(client):
    response = client.post(
        "/add",
        data={
            "description": "Dinner",
            "amount": "-100",
            "paid_by": "Shivani",
            "people": "3",
        },
    )

    assert response.status_code == 400
    assert len(expenses) == 0
