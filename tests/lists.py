import unittest
from genutilities import lists

class ListTests(unittest.TestCase):
    def setUp(self):
        self.l = [
            {'No': 1, 'Name': 'Alex', 'Country': 'India'},
            {'No': 2, 'Name': 'Ben', 'Country': 'USA'},
            {'No': 3, 'Name': 'Shri Ram', 'Country': 'India'},
            {'No': 4, 'Name': 'Smith', 'Country': 'USA'},
            {'No': 5, 'Name': 'Yuva Raj', 'Country': 'India'},
        ]

    def test_to_csv(self):
        self.assertEqual(lists.to_csv(self.l), "No,Name,Country\r\n1,Alex,India\r\n2,Ben,USA\r\n3,Shri Ram,India\r\n4,Smith,USA\r\n5,Yuva Raj,India\r\n")
        self.assertEqual(lists.to_csv([]), "\r\n")
        self.assertEqual(lists.to_csv([{"Nom": "H"}, {"Nom": "A"}]), "Nom\r\nH\r\nA\r\n")
    
    def test_flatten(self):
        self.assertEqual(lists.flatten(self.l), self.l)
        self.assertEqual(lists.flatten([[1,[2,3]], [4,5], [6], 7]), [1, 2, 3, 4, 5, 6, 7])

    def test_substract(self):
        self.assertEqual(lists.substract([1, 2, 3], [2]), [1, 3])
        self.assertEqual(lists.substract([3, 4, "oui", []], [[], 4]), [3, "oui"])
        self.assertEqual(lists.substract([1, 1, 2], [1]), [2])
        self.assertEqual(lists.substract([1, 1, 2], [1], False), [1, 2])
        self.assertEqual(lists.substract([1, 1, 2], [1, 1], False), [2])
    
    def test_unique(self):
        self.assertEqual(lists.unique([1, 2, 3]), [1, 2, 3])
        self.assertEqual(lists.unique([1, 1, 2]), [1, 2])