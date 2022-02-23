from pydantic import BaseModel


class MathQuery(BaseModel):
    a: int
    b: int