import unittest

from datetime import datetime

from modules.fitbit import Fitbit
from modules.body import Body


class TestFitbit(unittest.TestCase):
    def test_register(self):
        body: Body = Body("92.9", "21.1", datetime.now())
        f = Fitbit()
        f.register(body)

    def test_get_fat(self):
        f = Fitbit()
        f.get_fat()
