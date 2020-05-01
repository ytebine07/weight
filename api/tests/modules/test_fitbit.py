import unittest

from datetime import datetime

from modules.fitbit import Fitbit
from modules.body import Body


class TestFitbit(unittest.TestCase):
    def test_test(self):
        body: Body = Body("92.9", "21.1", datetime.now())
        f = Fitbit(body)
        f.save()
