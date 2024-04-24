from typing import List

from pydantic import BaseModel
from datetime import datetime


class TransactionDTO(BaseModel):
    transaction_time: datetime
    block_number: int
    receiver: str
    sender: str
    transaction_value: float

    @classmethod
    def get_transaction(cls, transaction_time: datetime, block_number: int, receiver: str, sender: str,
                        transaction_value: float) -> "TransactionDTO":
        return cls(transaction_time=transaction_time, block_number=block_number, receiver=receiver, sender=sender,
                   transaction_value=transaction_value)


class ResponseDTO(BaseModel):
    transactions_amount: int
    transactions: List[List[TransactionDTO]]

    @classmethod
    def get_response(cls, transactions_amount: int, transactions:list) -> "ResponseDTO":
        return cls(transactions_amount=transactions_amount, transactions=transactions)