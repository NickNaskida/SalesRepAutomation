from pydantic import BaseModel


class DBItem(BaseModel):
    id: int = 1
    amount: int = 1000
    sales_rep: str = "Alice"
