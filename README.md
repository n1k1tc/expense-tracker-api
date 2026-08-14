# Expense Tracker API

A simple REST API for managing expenses, built using FastAPI, SQLAlchemy, and SQLite.

## Features

- Create a new expense
- View all expenses
- View a single expense
- Update an expense
- Delete an expense
- SQLite database for storing expenses
- Interactive API documentation using Swagger UI

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Check if the API is running |
| GET | `/expenses` | Get all expenses |
| POST | `/expenses` | Create an expense |
| GET | `/expenses/{expense_id}` | Get a specific expense |
| PUT | `/expenses/{expense_id}` | Update an expense |
| DELETE | `/expenses/{expense_id}` | Delete an expense |

## Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/n1k1tc/expense-tracker-api.git
cd expense-tracker-api