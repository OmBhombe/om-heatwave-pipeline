import unittest
from heatwave import check_heatwave

class TestHeatwave(unittest.TestCase):

    def test_low(self):
        self.assertEqual(check_heatwave(30), "Low")

    def test_moderate(self):
        self.assertEqual(check_heatwave(37), "Moderate")

    def test_high(self):
        self.assertEqual(check_heatwave(42), "High")

if __name__ == "__main__":
    unittest.main()
