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

# We made an iterable list of the different dices, we make an empty list where we will add the possible pairs
# We made a variable to keep control of the number of the pair that we are actually working on
# We start a loop to look through all the dices
# FIRST CONDITIONAL "if", If the dice count is equal 2 and is equal or bigger than the current pair we are working with, we set up the new value of the current pair
# SECOND CONDITIONAL, if the account of the dice in the list of possible pairs is grather than 0 we append
# the value and if is not we clear the list because it menas is a bigger value than the value we had before
# and after clear the list we append the new bigger value of a possible pair
    @staticmethod
    def one_pair(d1,  d2,  d3,  d4,  d5):
        all_dice = [d1,  d2,  d3,  d4,  d5]
        possible_pairs = []
        current_pair = 0
        for dice in all_dice:
            if all_dice.count(dice) == 2 and dice >= current_pair:
                current_pair = dice
                if possible_pairs.count(dice) > 0:
                    possible_pairs.append(dice)
                else:
                    possible_pairs.clear()
                    possible_pairs.append(dice)
        return sum(possible_pairs)

# We made an iterable list of the different dices,  we make an empty list where we will add the pairs
# We start a loop to look though all the dices, the FIRST CONDITIONAL help to check that we are working minum
# with a pair and the SECOND CONDITIONAL just help to make sure that you are just going to add pairs and
# nothing over that
# When we finish the loop we check that we have more than a pair in our list, is is the case we give back the
# sumative of the pairs if is the opposite we just give back a 0
    @staticmethod
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

# We made an iterable list of the different dices,  we make an empty list where we will add the pairs. We
# start a loop to look through all the dices. If the count of the dice number is equal or bigger to 3 AND the
# account of the same number dice inside the threesome list is minor than 3, we append the dice number to the
# threesome list. Finally we return the sumative of the threesome
    @staticmethod
    def three_of_a_kind(d1,  d2,  d3,  d4,  d5):
        all_dice = [d1,  d2,  d3,  d4,  d5]
        threesome = []
        for dice in all_dice:
            if all_dice.count(dice) >= 3 and threesome.count(dice) < 3:
                threesome.append(dice)
        return sum(threesome)

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
