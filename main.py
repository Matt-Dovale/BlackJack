from deck import Deck
from player import Player
from cards import Card

deck = Deck()
deck.shuffle()

dealer = Player('Dealer')
player1 = Player('Matt')

while True:
    #Begin the round by dealing the cards
    player1.give_hand(deck)
    dealer.give_hand(deck)

    print('Your hand: ')
    player1.show_hand()

    print('\nDealers Hand:')
    dealer.show_dealer_cards()

    #Player Turn
    while player1.hand_value() < 21:
        print('Your hand: ')
        player1.show_hand()
        print(f'Current Value: {player1.hand_value()}')

        if player1.hand_value() == 21:
            print('BLACKJACK!')
            break
        
        move = input("Hit or Stand? ")
        if move.lower() == 'hit':
            player1.draw_card(deck)
        
        if move.lower() == 'stand':
            break
    else:
        if player1.hand_value() > 21:
            player1.show_hand()
            print(f'Current Value: {player1.hand_value()}')
            print('Bust')

    quit = input('Play again?: ')
    if quit.lower() == 'no':
        print("Thank you for playing")
        break

    player1.return_hand()
    dealer.return_hand()

    deck.shuffle()


    