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

# We made an iterable list of the different dices, we made an empty list where we will add the possible
# pairs. We made a variable to keep control of the number of the pair that we are actually working on. We
# start a loop to look through all the dices. The FIRST CONDITIONAL "if", if the dice count is equal 2 and
# the dice is equal or bigger than the current pair we are working with, we set up the new value of the
# current pair. The SECOND CONDITIONAL "if", if the account of the dice in the list of possible pairs is
# grather than 0 we append the dice value and if is not we clear the list because it menas is a bigger
# value than the value we had before and after clear the list we append the new bigger value of a possible
# pair
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

# We made an iterable list of the different dices, we make an empty list where we will add the pairs.
# We start a loop to look though all the dices, the FIRST CONDITIONAL help to check that we are working minum with a pair and the SECOND CONDITIONAL just help to make sure that you are just going to add pairs and nothing over that. When we finish the loop we check that we have more than a pair in our list, if is the case we give back the sumative of the pairs if is the opposite we just give back a 0
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

# We made an iterable list of the different dices, we make an empty list where we will add the threesome.
# We start a loop to look through all the dices. If the count of the dice with the same number is equal or
# bigger to 3 AND the account of the same number dice inside the threesome list is minor than 3, we append
# the dice to the threesome list. Finally we return the sumative of the list called threesome
    @staticmethod
    def three_of_a_kind(d1,  d2,  d3,  d4,  d5):
        all_dice = [d1,  d2,  d3,  d4,  d5]
        threesome = []
        for dice in all_dice:
            if all_dice.count(dice) >= 3 and threesome.count(dice) < 3:
                threesome.append(dice)
        return sum(threesome)

# We made an iterable list of the different dices, we make an empty list where we will add the four dice of
# same number. We start a loop to look through all the dices. If the count of the dice with the same number
# is equal or bigger to 4 AND the account of the same number dice inside the poker list is minor than 4, we
# append the dice to the poker list. Finally we return the sumative of the list called poker
    @staticmethod
    def four_of_a_kind(d1,  d2,  d3,  d4,  d5):
        all_dice = [d1,  d2,  d3,  d4,  d5]
        poker = []
        for dice in all_dice:
            if all_dice.count(dice) >= 4 and poker.count(dice) < 4:
                poker.append(dice)
        return sum(poker)

# We made an iterable list of the different dices. And we create a conditional where we sort the list to have it in numerical order from 1 to 5 (in case is a small straight) and we check with a boolean if it's the same than a list from 1 to 5, in case it's true we just return a sumative of all numbers and in case is false we return a 0
    @staticmethod
    def smallStraight(d1,  d2,  d3,  d4,  d5):
        all_dice = [d1,  d2,  d3,  d4,  d5]
        if sorted(all_dice) == list(range(1, 6)):
            return sum(all_dice)
        else:
            return 0

# We made an iterable list of the different dices. And we create a conditional where we sort the list to
# have in numerical order from 2 to 6 (in case is a large straight) and we check with a boolean if it's
# the same than a list from 2 to 6, in case it's true we just return a sumative of all numbers and in case
# is false we return a 0
    @staticmethod
    def largeStraight(d1,  d2,  d3,  d4,  d5):
        all_dice = [d1,  d2,  d3,  d4,  d5]
        if sorted(all_dice) == list(range(2, 7)):
            return sum(all_dice)
        else:
            return 0

# We made a list with all the dice values. We made a loop to look through all the dice numbers. If the
# dice account is equal to 3 or to 2 means that we have a threesome or a pair and we just want to continue
# looping through all the dices, in case gives back a "False" result means that we are not having a
# threesome and a pair to be able to make a full house, in this case we just return a 0. If it finish the
# loop without get back a "False" means that we have a full house and we return a sumative of the all_dice
# list
    @staticmethod
    def fullHouse(d1, d2, d3, d4, d5):
        all_dice = [d1,  d2,  d3,  d4,  d5]
        for dice in all_dice:
            if all_dice.count(dice) == 3 or all_dice.count(dice) == 2:
                continue
            else:
                return 0
        return sum(all_dice)
