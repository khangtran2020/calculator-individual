import unittest
from Calculator import Calculator
from CsvReader import CsvReader

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        test_data = CsvReader("data/Unit Test Addition.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_subtraction(self):
        test_data = CsvReader("data/Unit Test Subtraction.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiplication(self):
        test_data = CsvReader("data/Unit Test Multiplication.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_division(self):
        test_data = CsvReader("data/Unit Test Division.csv").data
        for row in test_data:
            lenth = self.calculator.getLength(row['Result'])
            result = float(row['Result'])
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2'],lenth), result)
            self.assertEqual(self.calculator.result, result)

    def test_square(self):
        test_data = CsvReader("data/Unit Test Square.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.square(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_sqare_root(self):
        test_data = CsvReader("data/Unit Test Square Root.csv").data
        for row in test_data:
            lenth = self.calculator.getLength(row['Result'])
            result = float(row['Result'])
            self.assertEqual(self.calculator.sqrt(row['Value 1'],lenth), result)
            self.assertEqual(self.calculator.result, result)

if __name__ == '__main__':
    unittest.main()
