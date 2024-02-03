import pygame
import random
from sys import exit

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Kill Doctor Lucky') # title for game

class Card:
    def __init__(self, type, value, room, bonus_value, luck):
        self.type = type # attack, movement, fail
        self.value = value # each card has a numerical value no matter the type, the type will decide what the value is used for
        self.room = room # will be used if the card has a room assigned for direct movement or attack bonus 
        self.bonus_value = bonus_value # if a card has a bonus value for attacking it will be stored here
        self.luck = luck # will hold the value of the luck for the card 
        
        
    

test_font = pygame.font.Font('fonts/m5x7.ttf', 50) #(font type, font size) None is the default

# *** Deciding the size of the player screen ***
# screen = pygame.display.set_mode((1000,1000)) # this will manually set the screen size

# this grabs the users screen size and set he screen to that size
screen = pygame.display.set_mode()
screen_W, screen_L = screen.get_size()
screen = pygame.display.set_mode((screen_W,screen_L))


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


# *** Building the static scene ***
board = pygame.image.load("images/Board2.jpg").convert()
board = pygame.transform.scale(board, (screen_W,screen_L)).convert()

text_surface = test_font.render('Kill Doctor Lucky', True, 'Black').convert_alpha() #('insert text', True or False, 'color of text') The T or F is for anti aliasing, true usually, false if pixel art

# this will create a red box 
#test_surface = pygame.Surface((100,200)) #S must be a capital, pygame.Surface((w,h))
#test_surface.fill('Red')



rect_width, rect_height = 50, 30
rect_x, rect_y = (screen_W - rect_width) // 3.75, (screen_L - rect_height) // 4


# *** Main game loop ***
while True:
    #for all possible events (player input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print("Thank you for playing")
            exit()

    # DRAW ALL ELEMENTS
    # UPDATE EVERYTHING HERE
            
    #screen.blit(test_surface,(200,100)) #screen.blit(surface,position), the position isformatted like this: (x,y)
    
    screen.blit(board,(0,0))
    screen.blit(text_surface,(500,500))

    pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))

    pygame.display.update()
    clock.tick(60) # Maximum Framerate of 60