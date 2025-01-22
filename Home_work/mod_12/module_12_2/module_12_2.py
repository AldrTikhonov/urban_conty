from runner_and_tournament import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):
    all_results = {}
    @classmethod
    def setUpClass(cls):
        """
        метод, создающий атрибут класса all_result, где в виде словаря будут сохраняться результаты всех тестов.
        :return:
        """
        cls.all_results = {}

    def setUp(self):
        """
        метод, где создаются 3 объекта, бегуны, имеющие имя и скорость
        :return:
        """
        self.runner1 = Runner("Usain", 10)
        self.runner2 = Runner("Andrey", 9)
        self.runner3 = Runner("Nick", 3)



    @classmethod
    def tearDownClass(cls):
        """
        метод, где выводятся all_result по очереди в столбец
        :return:
        """
        for result in cls.all_results.values():
            print(result)



    def test_race_1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results[max(results.keys())] = results
        self.assertFalse(results[max(results.keys())] == "Usain")

    def test_race_2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[max(results.keys())] = results
        self.assertFalse(results[max(results.keys())] == "Andrey")

    def test_race_3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[max(results.keys())] = results
        self.assertTrue(results[max(results.keys())] == "Nick")


if __name__ == "__main__":
    unittest.main()
