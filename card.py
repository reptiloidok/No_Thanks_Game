class Card:
    NUMBERS = list(range(3, 36))

    def __init__(self, number, chips=0):
        if 3 <= number <= 35:
            self.number = number
        else:
            raise ValueError(f'Wrong number {number}')
        self.chips = chips

    def __repr__(self):
        return f'{self.number}'

    def __eq__(self, other):
        return self.number == other

    def __it__(self, other):
        return self.number < other

    def __gt__(self, other):
        return self.number > other

    def __sub__(self, other):
        return self.number - other

    @staticmethod
    def create(number: str | int):
        """ По тексту вида '4' возвращается карта Card(4)."""
        number = int(number)
        return Card(number)

    @staticmethod
    def card_list(numbers: set):
        return [Card.create(number) for number in numbers]

    @staticmethod
    def all_cards():
        """ Все карты для создания колоды. """
        return [Card(number) for number in Card.NUMBERS]
