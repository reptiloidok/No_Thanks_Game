import random

from card import Card


class Deck:
    """ Колода карт"""

    def __init__(self, cards: list[Card] | None = None):
        if cards is None:
            self.cards = Card.all_cards()
            random.shuffle(self.cards)
            self.cards = self.cards[0: 23]
        else:
            self.cards = cards
            self.cards = self.cards[0: 23]

    def __repr__(self):
        """ 5, 6, 7, 8, 9 """
        return ' '.join([str(c) for c in self.cards])

    def draw(self):
        """ Взяли из колоды 1 карту и вернули ее."""
        card = self.cards.pop()
        return card

    @staticmethod
    def create(text: list):
        return Deck(Card.card_list(text))
