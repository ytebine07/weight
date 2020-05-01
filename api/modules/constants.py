import os


class Constants:

    FITBIT_USER_ID = os.getenv("_FITBIT_USER_ID")
    FITBIT_AUTHORIZATION = os.getenv("_FITBIT_AUTHORIZATION")

    FITBIT_WEIGHT_API_URL = (
        f"https://api.fitbit.com/1/user/{FITBIT_USER_ID}/body/log/weight.json"
    )
    FITBIT_FAT_API_URL = (
        f"https://api.fitbit.com/1/user/{FITBIT_USER_ID}/body/log/fat.json"
    )
