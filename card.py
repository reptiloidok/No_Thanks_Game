class Card:
    NUMBERS = list(range(3, 36))

    def __init__(self, number):
        if 3 <= number <= 35:
            self.number = number
        else:
            raise ValueError(f'Wrong number {number}')

    def __repr__(self):
        return f'{self.number}'

    @staticmethod
    def create(number: str | int):
        """ По тексту вида '4' возвращается карта Card(4)."""
        number = int(number)
        return Card(number)

    @staticmethod
    def card_list(text: str | list):
        return [Card.create(word) for word in text]

    @staticmethod
    def all_cards():
        """ Все карты для создания колоды. """
        return [Card(number) for number in Card.NUMBERS]
