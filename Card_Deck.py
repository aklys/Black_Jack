import random


class Deck:

    def __init__(self):
        self.deck = []

    def generate_std_deck(self):
        std_cards = {"Suits": ["S", "C", "H", "D"],
                     "Value": ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                               "J", "Q", "K"]}

        for i in std_cards["Suits"]:
            for j in std_cards["Value"]:
                self.deck.append(StdCard(i + j))

    def add_jokers(self, num):
        for i in range(num):
            self.deck.append(StdCard("JJ"))

    def shuffle(self, num_shuffles = 1):
        for i in range(num_shuffles):
            random.shuffle(self.deck)

    def deal_card(self, hand):
        dealt_card = random.choice(self.deck)

        print("{} has been dealt a card.".format(hand.owner))
        hand.add_card(dealt_card)
        self.deck.remove(dealt_card)


class StdCard:

    def __init__(self, ref):
        self.ref = ref

    def __repr__(self):
        names = {"A": "Ace", "2": "Two", "3": "Three", "4": "Four",
                 "5": "Five", "6": "Six", "7": "Seven", "8": "Eight",
                 "9": "Nine", "10": "Ten", "J": "Jack", "Q": "Queen", "K": "King",
                 "JJ": "Joker", "S": "Spades", "C": "Clubs", "H": "Hearts", "D": "Diamonds"}

        if self.ref == "JJ":
            return "Joker"
        else:
            return names[self.ref[1:]] + " of " + names[self.ref[0]]


class Hand:

    def __init__(self, owner):
        self.hand = []
        self.owner = owner

    def add_card(self, card):
        self.hand.append(card)

    def __repr__(self):
        return "Currently {} is holding:\n {}".format(self.owner, self.hand)
