import unittest
import String_manipulation


class String_manipulation(unittest.TestCase):
    def test_concate(self):
        result = "Python is a language"
        self.assertEqual(result,"Python is a language","Incorrect one")
    
    def test_slicing(self):
        result = "ytho"
        self.assertEqual(result,"ytho","incorrect one")
    
    def test_formmatting(self):
        self.assertEqual(format("allen is a 20 years old"),"allen is a 20 years old")

    def test_manipulation(self):
        self.assertEqual("  PYTHON IS A","  PYTHON IS A","Incorrect one")
        self.assertEqual("  python is a","  python is a","Incorrect one")
        self.assertEqual("Python is a","Python is a","Incorrect one")
        self.assertEqual("Java is a","Java is a","Incorrect one")

if __name__=="__main__":
    unittest.main()