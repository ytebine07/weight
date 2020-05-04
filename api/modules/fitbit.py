import requests
from modules.constants import Constants
from modules.body import Body


class Fitbit:
    def __init__(self):
        pass

    def get_fat(self) -> str:
        headers = {"Authorization": Constants.FITBIT_AUTHORIZATION}
        return requests.get(Constants.FITBIT_BODYLOG_API_URL, headers=headers,).json()

    def register(self, body: Body):
        self.__post_weight(body)
        self.__post_fat(body)

    def __post_weight(self, body: Body):
        headers = {"Authorization": Constants.FITBIT_AUTHORIZATION}
        payload = {
            "weight": body.weight,
            "date": body.timestamp.strftime("%Y-%m-%d"),
            "time": body.timestamp.strftime("%H:%M:%S"),
        }
        requests.post(
            Constants.FITBIT_WEIGHT_API_URL, data=payload, headers=headers,
        )
        # print(r.json())

    def __post_fat(self, body: Body):
        headers = {"Authorization": Constants.FITBIT_AUTHORIZATION}
        payload = {
            "fat": body.fat,
            "date": body.timestamp.strftime("%Y-%m-%d"),
            "time": body.timestamp.strftime("%H:%M:%S"),
        }

        requests.post(
            Constants.FITBIT_FAT_API_URL, data=payload, headers=headers,
        )
