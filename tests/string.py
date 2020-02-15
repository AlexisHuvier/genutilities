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
    
    def test_random(self):
        r1 = string.random()
        r2 = string.random(10)
        r3 = string.random(4, "abc")
        self.assertEqual(len(r1), 30)
        self.assertEqual(len(r2), 10)
        self.assertEqual(len(r3), 4)
        print("\nRandom String 1 (Default parameters): {}\nRandom String 2 (Len 10): {}\nRandom String 3 (Len 4, letters = 'a', 'b', 'c'): {}".format(r1, r2, r3))
    
    def test_reverse(self):
        self.assertEqual(string.reverse("oui"), "iuo")
        self.assertEqual(string.reverse("Ceci est à l'endroit"), "tiordne'l à tse iceC")
    
    def test_shuffle(self):
        s1 = string.shuffle("Ceci est un test")
        for i in s1:
            self.assertIn(i, "Ceci est un test")
        self.assertEqual(len(s1), len("Ceci est un test"))
        print("\nShuffle de 'Ceci est un test': {}".format(s1))
    
    def test_unique(self):
        self.assertEqual(string.unique("oui"), "oui")
        self.assertEqual(string.unique("Ceci est un test"), "Ceci stun")
    
    def test_convertion_between_convention(self):
        self.assertEqual(string.snake_to_pascal("snake_to_pascal"), "SnakeToPascal")
        self.assertEqual(string.pascal_to_snake("PascalToSnake"), "pascal_to_snake")
        self.assertEqual(string.snake_to_camel("snake_to_camel"), "snakeToCamel")
        self.assertEqual(string.camel_to_snake("camelToSnake"), "camel_to_snake")
        self.assertEqual(string.camel_to_pascal("camelToPascal"), "CamelToPascal")
        self.assertEqual(string.pascal_to_camel("PascalToCamel"), "pascalToCamel")