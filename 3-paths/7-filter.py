from fastapi import FastAPI, Query
from datetime import date
from typing import Optional, List


app = FastAPI()


@app.get("/transactions/")
async def get_transactions(
    account_id: int,
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None),
    min_amount: Optional[float] = Query(None),
    max_amount: Optional[float] = Query(None)
):
    transactions = filter_transactions(account_id, start_date, end_date, min_amount, max_amount)
    return {"transactions": transactions}


def filter_transactions(
    account_id: int,
    start_date: Optional[date],
    end_date: Optional[date],
    min_amount: Optional[float],
    max_amount: Optional[float]
) -> List[dict]:
    sample_transactions = [
        {"account_id": 1, "date": date(2023, 1, 1), "amount": 500},
        {"account_id": 1, "date": date(2023, 2, 15), "amount": 200},
        {"account_id": 2, "date": date(2023, 3, 10), "amount": 700}
    ]


    filtered = [t for t in sample_transactions if t["account_id"] == account_id]
    if start_date:
        filtered = [t for t in filtered if t["date"] >= start_date]
    if end_date:
        filtered = [t for t in filtered if t["date"] <= end_date]
    if min_amount:
        filtered = [t for t in filtered if t["amount"] >= min_amount]
    if max_amount:
        filtered = [t for t in filtered if t["amount"] <= max_amount]


    return filtered
