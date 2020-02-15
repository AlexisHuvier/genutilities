import unittest
from genutilities import json


class JsonObjectTests(unittest.TestCase):
    def setUp(self):
        self.obj = json.JsonObject("tests/test.json", {"config": "default"}, saved_destroy=False)

    def test_basic_function(self):
        self.assertEqual(str(self.obj), '{\n    "config": "other"\n}')
        self.assertEqual(self.obj["config"], "other")
        self.obj["joueurs.michel"] = 3
        self.assertEqual(str(self.obj), '{\n    "config": "other",\n    "joueurs": {\n        "michel": 3\n    }\n}')
        self.assertEqual(self.obj["joueurs.michel"], 3)
        
        with self.assertRaises(KeyError) as ctx:
            print(self.obj["wtf"])
        
        self.assertTrue("This key doesn't exist. Use get method to give a default value." in str(ctx.exception))
    
    def test_clear(self):
        obj = json.JsonObject("osef.json", {"test": "oui"}, saved_destroy=False)
        self.assertEqual(obj.dic, {"test": "oui"})
        obj.clear()
        self.assertEqual(obj.dic, {})
    
    def test_set_dict(self):
        obj = json.JsonObject("osef.json", {"test": "oui"}, saved_destroy=False)
        self.assertEqual(obj.dic, {"test": "oui"})
        obj.set_dict({"oui": "test"})
        self.assertEqual(obj.dic, {"oui": "test"})
