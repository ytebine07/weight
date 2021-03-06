import os
import json
from google.cloud import storage, secretmanager

from modules.constants import Constants


class Storage:
    def __init__(self):
        super().__init__()

        if not os.path.exists(Constants.GCP_UPLOAD_TO_GCS_KEY_PATH):
            self.__download_credential()

        self.__client = storage.Client.from_service_account_json(
            Constants.GCP_UPLOAD_TO_GCS_KEY_PATH
        )
        self.__bucket = self.__client.get_bucket("weight-transfer-api")

    def upload(self, name, path):
        blob = self.__bucket.blob(name)
        blob.upload_from_filename(path)

    def download(self, file):
        blob = self.__bucket.get_blob(file)
        return blob.download_as_string().decode("utf-8")

    def __download_credential(self):
        client = secretmanager.SecretManagerServiceClient()
        name = client.secret_version_path(
            Constants.GCP_PROJECT_ID, Constants.GCP_KEY_NAME, Constants.GCP_KEY_VERSION
        )
        response = client.access_secret_version(name)
        json_str = json.loads(response.payload.data.decode("UTF-8"))

        with open(Constants.GCP_UPLOAD_TO_GCS_KEY_PATH, mode="w") as f:
            f.write(json.dumps(json_str, indent=2))
