import os
from pathlib import Path

import gspread
from fastapi import APIRouter, Response

from src.schemas import DBItem, Leaderboard

SRC_DIR = Path(__file__).resolve().parent

router = APIRouter()
gc = gspread.service_account(
    filename=os.path.join(SRC_DIR, "service_account.json")
)
db_sheet_url = "https://docs.google.com/spreadsheets/d/17-xMFhMnay54HI_gvdT2-IUU8YrqIAUzq6-GQKC0JWQ/edit#gid=0"


@router.post("/add_to_database", status_code=201)
def add_to_database(item: DBItem) -> Response:
    """Add a new item to the google sheet database."""
    db_sheet = gc.open_by_url(db_sheet_url)
    worksheet = db_sheet.get_worksheet(0)
    worksheet.append_row([item.id, item.amount, item.sales_rep])

    return Response(status_code=201)


@router.get("/calculate_leaderboard")
def calculate_leaderboard() -> Leaderboard:
    """
    Calculate the leaderboard for the sales team

    :return: Leaderboard with detailed info
    """
    db_sheet = gc.open_by_url(db_sheet_url)
    worksheet = db_sheet.get_worksheet(0)
    data = worksheet.get_all_values()

    # Calculate the total sales for each sales rep
    sales_rep_totals = {}

    for row in data[1:]:
        sales_rep_totals[row[2]] = sales_rep_totals.get(row[2], 0) + int(row[1])

    sorted_sales_rep_totals = sorted(sales_rep_totals.items(), key=lambda x: x[1], reverse=True)

    leaderboard = Leaderboard(
        sales_team_total=f"${sum([int(row[1]) for row in data[1:]])}",  # Sum the total sales
        first_place=f"{sorted_sales_rep_totals[0][0]} - ${sorted_sales_rep_totals[0][1]}",
        second_place=f"{sorted_sales_rep_totals[1][0]} - ${sorted_sales_rep_totals[1][1]}",
    )

    return leaderboard
