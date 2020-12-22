class Yatzy:

    # Play the chance resource, make a sumative of all the faces of the dices
    @staticmethod
    def chance(d1, d2, d3, d4, d5):
        return(d1 + d2 + d3 + d4 + d5)


# Check that all the faces of the dice are equal to be able to make a Yatzy


    @staticmethod
    def yatzy(dice):
        for die in dice:
            if die == dice[0]:
                continue
            else:
                return 0
        return 50

# Check how many of the dice show the same number
# Check for how many dices with the number 1
    @staticmethod
    def ones(d1,  d2,  d3,  d4,  d5):
        all_dice = [d1, d2, d3, d4, d5]
        count = 0
        for dice in all_dice:
            if dice == 1:
                count += 1
        return count

# Check for how many dices with the number 2
    @staticmethod
    def twos(d1,  d2,  d3,  d4,  d5):
        all_dice = [d1, d2, d3, d4, d5]
        count = 0
        for dice in all_dice:
            if dice == 2:
                count += 2
        return count

# Check for how many dices with the number 3
    @staticmethod
    def threes(d1,  d2,  d3,  d4,  d5):
        all_dice = [d1, d2, d3, d4, d5]
        count = 0
        for dice in all_dice:
            if dice == 3:
                count += 3
        return count

# Check for how many dices with the number 4
    @staticmethod
    def fours(d1,  d2,  d3,  d4,  d5):
        all_dice = [d1, d2, d3, d4, d5]
        count = 0
        for dice in all_dice:
            if dice == 4:
                count += 4
        return count

# Check for how many dices with the number 5
    @staticmethod
    def fives(d1,  d2,  d3,  d4,  d5):
        all_dice = [d1, d2, d3, d4, d5]
        count = 0
        for dice in all_dice:
            if dice == 5:
                count += 5
        return count

# Check for how many dices with the number 6
    @staticmethod
    def sixes(d1,  d2,  d3,  d4,  d5):
        all_dice = [d1, d2, d3, d4, d5]
        count = 0
        for dice in all_dice:
            if dice == 6:
                count += 6
        return count

    @staticmethod
    def one_pair(d1,  d2,  d3,  d4,  d5):
        counts = [0]*6
        counts[d1-1] += 1
        counts[d2-1] += 1
        counts[d3-1] += 1
        counts[d4-1] += 1
        counts[d5-1] += 1
        at = 0
        for at in range(6):
            if (counts[6-at-1] == 2):
                return (6-at)*2
        return 0

    @staticmethod
    def two_pair(d1,  d2,  d3,  d4,  d5):
        counts = [0]*6
        counts[d1-1] += 1
        counts[d2-1] += 1
        counts[d3-1] += 1
        counts[d4-1] += 1
        counts[d5-1] += 1
        n = 0
        score = 0
        for i in range(6):
            if (counts[6-i-1] >= 2):
                n = n+1
                score += (6-i)

        if (n == 2):
            return score * 2
        else:
            return 0

    @staticmethod
    def three_of_a_kind(d1,  d2,  d3,  d4,  d5):
        t = [0]*6
        t[d1-1] += 1
        t[d2-1] += 1
        t[d3-1] += 1
        t[d4-1] += 1
        t[d5-1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i+1) * 3
        return 0

    @staticmethod
    def four_of_a_kind(_1,  _2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[_1-1] += 1
        tallies[_2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i+1) * 4
        return 0

    @staticmethod
    def smallStraight(d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[0] == 1 and
            tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
                tallies[4] == 1):
            return 15
        return 0

    @staticmethod
    def largeStraight(d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1
                and tallies[5] == 1):
            return 20
        return 0

    @staticmethod
    def fullHouse(d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i+1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i+1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
