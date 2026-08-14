from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import engine, Base, SessionLocal
from . import models, schemas, crud


Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Expense Tracker API is running!"}


@app.post("/expenses")
def create_expense(
    expense: schemas.ExpenseCreate,
    db: Session = Depends(get_db)
):
    return crud.create_expense(db, expense)


@app.get("/expenses")
def get_expenses(db: Session = Depends(get_db)):
    return crud.get_expenses(db)


@app.get("/expenses/{expense_id}")
def get_expense(
    expense_id: int,
    db: Session = Depends(get_db)
):
    expense = crud.get_expense(db, expense_id)

    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")

    return expense


@app.put("/expenses/{expense_id}")
def update_expense(
    expense_id: int,
    expense: schemas.ExpenseCreate,
    db: Session = Depends(get_db)
):
    updated_expense = crud.update_expense(
        db,
        expense_id,
        expense
    )

    if updated_expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")

    return updated_expense


@app.delete("/expenses/{expense_id}")
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db)
):
    deleted_expense = crud.delete_expense(db, expense_id)

    if deleted_expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")

    return {
        "message": "Expense deleted successfully"
    }