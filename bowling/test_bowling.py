#
# Bowling kata
#
import bowling
import unittest

class BowlingTest(unittest.TestCase):
    def test_get_next_roll(self):
        oo = bowling.Bowling("123-1/X4123412341234")
        res = oo.getNextRoll(2)
        self.assertEquals(res, "12")
        oo = bowling.Bowling("X4123412341234")
        res = oo.getNextRoll()
        self.assertEquals(res, "X")

    def test_next_frame(self):
        oo = bowling.Bowling("123-1/X4123412341234")
        res, oo.rolls = oo.popNextFrame(oo.rolls)
        self.assertEquals(res, "12")
        res, oo.rolls = oo.popNextFrame(oo.rolls)
        self.assertEquals(res, "3-")
        res, oo.rolls = oo.popNextFrame(oo.rolls)
        self.assertEquals(res, "1/")
        res, oo.rolls = oo.popNextFrame(oo.rolls)
        self.assertEquals(res, "X")
        res, oo.rolls = oo.popNextFrame(oo.rolls)
        self.assertEquals(res, "41")


    def test_compute_score_for_simple(self):
        oo = bowling.Bowling("1234")
        res = oo.computeScoreForSimple("12", oo.rolls)
        self.assertEquals(res, 3)
        res = oo.computeScoreForSimple("1-", oo.rolls)
        self.assertEquals(res, 1)


    def test_compute_score_for_spare(self):
        oo = bowling.Bowling("34")
        res = oo.computeScoreForSpare("3/", oo.rolls)
        self.assertEquals(res, 13)


    def test_compute_score_for_strike(self):
        oo = bowling.Bowling("34")
        res = oo.computeScoreForStrike("X", oo.rolls)
        self.assertEquals(res, 17)


if __name__ == "__main__":
    unittest.main()

# EOF
