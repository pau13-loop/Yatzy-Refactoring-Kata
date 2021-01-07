class Yatzy():

    def __init__(self, *dice):
        self.dice = list(dice)

    @staticmethod
    def chance(*dice):
        return sum(dice)

    @staticmethod
    def yatzy(*dice):
        for num_dice in dice:
            if num_dice != dice[0]:
                return 0
        return 50

    @staticmethod
    def ones(*dice):
        return (dice.count(1))

    @staticmethod
    def twos(*dice):
        return (dice.count(2) * 2)

    @staticmethod
    def threes(*dice):
        return (dice.count(3) * 3)

    @staticmethod
    def fours(*dice):
        return (dice.count(4) * 4)

    @staticmethod
    def fives(*dice):
        return (dice.count(5) * 5)

    @staticmethod
    def sixes(*dice):
        return (dice.count(6) * 6)

    @staticmethod
    def one_pair(*dice):
        current_pair = 0
        for num_dice in dice:
            if dice.count(num_dice) == 2 and num_dice >= current_pair:
                current_pair = num_dice
        return (current_pair * 2)

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

    @staticmethod
    def three_of_a_kind(*dice):
        threesome = []
        for num_dice in dice:
            if dice.count(num_dice) >= 3 and threesome.count(num_dice) < 3:
                threesome.append(num_dice)
        return sum(threesome)

    @staticmethod
    def four_of_a_kind(*dice):
        poker = []
        for num_dice in dice:
            if dice.count(num_dice) >= 4 and poker.count(num_dice) < 4:
                poker.append(num_dice)
        return sum(poker)

    @staticmethod
    def smallStraight(*dice):
        if sorted(dice) == list(range(1, 6)):
            return sum(dice)
        else:
            return 0

    @staticmethod
    def largeStraight(*dice):
        if sorted(dice) == list(range(2, 7)):
            return sum(dice)
        else:
            return 0

    @staticmethod
    def fullHouse(*dice):
        for num_dice in dice:
            if dice.count(num_dice) == 3 or dice.count(num_dice) == 2:
                continue
            else:
                return 0
        return sum(dice)
