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
        #deck.append(Card('move', 2, 11, 0, 2, 'moveMaster.jpg'))
        #deck.append(Card('move', 2, 16, 0, 2, 'none.jpg'))
        #deck.append(Card('move', 1, 12, 0, 1, 'none.jpg'))
        #deck.append(Card('move', 1, 7, 0, 0, 'none.jpg'))
        #deck.append(Card('move', 1, 5, 0, 2, 'none.jpg'))
        #deck.append(Card('move', 1, 1, 0, 0, 'none.jpg'))
        #deck.append(Card('move', 1, 23, 0, 2, 'none.jpg'))
        #deck.append(Card('move', 2, 0, 0, 1, 'none.jpg'))
        # deck.append(Card('move', 2, 22, 0, 0, 'none.jpg'))
        #deck.append(Card('move', 1, 14, 0, 2, 'none.jpg'))
        #deck.append(Card('move', 1, 20, 0, 0, 'none.jpg'))
        #deck.append(Card('move', 2, 21, 0, 1, 'none.jpg'))
        #deck.append(Card('move', 1, 2, 0, 2, 'none.jpg'))
        #deck.append(Card('move', 1, 8, 0, 2, 'none.jpg'))
        #deck.append(Card('move', 1, 19, 0, 2, 'none.jpg'))
        #deck.append(Card('move', 2, 3, 0, 1, 'none.jpg'))
        #deck.append(Card('move', 1, 17, 0, 0, 'none.jpg'))
        #deck.append(Card('move', 1, 13, 0, 0, 'none.jpg'))
        #deck.append(Card('move', 1, 4, 0, 0, 'none.jpg'))
        #deck.append(Card('move', 1, 9, 0, 1, 'none.jpg'))
        #deck.append(Card('move', 1, 10, 0, 0, 'none.jpg'))
        #deck.append(Card('move', 1, 18, 0, 1, 'none.jpg'))
        #deck.append(Card('move', 1, 15, 0, 1, 'none.jpg'))
        #deck.append(Card('move', 2, 6, 0, 1, 'none.jpg'))

        # Movement Cards
        # type, value, index, bonus, luck, image
        deck.append(Card('move', 2, 0, 0, 1, 'move1.jpg')) # Drawing Room
        deck.append(Card('move', 1, 1, 0, 0, 'move2.jpg')) # Parlor
        deck.append(Card('move', 1, 2, 0, 2, 'move3.jpg')) # Billard Room
        deck.append(Card('move', 2, 3, 0, 1, 'move4.jpg')) # Dining Hall 
        deck.append(Card('move', 1, 4, 0, 0, 'move5.jpg')) # Sitting Room 
        deck.append(Card('move', 1, 5, 0, 2, 'move6.jpg')) # Trophy Room
        deck.append(Card('move', 2, 6, 0, 1, 'move7.jpg')) # Green House
        deck.append(Card('move', 1, 7, 0, 0, 'move8.jpg')) # Winter Garden
        deck.append(Card('move', 1, 8, 0, 2, 'move9.jpg')) # Wine Cellar
        deck.append(Card('move', 1, 9, 0, 1, 'move10.jpg')) # Kitchen
        deck.append(Card('move', 1, 10, 0, 0, 'move11.jpg')) # Lancaster Room
        deck.append(Card('move', 2, 11, 0, 2, 'move12.jpg')) # Master Suite
        deck.append(Card('move', 1, 12, 0, 1, 'move13.jpg')) # Nursery 
        deck.append(Card('move', 1, 13, 0, 0, 'move14.jpg')) # Armory
        deck.append(Card('move', 1, 14, 0, 2, 'move15.jpg')) # Gallery
        deck.append(Card('move', 1, 15, 0, 1, 'move16.jpg')) # Library
        deck.append(Card('move', 2, 16, 0, 2, 'move17.jpg')) # Tennesse Room
        deck.append(Card('move', 1, 17, 0, 0, 'move18.jpg')) # Lilac Room
        deck.append(Card('move', 1, 18, 0, 1, 'move19.jpg')) # Servants Quarters
        deck.append(Card('move', 1, 19, 0, 2, 'move20.jpg')) # White Room
        deck.append(Card('move', 1, 20, 0, 0, 'move21.jpg')) # Hedge Maze
        deck.append(Card('move', 2, 21, 0, 1, 'move22.jpg')) # Carrige House
        deck.append(Card('move', 2, 22, 0, 0, 'move23.jpg')) # Piazza
        deck.append(Card('move', 1, 23, 0, 2, 'move24.jpg')) # Foyer

        # Weapon Cards
        # type, value, index, bonus, luck, image
        deck.append(Card('weapon', 3, 0, 6, 0, 'attk1.jpg'))
        deck.append(Card('weapon', 2, 1, 4, 2, 'attk2.jpg'))
        deck.append(Card('weapon', 3, 2, 5, 1, 'attk3.jpg'))
        deck.append(Card('weapon', 2, 3, 5, 0, 'attk4.jpg'))
        deck.append(Card('weapon', 2, 4, 4, 2, 'attk5.jpg'))
        deck.append(Card('weapon', 2, 5, 5, 1, 'attk6.jpg'))
        deck.append(Card('weapon', 3, 6, 5, 0, 'attk7.jpg'))
        deck.append(Card('weapon', 2, 7, 4, 2, 'attk8.jpg'))
        deck.append(Card('weapon', 2, 8, 5, 1, 'attk9.jpg'))
        deck.append(Card('weapon', 2, 9, 4, 2, 'attk10.jpg'))
        deck.append(Card('weapon', 2, 10, 4, 2, 'attk11.jpg'))
        deck.append(Card('weapon', 2, 11, 5, 1, 'attk12.jpg'))
        deck.append(Card('weapon', 2, 12, 5, 1, 'attk13.jpg'))
        deck.append(Card('weapon', 3, 13, 6, 0, 'attk14.jpg'))
        deck.append(Card('weapon', 2, 14, 6, 0, 'attk15.jpg'))
        deck.append(Card('weapon', 2, 15, 4, 2, 'attk16.jpg'))
        deck.append(Card('weapon', 2, 16, 6, 1, 'attk17.jpg'))
        deck.append(Card('weapon', 2, 17, 4, 0, 'attk18.jpg'))
        deck.append(Card('weapon', 2, 18, 4, 2, 'attk19.jpg'))
        deck.append(Card('weapon', 2, 19, 4, 1, 'attk20.jpg'))
        deck.append(Card('weapon', 3, 20, 6, 0, 'attk21.jpg'))
        deck.append(Card('weapon', 2, 21, 5, 1, 'attk22.jpg'))
        deck.append(Card('weapon', 2, 22, 4, 2, 'attk23.jpg'))
        deck.append(Card('weapon', 2, 23, 6, 0, 'attk24.jpg'))

        # Fail Cards
        # type, value, index, bonus, luck, image
        deck.append(Card('fail', 1, 0, 0, 1, 'fail1bats.jpg'))
        deck.append(Card('fail', 1, 0, 0, 1, 'fail1ennui.jpg'))
        deck.append(Card('fail', 1, 0, 0, 1, 'fail1goodsir.jpg'))
        deck.append(Card('fail', 1, 0, 0, 1, 'fail1hiya.jpg'))
        deck.append(Card('fail', 1, 0, 0, 1, 'fail1mist.jpg'))
        deck.append(Card('fail', 1, 0, 0, 1, 'fail1music.jpg'))
        deck.append(Card('fail', 1, 0, 0, 1, 'fail1poof.jpg'))
        deck.append(Card('fail', 1, 0, 0, 1, 'fail1regret.jpg'))
        deck.append(Card('fail', 1, 0, 0, 1, 'fail1thought.jpg'))
        deck.append(Card('fail', 1, 0, 0, 1, 'fail1tricklight.jpg'))
        deck.append(Card('fail', 2, 0, 0, 2, 'fail2inexplicable.jpg'))
        deck.append(Card('fail', 2, 0, 0, 2, 'fail2oops.jpg'))
        deck.append(Card('fail', 2, 0, 0, 2, 'fail2umm.jpg'))
        deck.append(Card('fail', 2, 0, 0, 2, 'fail2tumbler.jpg'))
        deck.append(Card('fail', 2, 0, 0, 2, 'fail2doubt.jpg'))
        deck.append(Card('fail', 2, 0, 0, 2, 'fail2turnabout.jpg'))
        deck.append(Card('fail', 3, 0, 0, 3, 'fail3cross.jpg'))
        deck.append(Card('fail', 3, 0, 0, 3, 'fail3immunity.jpg'))
        deck.append(Card('fail', 3, 0, 0, 3, 'fail3pledge.jpg'))
        deck.append(Card('fail', 3, 0, 0, 3, 'fail3feline.jpg'))
        deck.append(Card('fail', 4, 0, 0, 4, 'fail4shadows.jpg'))
        deck.append(Card('fail', 4, 0, 0, 4, 'fail4prestige.jpg'))
        deck.append(Card('fail', 4, 0, 0, 4, 'fail4blunder.jpg'))
        deck.append(Card('fail', 4, 0, 0, 4, 'fail4blocked.jpg'))

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
        

    def showCardTest(self, surface, percent_x, percent_y, scale):
        #resize image
        surface_W, surface_L = surface.get_size()
        card_W, card_L = self.image.get_size()
        card_W, card_L = card_W * scale, card_L * scale
        image = pygame.transform.scale(self.image, (card_W, card_L))

        #place image

        card_x = surface_W * percent_x
        card_y = surface_L * percent_y

        surface.blit(image, (card_x, card_y))