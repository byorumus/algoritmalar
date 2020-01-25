import unittest
import question1


class Question1TestCase(unittest.TestCase):
    def test_small(self):
        self.assertEqual(question1.is_greater_than(1, 2), False)

    def test_equal(self):
        self.assertEqual(question1.is_greater_than(1, 1), False)

    def test_negative(self):
        self.assertEqual(question1.is_greater_than(-1, 2), False)

    def test_large(self):
        self.assertEqual(question1.is_greater_than(2, 1), True)

    def test_large_negative(self):
        self.assertEqual(question1.is_greater_than(-10, -20), True)

if __name__ == '__main__':
    unittest.main()
