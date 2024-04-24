from pydantic import BaseModel


class RequestDTO(BaseModel):
    datetime: str
    integer: int
    entities_limit: int
    offset: int

