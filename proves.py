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
