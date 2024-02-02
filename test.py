import pygame
import random
from sys import exit
pygame.init()

class Cards:

    def __init__(self, type, value, room, bonus_value):
        self.type = type
        self.value = value
        self.room = room 
        self.bonus_value = bonus_value

    
        
    


pygame.display.set_caption('Kill Doctor Lucky') # title for game
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/m5x7.ttf', 50) #(font type, font size) None is the default

# *** Deciding the size of the player screen ***
# screen = pygame.display.set_mode((1000,1000)) # this will manually set the screen size

# this grab the users screen size and set he screen to that size
screen = pygame.display.set_mode()
x, y = screen.get_size()
screen = pygame.display.set_mode((x,y))


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


# *** Building the static scene ***
board = pygame.image.load("images/Board.png").convert()
board = pygame.transform.scale(board, (x,y)).convert()

text_surface = test_font.render('Kill Doctor Lucky', True, 'Black').convert_alpha() #('insert text', True or False, 'color of text') The T or F is for anti aliasing, true usually, false if pixel art

# this will create a red box 
#test_surface = pygame.Surface((100,200)) #S must be a capital, pygame.Surface((w,h))
#test_surface.fill('Red')

#test2 = pygame.image.load('images/Board.jpg')

rect_width, rect_height = 50, 30
rect_x, rect_y = (x - rect_width) // 3.75, (y - rect_height) // 4



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