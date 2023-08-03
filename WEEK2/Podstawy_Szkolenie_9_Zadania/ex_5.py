import random
from random import shuffle


class Deck:
    def __init__(self):
        card_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        card_figures = ["♠", "♣", "♦", "♥"]

        self.cards = []
        for value in card_values:
            for figure in card_figures:
                card = value + " " + figure
                self.cards.append(card)

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
