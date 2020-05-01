import requests

from modules.constants import Constants
from modules.body import Body


class Fitbit:
    def __init__(self, body: Body):
        self.__body: Body = body

    def save(self) -> bool:
        self.__post_weight()
        self.__post_fat()

    def __post_weight(self) -> str:
        headers = {"Authorization": Constants.FITBIT_AUTHORIZATION}
        payload = {
            "weight": self.__body.weight,
            "date": self.__body.timestamp.strftime("%Y-%m-%d"),
            "time": self.__body.timestamp.strftime("%H:%M:%S"),
        }
        r = requests.post(
            Constants.FITBIT_WEIGHT_API_URL, data=payload, headers=headers,
        )
        print(r.json())

    def __post_fat(self) -> str:
        headers = {"Authorization": Constants.FITBIT_AUTHORIZATION}
        payload = {
            "fat": self.__body.fat,
            "date": self.__body.timestamp.strftime("%Y-%m-%d"),
            "time": self.__body.timestamp.strftime("%H:%M:%S"),
        }

        r = requests.post(Constants.FITBIT_FAT_API_URL, data=payload, headers=headers,)
        print(r.json())
