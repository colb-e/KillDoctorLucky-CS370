import pygame
import random


class deck:

    num_of_cards = 0
    
    '''
    ** Notes for card values **
    type: move, weapon or fail
    value: the number value of the card
    room: either the room a weapon card has a bonus in or a move card specifies | 'none' by default
    bonus_value: a attack card will have this attack value if it the current room is equal to the room value on the card | 0 by default
    luck: holds the value of luck, equal to value on card if type is fail | 0 by default
    inPlay: true or false | false by default
    inDiscard: true or false | false by default
    playerHand: Will have num value of the player that has this card | 0 by default
    '''
    def __init__(self, type, value, room, bonus_value, luck, inPlay, inDiscard, playerHand):
        self.type = type 
        self.value = value 
        self.room = room 
        self.bonus_value = bonus_value 
        self.luck = luck 
        self.inPlay = inPlay 
        self.inDiscard = inDiscard 
        self.playerHand = playerHand 

        deck.num_of_cards += 1 # will add to sum of cards when a card is created


    def createDeck():

        # Move cards
        card1 = deck('move', 2, 12, 0, 2, False, False, 0)
        card2 = deck('move', 2, 17, 0, 2, False, False, 0)
        card3 = deck('move', 1, 13, 0, 1, False, False, 0)
        card4 = deck('move', 1, 8, 0, 0, False, False, 0)
        card5 = deck('move', 1, 6, 0, 2, False, False, 0)
        card6 = deck('move', 1, 2, 0, 0, False, False, 0)
        card7 = deck('move', 1, 24, 0, 2, False, False, 0)
        card8 = deck('move', 2, 1, 0, 1, False, False, 0)
        card9 = deck('move', 2, 23, 0, 0, False, False, 0)
        card10 = deck('move', 1, 15, 0, 2, False, False, 0)
        card11 = deck('move', 1, 21, 0, 0, False, False, 0)
        card12 = deck('move', 2, 22, 0, 1, False, False, 0)
        card13 = deck('move', 1, 3, 0, 2, False, False, 0)
        card14 = deck('move', 1, 9, 0, 2, False, False, 0)
        card15 = deck('move', 1, 20, 0, 2, False, False, 0)
        card16 = deck('move', 2, 4, 0, 1, False, False, 0)
        card17 = deck('move', 1, 18, 0, 0, False, False, 0)
        card18 = deck('move', 1, 14, 0, 0, False, False, 0)
        card19 = deck('move', 1, 5, 0, 0, False, False, 0)
        card20 = deck('move', 1, 10, 0, 1, False, False, 0)
        card21 = deck('move', 1, 11, 0, 0, False, False, 0)
        card22 = deck('move', 1, 19, 0, 1, False, False, 0)
        card23 = deck('move', 1, 16, 0, 1, False, False, 0)
        card24 = deck('move', 2, 7, 0, 1, False, False, 0)

        # Weapon cards

    def cardsInPlay(self):
        pass


deck.createDeck()
print(deck.num_of_cards)


