import Card_Deck
import time


def main():
    players, deck = init_game()

    print(players[:-2])

    for player in players:
        actions(player, deck)


def init_game():

    num_decks = int(input('How many decks do you want to use? '))

    deck = Card_Deck.Deck()
    for i in range(num_decks):
        deck.generate_std_deck()
    deck.shuffle()

    num_players = int(input("How many people are playing? "))
    players = []

    for i in range(num_players):
        name = input("What is the name of Player {}? ".format(i+1))
        players.append(Card_Deck.Hand(name))

    players.append(Card_Deck.Hand("Dealer"))

    # two initial rounds of cards dealt out
    for i in range(2):
        for player in players:
            deck.deal_card(player)
            time.sleep(2)

    return players, deck


def actions(player, deck):

    print("{} your current hand is:\n {}".format(player.owner, player.hand))

    if player[0][1:] == player[1][1:]:
        action = input('Do you want to split (Y/N)? ')
        if action.lower() == "y":


    action = input('{} would like to [H]it, [S]tand or [C]heck hand: '.format(player.owner))

    while action.lower() != 's':
        if action.lower() == 'h':
            deck.deal_card(player)
            score = hand_value(player)
            if score > 21:
                print('{}, I\'m sorry to say you went bust with a score of {}'
                      .format(player.owner, score))
                break
            elif score == 21:
                print('{} is on the money with 21. Woop! Woop!'.format(player.owner))
                break

        elif action.lower() == 'c':
            print(player.hand)
        action = input('{} would like to [H]it, [S]tand or [C]heck hand: '.format(player.owner))


def hand_value(player):
    score_high = 0
    score_low = 0
    for i in player.hand:
        if i.ref[1].lower() == "a":
            score_high += 11
            score_low += 1
        elif i.ref[1].lower() == "j" or i.ref[1].lower() == "q" or i.ref[1].lower() == "k":
            score_high += 10
            score_low += 10
        else:
            score_high += int(i.ref[1:])
            score_low += int(i.ref[1:])

    if score_high == score_low:
        return score_high
    elif score_high > 21:
        return score_low


if __name__ == '__main__':
    main()
