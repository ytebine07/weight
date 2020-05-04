import unittest

from modules.body import Body
from modules.withings import Withings, Token


class Test_Withings(unittest.TestCase):
    def test_fetch_last_body(self):
        target = Withings()
        last_body = target.fetch_last_body()
        self.assertTrue(type(last_body) is Body)

    def test_token(self):
        target = Token()
        type(target)

    def test_refresh(self):
        Token().refresh()
