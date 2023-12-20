from card import Card
from hand import Hand


class Player:
    def __init__(self, name: str, hand: Hand | None = None, interactive_player: bool = False):
        self.name = name
        self.hand = Hand([] if hand is None else hand)
        self.interactive = interactive_player

    def __repr__(self):
        return f'{self.name}: {self.hand}'

    def add_card(self, card: Card):
        self.hand.add_card(card)

    def skip_turn(self):
        self.hand.chips -= 1

    @staticmethod
    def create(player_dict: dict):
        """ {'name': 'Bob', 'hand': ' 7, 8, 5} """
        return Player(player_dict['name'], Hand.create(player_dict['hand']))

