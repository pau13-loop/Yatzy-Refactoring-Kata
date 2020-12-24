"""
#ORIGNIAL
def yatzy(dice):
    counts = [0]*(len(dice)+1)
    for die in dice:
        counts[die-1] += 1
    for i in range(len(counts)):
        if counts[i] == 5:
            return 50
    return 0

#REFACTOR
def yatzy(dice):
    for die in dice:
        if die == dice[0]:
            continue
        else:
            return 0
    return 50


ORIGNIAL ONE_PAIR
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


REFACTOR TWO_PAIR
def one_pair(d1,  d2,  d3,  d4,  d5):
    all_dice = [d1,  d2,  d3,  d4,  d5]
    current_pair = 0
    possible_pairs = []
    for dice in all_dice:
        if all_dice.count(dice) == 2 and dice >= current_pair:
            current_pair = dice
            if possible_pairs.count(dice) > 0:
                possible_pairs.append(dice)
            else:
                possible_pairs.clear()
                possible_pairs.append(dice)
    return sum(possible_pairs)


ORIGINIAL TWO_PAIR
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


REFACTOR TWO_PAIR
def two_pair(d1,  d2,  d3,  d4,  d5):
    all_dice = [d1,  d2,  d3,  d4,  d5]
    pairs = []
    for dice in all_dice:
        if all_dice.count(dice) >= 2:
            if pairs.count(dice) < 2:
                pairs.append(dice)
    if len(pairs) > 2:
        return sum(pairs)
    else:
        return 0



ORIGINAL THREE_OF_A_KIND
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


REFACTOR THREE_OF_A_KIND
def three_of_a_kind(d1,  d2,  d3,  d4,  d5):
    all_dice = [d1,  d2,  d3,  d4,  d5]
    threesome = []
    for dice in all_dice:
        if all_dice.count(dice) >= 3 and threesome.count(dice) < 3:
            threesome.append(dice)
    return sum(threesome)


ORIGINAL FOUR_OF_A_KIND
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


REFACTOR FOUR_OF_A_KIND
def four_of_a_kind(d1,  d2,  d3,  d4,  d5):
    all_dice = [d1,  d2,  d3,  d4,  d5]
    poker = []
    for dice in all_dice:
        if all_dice.count(dice) >= 4 and poker.count(dice) < 4:
            poker.append(dice)
    return sum(poker)



ORIGNIAL SMALL_STRAIGHT
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


REFACTOR SMALL_STRAIGHT
def smallStraight(d1,  d2,  d3,  d4,  d5):
    all_dice = [d1,  d2,  d3,  d4,  d5]
    if sorted(all_dice) == list(range(1, 6)):
        return sum(all_dice)
    else:
        return 0



ORIGNIAL LARGE_STRAIGHT
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


REFACTOR LARGE_STRAIGHT
def largeStraight(d1,  d2,  d3,  d4,  d5):
    all_dice = [d1,  d2,  d3,  d4,  d5]
    if sorted(all_dice) == list(range(2, 7)):
        return sum(all_dice)
    else:
        return 0



ORIGINAL FULL_HOUSE
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


REFACTOR FULL_HOUSE
def fullHouse(d1, d2, d3, d4, d5):
    all_dice = [d1,  d2,  d3,  d4,  d5]
    for dice in all_dice:
        if all_dice.count(dice) == 3 or all_dice.count(dice) == 2:
            continue
        else:
            return 0
    return sum(all_dice)
"""

if __name__ == "__main__":

    # YATZI ASSERTS
    #assert yatzy([4, 4, 4, 4, 4]) == 50
    #assert yatzy([6, 6, 6, 6, 6]) == 50
    #assert yatzy([6, 6, 6, 6, 3]) == 0
    # ONE_PAIR ASSERTS
    #assert 6 == one_pair(3, 4, 3, 5, 6)
    #assert 10 == one_pair(5, 3, 3, 3, 5)
    #assert 12 == one_pair(5, 3, 6, 6, 5)

    # TOW_PAIR ASSERTS
    #assert 16 == two_pair(3, 3, 5, 4, 5)
    #assert 18 == two_pair(3, 3, 6, 6, 6)
    #assert 0 == two_pair(3, 3, 6, 5, 4)

    # THREESOME
    #assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 4, 5)
    #assert 15 == Yatzy.three_of_a_kind(5, 3, 5, 4, 5)
    #assert 9 == three_of_a_kind(3, 3, 3, 3, 5)

    # FOUR_OF_A_KIND ASSERTS
    #assert 12 == four_of_a_kind(3, 3, 3, 3, 5)
    #assert 20 == four_of_a_kind(5, 5, 5, 4, 5)
    #assert 12 == four_of_a_kind(3, 3, 3, 3, 3)
    #assert 0 == four_of_a_kind(3, 3, 3, 2, 1)

    # SMALL STRAIGHT
    #assert 15 == smallStraight(1, 2, 3, 4, 5)
    #assert 15 == smallStraight(2, 3, 4, 5, 1)
    #assert 0 == smallStraight(1, 2, 2, 4, 5)

    # LARGE_STRAIGHT
    #assert 20 == largeStraight(6, 2, 3, 4, 5)
    #assert 20 == largeStraight(2, 3, 4, 5, 6)
    #assert 0 == largeStraight(1, 2, 2, 4, 5)

    # FULL_HOUSE
    #assert 18 == fullHouse(6, 2, 2, 2, 6)
    #assert 0 == fullHouse(2, 3, 4, 5, 6)
