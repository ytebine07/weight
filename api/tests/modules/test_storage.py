import unittest

from modules.storage import Storage


class TestStorage(unittest.TestCase):
    def test_upload(self):
        target = Storage()
        target.upload("from_test.json", "/tmp/test.json")

    def test_download(self):
        target = Storage()
        print(target.download("from_test.json"))
