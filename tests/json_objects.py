import unittest
import jsonutils


class JsonObjectTests(unittest.TestCase):
    def test_creating(self):
        obj = jsonutils.JsonObject("tests/test.json", {"config": "default"})