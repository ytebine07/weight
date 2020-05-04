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

    WITHINGS_CLIENT_ID = os.getenv("_WITHINGS_CLIENT_ID")
    WITHINGS_CONS_SECRET = os.getenv("_WITHINGS_CONS_SECRET")
    WITHINGS_TOKEN_FILE_PATH = "/workspaces/weight/api/credentials/withings.json"
    WITHINGS_TOKEN_API_URL = "https://account.withings.com/oauth2/token"
    WITHINGS_MEASURE_API_URL = "https://wbsapi.withings.net/measure"
    WITHINGS_MEASURE_TERM_SECONDS = 60 * 60