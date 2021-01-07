from src.yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_chance():
    assert 15 == Yatzy.chance(2, 3, 4, 5, 1)
    assert 16 == Yatzy.chance(3, 3, 4, 5, 1)


def test_yatzy():
    assert 50 == Yatzy.yatzy(4, 4, 4, 4, 4)
    assert 50 == Yatzy.yatzy(6, 6, 6, 6, 6)
    assert 0 == Yatzy.yatzy(6, 6, 6, 6, 3)


def test_ones():
    assert Yatzy.ones(1, 2, 3, 4, 5) == 1
    assert 2 == Yatzy.ones(1, 2, 1, 4, 5)
    assert 0 == Yatzy.ones(6, 2, 2, 4, 5)
    assert 4 == Yatzy.ones(1, 2, 1, 1, 1)


def test_twos():
    assert 4 == Yatzy.twos(1, 2, 3, 2, 6)
    assert 10 == Yatzy.twos(2, 2, 2, 2, 2)


def test_threes():
    assert 6 == Yatzy.threes(1, 2, 3, 2, 3)
    assert 12 == Yatzy.threes(2, 3, 3, 3, 3)


def test_fours():
    assert 12 == Yatzy.fours(4, 4, 4, 5, 5)
    assert 8 == Yatzy.fours(4, 4, 5, 5, 5)
    assert 4 == Yatzy.fours(4, 5, 5, 5, 5)


def test_fives():
    assert 10 == Yatzy.fives(4, 4, 4, 5, 5)
    assert 15 == Yatzy.fives(4, 4, 5, 5, 5)
    assert 20 == Yatzy.fives(4, 5, 5, 5, 5)


def test_sixes():
    assert 0 == Yatzy.sixes(4, 4, 4, 5, 5)
    assert 6 == Yatzy.sixes(4, 4, 6, 5, 5)
    assert 18 == Yatzy.sixes(6, 5, 6, 6, 5)


def test_one_pair():
    assert 6 == Yatzy.one_pair(3, 4, 3, 5, 6)
    assert 10 == Yatzy.one_pair(5, 3, 3, 3, 5)
    assert 12 == Yatzy.one_pair(5, 3, 6, 6, 5)
    # Adding some more tests to make sure the new refactor works
    # Puting a pair in each extreme
    assert 2 == Yatzy.one_pair(1, 2, 3, 4, 1)
    # Adding a pair at the last two positions to check the index is not out of range
    assert 6 == Yatzy.one_pair(1, 2, 4, 3, 3)
    # Non possible pairs
    assert 0 == Yatzy.one_pair(1, 2, 3, 4, 5)
    # A threesome and a pair, should get just the pair of 2 that equal 4
    assert 4 == Yatzy.one_pair(1, 1, 2, 2, 1)


def test_two_Pair():
    assert 16 == Yatzy.two_pair(3, 3, 5, 4, 5)
    assert 18 == Yatzy.two_pair(3, 3, 6, 6, 6)
    assert 0 == Yatzy.two_pair(3, 3, 6, 5, 4)
    # A pair in each extreme
    assert 16 == Yatzy.two_pair(3, 3, 1, 5, 5)
    # A non possible pairs
    assert 0 == Yatzy.two_pair(1, 2, 3, 4, 5)


def test_three_of_a_kind():
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 4, 5)
    assert 15 == Yatzy.three_of_a_kind(5, 3, 5, 4, 5)
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 3, 5)
    # A pair instead be a threesome
    assert 0 == Yatzy.three_of_a_kind(2, 3, 4, 6, 6)
    # A double pair instead a threesome
    assert 0 == Yatzy.three_of_a_kind(2, 2, 5, 6, 6)
    # All different
    assert 0 == Yatzy.three_of_a_kind(1, 2, 3, 4, 5)
    # All the same
    assert 6 == Yatzy.three_of_a_kind(2, 2, 2, 2, 2)


def test_four_of_a_kind():
    assert 12 == Yatzy.four_of_a_kind(3, 3, 3, 3, 5)
    assert 20 == Yatzy.four_of_a_kind(5, 5, 5, 4, 5)
    assert 12 == Yatzy.four_of_a_kind(3, 3, 3, 3, 3)
    assert 0 == Yatzy.four_of_a_kind(3, 3, 3, 2, 1)


def test_smallStraight():
    assert 15 == Yatzy.smallStraight(1, 2, 3, 4, 5)
    assert 15 == Yatzy.smallStraight(2, 3, 4, 5, 1)
    assert 15 == Yatzy.smallStraight(3, 5, 2, 1, 4)
    assert 0 == Yatzy.smallStraight(1, 2, 2, 4, 5)
    # Large Straight
    assert 0 == Yatzy.smallStraight(2, 3, 4, 5, 6)


def test_largeStraight():
    assert 20 == Yatzy.largeStraight(6, 2, 3, 4, 5)
    assert 20 == Yatzy.largeStraight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.largeStraight(1, 2, 2, 4, 5)
    # Small Straight
    assert 0 == Yatzy.largeStraight(1, 2, 3, 4, 5)


def test_fullHouse():
    assert 18 == Yatzy.fullHouse(6, 2, 2, 2, 6)
    assert 0 == Yatzy.fullHouse(2, 3, 4, 5, 6)
    # Just a pair
    assert 0 == Yatzy.fullHouse(1, 2, 3, 4, 1)
    # Just a threesome
    assert 0 == Yatzy.fullHouse(2, 3, 4, 2, 2)
    # Poker
    assert 0 == Yatzy.fullHouse(1, 1, 1, 1, 2)
    # Repoker
    assert 0 == Yatzy.fullHouse(3, 3, 3, 3, 3)
