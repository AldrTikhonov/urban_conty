from Home_work.mod_12.module_12_2.runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """ Создаем объект класса Runner """
        run = Runner('TestRunner_1')

        """ Вызовем метод walk 10 раз """
        for i in range(10):
            run.walk()

        """ Проверяем условие, что distance = 50 """
        self.assertEqual(run.distance, 50)


    def test_run(self):
        """ Создаем объект класса Runner """
        run = Runner('TestRunner_2')

        """ Вызовем метод run 10 раз """
        for i in range(10):
            run.run()

        """ Проверяем условие, что distance = 100 """
        self.assertEqual(run.distance, 100)

    def test_challenge(self):
        """ Создаем два объекта класса Runner """
        run1 = Runner('TestRunner_3')
        run2 = Runner('TestRunner_4')

        """ Вызываем методы walk и run по 10 раз соответственно """
        for i in range(10):
            run1.walk()
            run2.run()

        """ Проверяем, что distance у двух объектов не равны """
        self.assertNotEqual(run1.distance, run2.distance)


if __name__ == "__main__":
    unittest.main()
