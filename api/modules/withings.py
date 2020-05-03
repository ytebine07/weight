import os
import requests
import decimal
import json
from datetime import datetime, timedelta, timezone

from modules.body import Body
from modules.constants import Constants


class Meas:
    JST = timezone(timedelta(hours=+9), "JST")

    def __init__(self, value: decimal, registerd_at: datetime):
        self.value: decimal = value
        self.registered_at: datetime = registerd_at

    @staticmethod
    def toValue(response) -> decimal:
        if not response["body"]["measuregrps"]:
            return None

        value = response["body"]["measuregrps"][0]["measures"][0]["value"]
        decimal.getcontext().prec = 3
        decimal_value = decimal.Decimal(str(value)) / decimal.Decimal(1000)
        return decimal_value

    @staticmethod
    def toRegisteredAt(response) -> datetime:
        if not response["body"]["measuregrps"]:
            return None

        registered_at_unixtime = response["body"]["measuregrps"][0]["date"]
        registered_at_datetime = datetime.fromtimestamp(
            registered_at_unixtime, Meas.JST
        )
        return registered_at_datetime

    @staticmethod
    def startdate() -> int:
        return Meas.enddate() - Constants.WITHINGS_MEASURE_TERM_SECONDS

    @staticmethod
    def enddate() -> int:
        return int(datetime.now().strftime("%s"))


class Token:
    def __init__(self):
        super().__init__()

        # 保存してあるのは有効期限切れてるかもなので、先にリフレッシュする
        self.refresh()

        with open(Constants.WITHINGS_TOKEN_FILE_PATH, mode="r") as f:
            self.__json = json.loads(f.read())
        self.access_token = self.__json["access_token"]

    def refresh(self):

        credentials = {}
        if os.path.exists(Constants.WITHINGS_TOKEN_FILE_PATH):
            with open(Constants.WITHINGS_TOKEN_FILE_PATH, mode="r") as f:
                credentials = json.loads(f.read())
        else:
            credentials["refresh_token"] = os.getenv("_WITHINGS_INIT_REFRESH_TOKEN")

        params = {
            "grant_type": "refresh_token",
            "client_id": Constants.WITHINGS_CLIENT_ID,
            "client_secret": Constants.WITHINGS_CONS_SECRET,
            "refresh_token": credentials["refresh_token"],
        }
        response = requests.post(Constants.WITHINGS_TOKEN_API_URL, data=params).json()
        obj = {
            "access_token": response["access_token"],
            "refresh_token": response["refresh_token"],
        }

        with open(Constants.WITHINGS_TOKEN_FILE_PATH, mode="w") as f:
            f.write(json.dumps(obj, indent=2))


class Withings:

    MEASTYPYE_WEIGHT_KG = 1
    MEASTYPE_PAT_PERCENTAGE = 6

    def __init__(self):
        super().__init__()
        self.__token = Token()

    def fetch_last_body(self) -> Body:
        weight = self.__get_weight()
        fat = self.__get_fat_percentage()
        return Body(weight=weight.value, fat=fat.value, timestamp=weight.registered_at)

    def __get_weight(self) -> Meas:
        return self.__request_api(self.MEASTYPYE_WEIGHT_KG)

    def __get_fat_percentage(self) -> Meas:
        return self.__request_api(self.MEASTYPE_PAT_PERCENTAGE)

    def __request_api(self, meastype: int) -> Meas:
        params = {
            "action": "getmeas",
            "access_token": self.__token.access_token,
            "meastype": meastype,
            "category": 1,
            "startdate": Meas.startdate(),
            "enddate": Meas.enddate(),
            "offset": 0,
        }
        response = requests.get(
            Constants.WITHINGS_MEASURE_API_URL, params=params
        ).json()
        return Meas(Meas.toValue(response), Meas.toRegisteredAt(response))
