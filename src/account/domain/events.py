from dataclasses import dataclass


class Event:
    pass


@dataclass
class InsufficientCash(Event):
    account_number: str


@dataclass
class Withdrew(Event):
    account_number: str
    amount: int


@dataclass
class Deposited(Event):
    account_number: str
    amount: int
