# Template Method Pattern
# The template method pattern allows to define a "skeleton" for an algorithm, while then providing different concrete
# implementations. The skeleton is so then a template for an algorithm. The concrete implementations are then kept in
# subclasses, so the template method pattern works very similar to the strategy and abstract factory templates.
from abc import ABC
from distutils.command.check import check


class Game(ABC):
    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.current_player = 0

    # this is the template method
    def run(self):
        self.start()
        while not self.have_winner:
            self.take_turn()
        print(f"Player {self.winning_player} has won")
        self.restart()

    @property
    def have_winner(self): pass

    def take_turn(self): pass

    def start(self): pass

    def restart(self):
        print("Restarting the game")

    @property
    def winning_player(self): pass


class Chess(Game):
    def __init__(self):
        super().__init__(2)
        self.max_turns = 10
        self.turn = 1

    def start(self):
       print(f"Starting a game of chess with {self.number_of_players} players")

    @property
    def have_winner(self):
        return self.turn == self.max_turns

    def take_turn(self):
        print(f"Turn {self.turn} taken by player {self.current_player}")
        self.turn += 1
        self.current_player = 1 - self.current_player

    @property
    def winning_player(self):
        return self.current_player


if __name__ == "__main__":
    chess = Chess()
    chess.run()