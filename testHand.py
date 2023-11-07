from card import Card
from hand import Hand


def test_CardChain():
    hand = Hand([5, 6, 8, 10, 9, 7, 3, 2, 1])
    assert hand.chains == [[10, 9, 8, 7, 6, 5], [3, 2, 1]]
    assert hand.sum == -5

def test_sum():
    hand = Hand([5, 6, 8, 10, 9, 7, 3, 2, 1])
    a= hand.sum()
    assert a == -5
def test_append():
    hand = Hand([5, 6, 8, 10, 9, 7, 3, 2, 1])
    assert hand.chains == [[10, 9, 8, 7, 6, 5], [3, 2, 1]]
    hand.append(22)
    assert hand.chains == [[22],[10, 9, 8, 7, 6, 5], [3, 2, 1]]
