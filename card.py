import pygame
import random

class Card:

    cardCount = 0

    def __init__(self, card_type, value, room_index, bonus_value, luck, image_name):
        # Card Values
        self.card_type = card_type # Move, Attack, Fail
        self.value = value # numerical value on card
        self.room_index = room_index # will store room number if any room provided
        self.bonus_value = bonus_value # will store bonus value if any provided
        self.luck = luck # given luck value if any
        
        

        # Card organization
        self.playerHand = None
        self.inPlay = False
        self.inDiscard = False
        Card.cardCount += 1 

        # Card Display
        self.image = pygame.image.load('images/cards/' + image_name).convert()

    def createDeck():
        deck = []

        # Movement Cards
        deck.append(Card('move', 2, 11, 0, 2, 'moveMaster.jpg'))
        deck.append(Card('move', 2, 16, 0, 2, 'none.jpg'))
        deck.append(Card('move', 1, 12, 0, 1, 'none.jpg'))
        deck.append(Card('move', 1, 7, 0, 0, 'none.jpg'))
        deck.append(Card('move', 1, 5, 0, 2, 'none.jpg'))
        deck.append(Card('move', 1, 1, 0, 0, 'none.jpg'))
        deck.append(Card('move', 1, 23, 0, 2, 'none.jpg'))
        deck.append(Card('move', 2, 0, 0, 1, 'none.jpg'))
        deck.append(Card('move', 2, 22, 0, 0, 'none.jpg'))
        deck.append(Card('move', 1, 14, 0, 2, 'none.jpg'))
        deck.append(Card('move', 1, 20, 0, 0, 'none.jpg'))
        deck.append(Card('move', 2, 21, 0, 1, 'none.jpg'))
        deck.append(Card('move', 1, 2, 0, 2, 'none.jpg'))
        deck.append(Card('move', 1, 8, 0, 2, 'none.jpg'))
        deck.append(Card('move', 1, 19, 0, 2, 'none.jpg'))
        deck.append(Card('move', 2, 3, 0, 1, 'none.jpg'))
        deck.append(Card('move', 1, 17, 0, 0, 'none.jpg'))
        deck.append(Card('move', 1, 13, 0, 0, 'none.jpg'))
        deck.append(Card('move', 1, 4, 0, 0, 'none.jpg'))
        deck.append(Card('move', 1, 9, 0, 1, 'none.jpg'))
        deck.append(Card('move', 1, 10, 0, 0, 'none.jpg'))
        deck.append(Card('move', 1, 18, 0, 1, 'none.jpg'))
        deck.append(Card('move', 1, 15, 0, 1, 'none.jpg'))
        deck.append(Card('move', 2, 6, 0, 1, 'none.jpg'))

        random.shuffle(deck)

        return deck
    
    def showCard(self, surface, x, y, scale):
        surface_W, surface_L = surface.get_size()
        card_W, card_L = self.image.get_size()
        card_W, card_L = card_W * scale, card_L * scale
        image = pygame.transform.scale(self.image, (card_W, card_L))

        card_x = (surface_W - card_W) // x
        card_y = (surface_L - card_L) // y
        surface.blit(image, (card_x, card_y))