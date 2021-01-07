class Yatzy:

    def __init__(self, *dice):
        self.dice = list(dice)

    # Play the chance option, make a sumative of all the faces of the dices
    @staticmethod
    def chance(*dice):
        return sum(dice)

    # Check that all the faces of the dice are equal to be able to make a Yatzy

    @staticmethod
    def yatzy(*dice):
        for num_dice in dice:
            if num_dice != dice[0]:
                return 0
        return 50

    # Return the number of all the dices that show the number 1

    @staticmethod
    def ones(*dice):
        return (dice.count(1))

    # Return the number of all the dices that show the number 2

    @staticmethod
    def twos(*dice):
        return (dice.count(2) * 2)

    # Return the number of all the dices that show the number 3

    @staticmethod
    def threes(*dice):
        return (dice.count(3) * 3)

    # Return the number of all the dices that show the number 4

    @staticmethod
    def fours(*dice):
        return (dice.count(4) * 4)

    # Return the number of all the dices that show the number 5

    @staticmethod
    def fives(*dice):
        return (dice.count(5) * 5)

    # Return the number of all the dices that show the number 6

    @staticmethod
    def sixes(*dice):
        return (dice.count(6) * 6)

    # We have made a variable to keep control of the number of the pair that we are actually working with. We
    # start a loop to look through all the dices. The if the dice count is equal 2 and
    # the dice is equal or bigger than the current pair we are working with, we set up the new value of the
    # current pair. Finally we return the value of the current pair plus two to be the actual value of the pair

    @staticmethod
    def one_pair(*dice):
        current_pair = 0
        for num_dice in dice:
            if dice.count(num_dice) == 2 and num_dice >= current_pair:
                current_pair = num_dice
        return (current_pair * 2)

    # We have made an empty list where we will add the pairs.
    # We start a loop to look though all the dices, If the account of the dice number is bigger or equal to two we know we are working with a
    # pair and if the account of the dice number in the list of pairs is minor than two help us to make sure that you are just going to add
    # pairs and nothing over that. When we finish the loop we check that we have more than a pair in our list, if is the case we give back the
    # sumative of the pairs if is the opposite we just return a 0

    @staticmethod
    def two_pair(*dice):
        pairs = []
        for num_dice in dice:
            if dice.count(num_dice) >= 2 and pairs.count(num_dice) < 2:
                pairs.append(num_dice)
        if len(pairs) > 2:
            return sum(pairs)
        else:
            return 0

    # We have made an empty list where we will add the threesome.
    # We start a loop to look through all the dices. If the count of the dice with the same number is equal or
    # bigger to 3 AND the account of the same number dice inside the threesome list is minor than 3, we append
    # the dice to the threesome list. Finally we return the sumative of the list called threesome

    @staticmethod
    def three_of_a_kind(*dice):
        threesome = []
        for num_dice in dice:
            if dice.count(num_dice) >= 3 and threesome.count(num_dice) < 3:
                threesome.append(num_dice)
        return sum(threesome)

    # We have made an empty list where we will add the four dice of the same number.
    # We start a loop to look through all the dices. If the count of the dice with the same number
    # is equal or bigger to 4 AND the account of the same number dice inside the poker list is minor than 4, we
    # append the dice to the poker list. Finally we return the sumative of the list called poker

    @staticmethod
    def four_of_a_kind(*dice):
        poker = []
        for num_dice in dice:
            if dice.count(num_dice) >= 4 and poker.count(num_dice) < 4:
                poker.append(num_dice)
        return sum(poker)

    # We have created a conditional where we sort the list to have it in numerical order from 1 to 5 (in case is a small straight) and we check
    # with a condition if it's the same than a list from 1 to 5, in case it's true we just return a sumative of all numbers and in case is
    # false we return a 0

    @staticmethod
    def smallStraight(*dice):
        if sorted(dice) == list(range(1, 6)):
            return sum(dice)
        else:
            return 0

    # We have created a conditional where we sort the list to
    # have in numerical order from 2 to 6 (in case is a large straight) and we check with a condition if it's
    # the same than a list from 2 to 6, in case it's true we just return a sumative of all numbers and in case
    # is false we return a 0
    @staticmethod
    def largeStraight(*dice):
        if sorted(dice) == list(range(2, 7)):
            return sum(dice)
        else:
            return 0

    # We have made a loop to look through all the dice numbers. If the dice account is equal to 3 or to 2 means
    # that we have a threesome or a pair and we just want to continue
    # looping through all the dices, in case in the condition we obtain a "False" result means that we are not having a
    # threesome and a pair to be able to make a full house, in this case we just return a 0. If it finish the
    # loop without get back a "False" means that we have a full house and we return a sumative of the all_dice

    @staticmethod
    def fullHouse(*dice):
        for num_dice in dice:
            if dice.count(num_dice) == 3 or dice.count(num_dice) == 2:
                continue
            else:
                return 0
        return sum(dice)
