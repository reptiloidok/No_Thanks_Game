from card import Card


def test_init_valid_number():
    card = Card(4)
    assert card.number == 4


def test_repr():
    card = Card(7)
    assert card.__repr__() == '7'


def test_eq_same_number():
    card1 = Card(9)
    card2 = Card(9)
    assert card1.__eq__(card2) is True


def test_eq_different_number():
    card1 = Card(11)
    card2 = Card(13)
    assert card1.__eq__(card2) is False


def test_create():
    card = Card.create('4')
    assert card.number == 4


def test_card_list():
    cards = Card.card_list([5, 8, 11])
    assert len(cards) == 3
    assert cards.__repr__()=='[5, 8, 11]'



def test_all_cards():
    cards = Card.all_cards()
    assert len(cards) == 33
    assert cards[0].number == 3
    assert cards[-1].number == 35



