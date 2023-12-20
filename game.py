from deck import Deck
from player import Player


class Game:
    DEFAULT_PLAYER_NAMES = ['Bob', 'Mike', 'Ivan']
    DECK_INDEX = -1

    def __init__(self, player_names: list[str] | None = None):
        if player_names is None:
            player_names = Game.DEFAULT_PLAYER_NAMES
        self.deck = Deck()
        self.players = [Player(name) for name in player_names]
        self.players[0].interactive = True
        self.player_index = 0
        self.table_card = self.deck.draw()
        self.wait_interactive_action = False

    @staticmethod
    def create(game_dict: dict):
        g = Game([])  # без игроков
        g.deck = Deck.create(game_dict['deck'])
        g.players = [Player(p) for p in game_dict['players']]
        g.player_index = int(game_dict['player_index'])
        return g


    @property
    def current_player(self):
        return self.players[self.player_index]

    def player_wait(self):
        input('введите что-нибудь для продолжения')

    def choose_move(self):
        """ Выбор игрока, что он будет делать"""
        print('введите 1, если хотите взять карту')
        print('введите 2, если не хотите взять карту')
        while True:
            try:
                num = int(input('Введите число: '))
                if 1 <= num <= 2:
                    break
                else:
                    print("Ошибка: введено некорректное значение. Попробуйте еще раз.")
            except ValueError:
                print("Ошибка: введено некорректное значение. Попробуйте еще раз.")

        return num

    def player_draw_card(self):
        """ Для бота и когда берут карту со стола"""
        self.current_player.hand.add_card(self.table_card)
        print(f'Игрок {self.current_player.name} взял карту {self.table_card} cо стола')
        self.table_card = self.deck.draw()
        print(f'карта на столе: {self.table_card}')
        print(self.current_player)

    def skip_turn(self):
        self.current_player.skip_turn()
        self.table_card.chips += 1

    def run(self):

        running = True
        while running:
            print(f'карта на столе: {self.table_card}, кол-во фишек на ней {self.table_card.chips}')
            print(self.current_player)
            hand = self.current_player.hand
            print(hand)
            if self.current_player.hand.chips == 0:
                print(f"{self.current_player.name} берет карту")
            else:
                print(f"{self.current_player.name} выбирает что будет делать")
                move = self.choose_move()
                if move == 1:
                    self.player_draw_card()
                else:
                    self.skip_turn()
            if len(self.deck) == 0:
                self.congratulations()
            self.next_player()

    def next_player(self):
        """ Переходим к следующему игроку. """
        self.player_index = (self.player_index + 1) % len(self.players)

    def congratulations(self):
        maximum = 0
        winner_name = self.players[0].name
        for player in self.players:
            value = player.hand.summ()
            print(f'Игрок {player.name} набрал {value} очков')
            if value > maximum:
                maximum = value
                winner_name = player.name
        print(f'Конец игры, победитель! {winner_name}')
        print("")
        print("")
        self.player_wait()


def new_game():
    from random import seed
    seed(7)
    g = Game(['Bob', 'Mike', 'Ivan'])
    g.run()


new_game()
