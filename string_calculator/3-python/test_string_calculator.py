#
# String Calculator kata
#
import string_calculator
import unittest

class StringCalculatorTest(unittest.TestCase):
    def test_None(self):
        oo = string_calculator.StringCalculator()
        res = oo.add("")
        self.assertEquals(0, res)

if __name__ == "__main__":
    unittest.main()

# EOF
