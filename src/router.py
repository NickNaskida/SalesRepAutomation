import os
from pathlib import Path

import gspread
from fastapi import APIRouter, Response

from src.schemas import DBItem

SRC_DIR = Path(__file__).resolve().parent

router = APIRouter()
gc = gspread.service_account(
    filename=os.path.join(SRC_DIR, "service_account.json")
)
db_sheet_url = "https://docs.google.com/spreadsheets/d/17-xMFhMnay54HI_gvdT2-IUU8YrqIAUzq6-GQKC0JWQ/edit#gid=0"


@router.post("/add_to_database", status_code=201)
def add_to_database(item: DBItem):
    db_sheet = gc.open_by_url(db_sheet_url)
    worksheet = db_sheet.get_worksheet(0)
    worksheet.append_row([item.id, item.amount, item.sales_rep])

    return Response(status_code=201)


@router.get("/calculate_leaderboard")
def calculate_leaderboard():
    pass
