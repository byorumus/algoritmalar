import unittest
import question2


class Question2TestCase(unittest.TestCase):
    def test_prime1(self):
        self.assertEqual(True, question2.is_prime(2))

    def test_prime2(self):
        self.assertEqual(True, question2.is_prime(3))

    def test_prime3(self):
        self.assertEqual(False, question2.is_prime(4))

    def test_prime4(self):
        self.assertEqual(True, question2.is_prime(5))

    def test_prime5(self):
        self.assertEqual(False, question2.is_prime(6))

    def test_prime6(self):
        self.assertEqual(False, question2.is_prime(1000000))

    def test_prime7(self):
        self.assertEqual(False, question2.is_prime(1))

    def test_all_primes1(self):
        self.assertEqual([], question2.all_primes(2))

    def test_all_primes2(self):
        self.assertEqual([2], question2.all_primes(3))

    def test_all_primes3(self):
        self.assertEqual([2, 3], question2.all_primes(4))

    def test_all_primes4(self):
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19], question2.all_primes(20))

    def test_question2_all_1(self):
        self.assertEqual(False, question2.question2_all(2))

    def test_question2_all_2(self):
        self.assertEqual(False, question2.question2_all(3))

    def test_question2_all_3(self):
        self.assertEqual(True, question2.question2_all(5))


if __name__ == '__main__':
    unittest.main()
