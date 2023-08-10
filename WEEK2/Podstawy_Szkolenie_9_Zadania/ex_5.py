import random
from random import shuffle


class Card:
    def __init__(self, value, figure):
        self.value = value
        self.figure = figure


class Deck:
    CARD_VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    CARD_FIGURES = ["♠", "♣", "♦", "♥"]

    def __init__(self):
        self.cards = []
        self.create_deck()
        self.shuffle()

    def create_deck(self):
        for value in Deck.CARD_VALUES:
            for figure in Deck.CARD_FIGURES:
                self.cards.append(Card(value, figure))

    def shuffle(self):
        random.shuffle(self.cards)
        print(self.cards)

    def deal(self):
        card = self.cards.pop(-1)
        print(card)
        print(self.cards)


def main():
    deck = Deck()
    deck.shuffle()
    deck.deal()


if __name__ == "__main__":
    main()
