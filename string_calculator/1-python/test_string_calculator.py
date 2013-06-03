#
# String Calculator kata
#
import string_calculator
import unittest

class StringCalculatorTest(unittest.TestCase):
    def test_empty(self):
        oo = string_calculator.StringCalculator()
        res = oo.add("")
        self.assertEquals(0, res)

    def test_one(self):
        oo = string_calculator.StringCalculator()
        res = oo.add("1")
        self.assertEquals(1, res)

    def test_two(self):
        oo = string_calculator.StringCalculator()
        res = oo.add("1,2")
        self.assertEquals(3, res)

    def test_many(self):
        oo = string_calculator.StringCalculator()
        res = oo.add("1,2,3")
        self.assertEquals(6, res)

    def test_many_and_newline(self):
        oo = string_calculator.StringCalculator()
        res = oo.add("1\n2,3")
        self.assertEquals(6, res)

    def test_normalize_string(self):
        oo = string_calculator.StringCalculator()
        res = oo.normalizeString("1,2,3")
        self.assertEquals("1,2,3", res)
        res = oo.normalizeString("1\n2,3")
        self.assertEquals("1,2,3", res)
        res = oo.normalizeString("//;\n1\n2;3")
        self.assertEquals("1,2,3", res)
        res = oo.normalizeString("//***\n1\n2***3")
        self.assertEquals("1,2,3", res)
        res = oo.normalizeString("//[**][++]\n1\n2**3++4")
        self.assertEquals("1,2,3,4", res)

    def test_negative(self):
        oo = string_calculator.StringCalculator()
        with self.assertRaises(Exception) as cm:
            res = oo.add("1,-2,3")
        self.assertEqual(cm.exception.message, "negative numbers not allowed : -2")
        with self.assertRaises(Exception) as cm:
            res = oo.add("1,-2,-3")
        self.assertEqual(cm.exception.message, """negative numbers not allowed : -2
negative numbers not allowed : -3""")

    def test_max_size(self):
        oo = string_calculator.StringCalculator()
        res = oo.add("1,2,3,999")
        self.assertEquals(1005, res)
        res = oo.add("1,2,3,1000")
        self.assertEquals(6, res)


if __name__ == "__main__":
    unittest.main()

# EOF
