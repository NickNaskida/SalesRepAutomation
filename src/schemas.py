from pydantic import BaseModel


class DBItem(BaseModel):
    id: int = 1
    amount: int = 1000
    sales_rep: str = "Alice"


class Leaderboard(BaseModel):
    sales_team_total: str = "$1000"
    first_place: str = "Alice"
    second_place: str = "Bob"
