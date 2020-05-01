import decimal
import datetime


class Body:
    def __init__(self, weight: decimal, fat: decimal, timestamp: datetime):
        self.weight: decimal = weight
        self.fat: decimal = fat
        self.timestamp: datetime = timestamp
