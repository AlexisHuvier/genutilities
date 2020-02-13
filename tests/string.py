import unittest
from genutilities import string


class ModificationTests(unittest.TestCase):
    def test_remove(self):
        text = "Ceci est un test"
        self.assertEqual(string.remove(text, "t"), "Ceci es un es")
        self.assertEqual(string.remove(text, ("c", "t")), "Cei es un es")
        self.assertEqual(string.remove(text, ["es", "is"]), "Ceci t un tt")
        
        with self.assertRaises(TypeError) as ctx:
            string.remove(text, 4)

        self.assertTrue("Second Argument must be a list or a str." in str(ctx.exception))