from card import Card
from hand import Hand


def test_CardChain():
    hand = Hand([5, 6, 8, 10, 9, 7, 3, 2, 1])
    assert hand.chains == [[10, 9, 8, 7, 6, 5], [3, 2, 1]]

def test_sum():
    hand = Hand([5, 6, 8, 10, 9, 7, 3, 2, 1])
    a= hand.summ()
    assert a == -5
def test_append():
    hand = Hand([5, 6, 8, 10, 9, 7, 3, 2, 1])
    assert hand.chains == [[10, 9, 8, 7, 6, 5], [3, 2, 1]]
    a = Card(22, 11)
    hand.append(a)
    assert hand.chains == [[22],[10, 9, 8, 7, 6, 5], [3, 2, 1]]
def test_is_chain():
    hand = Hand([5, 6, 8, 10, 9, 7, 3, 2, 1])
    a = Card(4, 11)
    assert (hand.is_chain(a))
    assert hand.chains == [[10, 9, 8, 7, 6, 5], [3, 2, 1]]
