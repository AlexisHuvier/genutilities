import unittest
from genutilities import json


class JsonObjectTests(unittest.TestCase):
    def setUp(self):
        self.obj = json.JsonObject("tests/test.json", {"config": "default"}, saved_destroy=False)

    def test_obj(self):
        self.assertEqual(str(self.obj), '{\n    "config": "other"\n}')
        self.assertEqual(self.obj["config"], "other")
        self.obj["joueurs.michel"] = 3
        self.assertEqual(str(self.obj), '{\n    "config": "other",\n    "joueurs": {\n        "michel": 3\n    }\n}')
        self.assertEqual(self.obj["joueurs.michel"], 3)
        
        with self.assertRaises(KeyError) as ctx:
            print(self.obj["wtf"])
        
        self.assertTrue("This key doesn't exist. Use get method to give a default value." in str(ctx.exception))

    def test_to_xml(self):
        self.assertEqual(self.obj.to_xml(), '<?xml version="1.0" encoding="UTF-8"?>\n<root>\n   <config>other</config>\n</root>')
        o2 = json.JsonObject("doesnt_be_saved.json", { 
            "config": "other",
            "joueurs": {
                "michel": 3
            },
            "score": [
                {
                    "oui": "non"
                },
                "non"
            ]
        }, saved_destroy=False)
        self.assertEqual(o2.to_xml(), '<?xml version="1.0" encoding="UTF-8"?>\n<root>\n   <config>other</config>\n   <joueurs>\n      <michel>3</michel>\n   </joueurs>\n   <score>\n      <element>\n         <oui>non</oui>\n      </element>\n      <element>non</element>\n   </score>\n</root>')
