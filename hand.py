from card import Card


class Hand:
    """ Рука игрока"""

    def __init__(self, cards: list[Card] | None = None):
        self.chains = [] if cards is None else self.build_chains(cards)
        self.chips = 11

    def append(self, card):
        cards = [element for row in self.chains for element in row]
        cards.append(card)
        self.chains = self.build_chains(cards)

    """ Метод для построения цепи карт в руке"""

    @staticmethod
    def build_chains(cards):
        chains = []
        sorted_numbers = sorted(cards, reverse=True)
        current_chain = [sorted_numbers[0]]
        for i in range(1, len(sorted_numbers)):
            if sorted_numbers[i] == current_chain[-1] - 1:
                current_chain.append(sorted_numbers[i])
            else:
                chains.append(current_chain)
                current_chain = [sorted_numbers[i]]
        chains.append(current_chain)
        return chains

    def __repr__(self):
        """ 1, 9, 4, 5  """

    """ Метод подсчёта очков"""
    def sum(self):
        sum = 0
        for i in range(len(self.chains)):
            sum += int(self.chains[i][-1])
        return sum - self.chips

    def add_card(self, card: Card):
        """ Добавляет карту в руку. """
        self.chips += card.chips
        self.append(card)
