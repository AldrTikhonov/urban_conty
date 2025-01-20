import calk
import unittest

class CalkTest(unittest.TestCase):
    def setUp(self):
        """
        метод запускающийся перед каждым тестом (сложения, вычитания и т.д.)
        :return:
        """
        print("setup")

    @classmethod
    def setUpClass(cls):
        """
        метод запускается в самом начале и 1 раз
        :return:
        """
        print("MegaSetup")


    def tearDown(self):
        """
        метод запускается после любого тест - кейса
        :return:
        """
        pass


    @classmethod
    def tearDownClass(cls):
        """
        метод запускается после отработки всех тестов и 1 раз
        :return:
        """


    def test_add(self):
        """
        тест на функцию сложения в калькуляторе
        :return:
        """
        self.assertEqual(calk.add(1, 2), 3)
    def test_sub(self):
        """
        тест на функцию вычитания в калькуляторе
        :return:
        """
        self.assertEqual(calk.sub(5, 3), 2)

if __name__ == "__main__":
    unittest.main()