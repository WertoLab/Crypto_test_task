from datetime import datetime


class TransactionModel:
    __block_number: str
    __receiver: str
    __sender: str
    __value: str
    __timestep: int

    def __init__(self, block_number: str, receiver: str, sender: str, value: str, timestep: int):
        self.__block_number = block_number
        self.__receiver = receiver
        self.__sender = sender
        self.__value = value
        self.__timestep = timestep

    def get_block_number(self) -> int:
        return int(self.__block_number, 16)

    def get_receiver(self) -> str:
        return str(int(self.__receiver, 16))

    def get_sender(self) -> str:
        return str(int(self.__sender, 16))

    def get_value(self) -> float:
        return float(int(self.__value, 16))/10**18

    def get_timestep(self) -> datetime:
        return datetime.fromtimestamp(self.__timestep)
