from typing import Any, Optional

from pydantic import BaseModel


class MathQuery(BaseModel):
    a: int
    b: int

class MessageResponse(BaseModel):

    def __init__(self, msg: str, code: int, **data: Any):
        super().__init__(**data)
        self.msg = msg
        self.code = code

    msg: Optional[str] = None
    code: Optional[int] = 0

class ValueResponse(BaseModel):
    def __init__(self, msg: int, code: int, **data: Any):
        super().__init__(**data)
        self.msg = msg
        self.code = code
    msg: Optional[int] = 0
    code: Optional[int] = 0

class MathResponse(BaseModel):
    def __init__(self, query: MathQuery, result: int, err : str, **data: Any):
        super().__init__(**data)
        self.query = query
        self.result = result
        self.err = err
    query: Optional[MathQuery] = None
    result: Optional[int] = 0