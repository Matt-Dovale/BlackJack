from deck import Deck
from player import Player
from cards import Card
import time

deck = Deck()
deck.shuffle()

dealer = Player('Dealer')
player1 = Player('Matt')

while True:
    #Begin the round by dealing the cards
    bust = False

    player1.give_hand(deck)
    dealer.give_hand(deck)

    print('\nDealers Hand:')
    dealer.show_dealer_cards()

    #Player Turn
    while player1.hand_value() < 21:
        print('\nYour hand: ')
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
            bust = True
            time.sleep(2)

    #Dealers turn
    while dealer.hand_value() < 17:
        print('\nDealers card:')
        dealer.show_hand()
        print(f'Current Value: {dealer.hand_value()}')

        dealer.draw_card(deck)

        time.sleep(2)
    else:
        print('\nDealers card:')
        dealer.show_hand()
        print(f'Current Value: {dealer.hand_value()}')

    if not bust and dealer.hand_value() < player1.hand_value():
        print('You Win!')
    else:
        print('You Lost')
    
    quit = input('Play again?: ')

    if quit.lower() == 'no':
        print("Thank you for playing")
        break

    player1.return_hand()
    dealer.return_hand()

    deck.shuffle()


    