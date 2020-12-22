"""
def yatzy(dice):
    counts = [0]*(len(dice)+1)
    for die in dice:
        counts[die-1] += 1
    for i in range(len(counts)):
        if counts[i] == 5:
            return 50
    return 0



def yatzy(dice):
    for die in dice:
        if die == dice[0]:
            continue
        else:
            return 0
    return 50
"""


def ones(d1,  d2,  d3,  d4,  d5):
    sum = 0
    for dice in ones:
        if dice == 1:
            sum += 1
    return sum


if __name__ == "__main__":
    #assert yatzy([4, 4, 4, 4, 4]) == 50
    #assert yatzy([6, 6, 6, 6, 6]) == 50
    #assert yatzy([6, 6, 6, 6, 3]) == 0
    assert ones(1, 2, 3, 4, 5) == 1
    #assert 2 == ones(1,2,1,4,5)
    #assert 0 == ones(6,2,2,4,5)
    #assert 4 == ones(1,2,1,1,1)
