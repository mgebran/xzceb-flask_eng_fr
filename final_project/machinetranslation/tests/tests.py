from translator import englishtofrench, frenchtoenglish
import unittest

class testenfr(unittest.TestCase):
    def test_eng_fr(self):
        self.assertEqual(englishtofrench('Hello'),'Bonjour')
        self.assertNotEqual(englishtofrench('home'),'chien')

class testfren(unittest.TestCase):
    def test_fr_eng(self):
        self.assertEqual(frenchtoenglish('Bonjour'),'Hello')
        self.assertNotEqual(frenchtoenglish('Nom'),'negative')

unittest.main()
