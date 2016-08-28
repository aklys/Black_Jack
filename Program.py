import Card_Deck

Current_Cards = Card_Deck.Deck()

Current_Cards.generate_std_deck()
Current_Cards.add_jokers(2)

print(Current_Cards.deck)

Current_Cards.generate_std_deck()

print(Current_Cards.deck)