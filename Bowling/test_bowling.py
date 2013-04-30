#
# Bowling kata
#

class Bowling:
    def __init__(self, rolls):
        self.rolls = rolls

    def compute(self):
        ret = 0
        cpt = 0
        try:
            while cpt < 10:
                cpt += 1
                frame, self.rolls = self.popNextFrame(self.rolls)
                ret += self.computeScoreForFrame(frame, self.rolls)
        except Exception, ee:
            pass
        return ret


    def computeScoreForFrame(self, frame, rolls):
        ret = 0
        if frame == "X":
            ret += self.computeScoreForStrike(frame, rolls)
        elif frame[-1] == "/":
            ret += self.computeScoreForSpare(frame, rolls)
        else:
            ret += self.computeScoreForSimple(frame, rolls)
        return ret

    def computeScoreForSpare(self, frame, rolls):
        return 10 + self.computeScoreForFrame(self.getNextRoll(), rolls)

    def computeScoreForStrike(self, frame, rolls):
        return 10 + self.computeScoreForFrame(self.getNextRoll(2), rolls)

    def computeScoreForSimple(self, frame, rolls):
        ret = 0
        for ii in frame:
            if ii == "-":
                pass
            else:
                ret += int(ii)
        return ret

    def popNextFrame(self, rolls):
        if rolls[0] == "X":
            ret = rolls[0]
            rolls = rolls[1:]
            return ret, rolls
        else:
            ret = rolls[:2]
            rolls = rolls[2:]
            return ret, rolls

    def getNextRoll(self, number = 1):
        return self.rolls[:number]

if __name__ == "__main__":
    pass

# EOF