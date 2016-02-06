#7.1 CTCI: Design the data structures for a generic deck of cars. Explain how you would subclass the data structures to implement blackjack.

import random

class Card(object):
    suits = ('Clubs', 'Hearts', 'Spades', 'Diamonds')
    pips = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')

    def __init__(self, pip, suit):
        self.pip = pip
        self.suit = suit

    def __str__(self):
        return "%s %s" (self.pip, self.suit)


class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in Card.suits:
            for pip in Card.pips:
                card = Card(pip, suit)
                self.cards.append(card)

    def __str__(self):
        result = [str(card) for card in self.cards]
        return '\n'.join(result)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        self.shuffle()
        return self.cards.pop(0)

    def add_card(self, card):
        self.cards.append(card)
