"""Game Module"""
from game.card import Card

class Director:
    """A person who directs the game.

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        cards (List[Card]): A list of Card instances.
        is_playing (boolean): Whether or not the game is being played.
        guess (string): The player's guess
        score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self.cards = []
        self.is_playing = True
        self.guess = ""
        self.score = 300

        for i in range(2):
            card = Card()
            self.cards.append(card)

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.take_guess()
            self.do_updates()
            self.do_outputs()

    def take_guess(self):
        """Ask the user to guess higher or lower.

        Args:
            self (Director): An instance of Director.
        """
        print (f"The card is : {self.cards[0].value}")
        self.guess = input("Higher or lower? [h/l] ").lower()

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        print(f"Next card was: {self.cards[1].value}")

        if ((self.cards[0].value > self.cards[1].value) and self.guess == "l"
        or (self.cards[0].value < self.cards[1].value and self.guess == "h")):
            self.score += 100
        else: self.score -= 75

        self.cards.pop(0)
        self.cards.append(Card())

    def do_outputs(self):
        """Displays the score. Also asks the player if they want to draw again.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        print(f"Your score is: {self.score}")
        self.is_playing = (self.score > 0 and input("Play again? [y/n]").lower() != "n")
        print()
        