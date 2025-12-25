
import unittest
from refactored_code import (
    Computer, Browser, BrowserComputer,
    get_computer_browsers_one_to_many,
    get_computers_with_total_memory,
    get_computers_with_department
)

class TestBrowserComputerLogic(unittest.TestCase):

    def setUp(self):
        self.computers = [
            Computer(1, "Игровой компьютер"),
            Computer(2, "Рабочий компьютер"),
            Computer(3, "Серверный отдел")
        ]
        self.browsers = [
            Browser(1, "Chrome", 512, 1),
            Browser(2, "Firefox", 256, 2),
            Browser(3, "Edge", 300, 3),
            Browser(4, "Chrome", 500, 2)
        ]

    def test_get_computer_browsers_one_to_many(self):
        result = get_computer_browsers_one_to_many(self.computers, self.browsers)
        self.assertEqual(len(result), 3)
        computer_names = [comp.name for comp, _ in result]
        self.assertIn("Игровой компьютер", computer_names)
        self.assertIn("Рабочий компьютер", computer_names)
        self.assertIn("Серверный отдел", computer_names)

    def test_get_computers_with_total_memory(self):
        result = get_computers_with_total_memory(self.computers, self.browsers)
        self.assertEqual(len(result), 3)
        memory_values = [total for _, total in result]
        self.assertEqual(memory_values, sorted(memory_values, reverse=True))

    def test_get_computers_with_department(self):
        result = get_computers_with_department(self.computers, self.browsers)
        self.assertEqual(len(result), 1)
        comp_name, browsers = result[0]
        self.assertEqual(comp_name.name, "Серверный отдел")
        self.assertEqual(browsers, ["Edge"])

if __name__ == "__main__":
    unittest.main()
