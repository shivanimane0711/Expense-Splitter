# Expense Splitter – Shared Expense Management System

## 1. Project Description

Expense Splitter is a Flask-based web application for managing shared expenses. Users can enter an expense description, amount, payer and number of people. The application calculates the equal share per person and displays the expenses.

This project demonstrates Git, automated testing, linting, Docker containerization, CI/CD using GitHub Actions and deployment using Render.

## 2. Features

- Add shared expenses
- Calculate equal share per person
- Display total expenses
- Input validation
- JSON API for expenses
- Health check endpoint
- Automated testing using pytest
- Code linting using flake8
- Docker containerization
- GitHub Actions CI/CD
- Deployment on Render

## 3. Technologies Used

- Python 3.12
- Flask
- pytest
- flake8
- Docker
- GitHub
- GitHub Actions
- Render

## 4. Project Structure

```text
Expense-Splitter/
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── templates/
│   └── index.html
├── .dockerignore
├── .gitignore
├── Dockerfile
├── app.py
├── requirements.txt
├── test_app.py
└── README.md
```

## 5. Application Routes

| Route | Method | Purpose |
|---|---|---|
| `/` | GET | Displays the Expense Splitter home page |
| `/add` | POST | Adds a new expense |
| `/api/expenses` | GET | Returns expenses in JSON format |
| `/health` | GET | Checks application health |

## 6. Run Locally

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open the application in a browser:

http://localhost:5000

## 7. Run Tests

Run the automated tests using:

```bash
pytest -v
```

## 8. Run Lint

Run flake8 using:

```bash
flake8 --max-line-length=100 app.py test_app.py
```

## 9. Run with Docker

Build the Docker image:

```bash
docker build -t expense-splitter .
```

Run the Docker container:

```bash
docker run -d --name expense-splitter-container -p 5000:5000 expense-splitter
```

Open the application:

http://localhost:5000

Health check:

http://localhost:5000/health

## 10. CI/CD Pipeline

GitHub Actions is used to automate the project workflow.

The pipeline performs:

1. Code checkout
2. Python setup
3. Dependency installation
4. Flake8 linting
5. Automated testing using pytest
6. Docker image build
7. Docker container smoke test
8. Deployment to Render after a successful build on the main branch

The deployment step uses a Render Deploy Hook stored securely in GitHub Actions Secrets.

## 11. Deployment

The application is deployed on Render.

The application uses the `RENDER_GIT_COMMIT` environment variable to display the deployed Git commit ID in the application footer.

The `/health` endpoint is used to verify that the deployed application is running correctly.

## 12. Project Links

### GitHub Repository

https://github.com/shivanimane0711/Expense-Splitter

### GitHub Actions

https://github.com/shivanimane0711/Expense-Splitter/actions

### Live Application
https://expense-splitter-1-aoop.onrender.com