import unittest

print("Doing other stuff that isn't testing related; maybe setting up constants")

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(fun(3), 4)

    def test2(self):
        self.assertFalse(fun(4) == 6)

    def test3(self):
        self.assertTrue(fun(3) == 4)

if __name__ == "__main__":
    unittest.main()