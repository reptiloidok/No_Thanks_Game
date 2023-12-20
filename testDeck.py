import pytest
from card import Card
from deck import Deck


def test_init_default():
    deck = Deck()
    assert len(deck.cards) == 23


def test_init_custom():
    cards = Card.card_list([4, 7, 10, 13])
    deck = Deck(cards)
    assert len(deck.cards) == 4
    assert deck.cards[0].number == 4
    assert deck.cards[3].number == 13


def test_repr():
    cards = Card.card_list({5, 6, 7, 8, 9})
    deck = Deck(cards)
    assert repr(deck) == '5 6 7 8 9'


def test_draw():
    cards = Card.card_list({5, 6, 7, 8, 9})
    deck = Deck(cards)
    card = deck.draw()
    assert len(deck.cards) == 4
    assert card.number == 9


def test_create():
    deck = Deck.create({5, 6, 7, 8, 9})
    assert len(deck.cards) == 5
    assert deck.cards[0].number == 5
    assert deck.cards[-1].number == 9
