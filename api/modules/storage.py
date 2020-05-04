import os
import json
from google.cloud import storage, secretmanager


class Storage:
    def __init__(self):
        super().__init__()

        if not os.path.exists(os.getenv("GOOGLE_APPLICATION_CREDENTIALS")):
            self.__download_credential()

        self.__client = storage.Client()
        self.__bucket = self.__client.get_bucket("weight-transfer-api")

    def upload(self, name, path):
        blob = self.__bucket.blob(name)
        blob.upload_from_filename(path)

    def download(self, file):
        blob = self.__bucket.get_blob(file)
        return blob.download_as_string().decode("utf-8")

    def __download_credential(self):
        client = secretmanager.SecretManagerServiceClient()
        name = client.secret_version_path("homes", "weight-transfer-api-to-gsc", 1)
        response = client.access_secret_version(name)
        str = response.payload.data.decode("UTF-8")

        with open(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"), mode="w") as f:
            f.write(json.dumps(str, indent=2))
