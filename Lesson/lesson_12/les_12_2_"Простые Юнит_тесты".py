import calk
import unittest

class CalkTest(unittest.TestCase):
    def test_add(self):
        """
        Тест проверяет правильность работы функции add в калькуляторе
        :return:
        """
        self.assertEqual(calk.add(1, 2), 3)
    def test_sub(self):
        self.assertEqual(calk.sub(3, 2), 1)
    def test_mul(self):
        self.assertEqual(calk.mul(3, 2), 6)
    def test_div(self):
        self.assertEqual(calk.div(6, 2), 3)


if __name__ == "__main__":
    unittest.main()