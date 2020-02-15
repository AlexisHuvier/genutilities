import unittest
from genutilities import dictionnary

class DictionnaryTests(unittest.TestCase):
    def setUp(self):
        self.dic = { 
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
        }

    def test_to_xml(self):
        self.assertEqual(dictionnary.to_xml({"config" : "other"}), '<?xml version="1.0" encoding="UTF-8"?>\n<root>\n   <config>other</config>\n</root>')
        self.assertEqual(dictionnary.to_xml(self.dic), '<?xml version="1.0" encoding="UTF-8"?>\n<root>\n   <config>other</config>\n   <joueurs>\n      <michel>3</michel>\n   </joueurs>\n   <score>\n      <element>\n         <oui>non</oui>\n      </element>\n      <element>non</element>\n   </score>\n</root>')

    def test_flatten(self):
        self.assertEqual(dictionnary.flatten({"config": "other"}), {"config": "other"})
        self.assertEqual(dictionnary.flatten(self.dic), {'config': 'other', 'joueurs.michel': 3, 'score.0.oui': 'non', 'score.1': 'non'})
        self.assertEqual(dictionnary.flatten(self.dic, "_"), {'config': 'other', 'joueurs_michel': 3, 'score_0_oui': 'non', 'score_1': 'non'})
        self.assertEqual(dictionnary.flatten(self.dic, list_flatten=False), {'config': 'other', 'joueurs.michel': 3, 'score': [{'oui': 'non'}, 'non']})
    
    def test_unflatten(self):
        self.assertEqual(dictionnary.unflatten({'config': 'other', 'joueurs.michel': 3}), {"config": "other", "joueurs": { "michel" : 3 }})
        self.assertEqual(dictionnary.unflatten({'config': 'other', 'joueurs_michel': 3}, "_"), {"config": "other", "joueurs": { "michel" : 3 }})
    
    def test_substract(self):
        self.assertEqual(dictionnary.substract({"conf": "other"}, {"conf": "blabla"}), {})
        self.assertEqual(dictionnary.substract({"conf": "other", "test2": "oui"}, {"conf": "blabla"}), {"test2": "oui"})
        self.assertEqual(dictionnary.substract({"conf": "other"}, {"conf2": "blabla"}), {"conf": "other"})