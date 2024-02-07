import pygame
import button
import random
from sys import exit

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Kill Doctor Lucky') # title for game
test_font = pygame.font.Font('fonts/m5x7.ttf', 50) #(font type, font size) None is the default

# *** Deciding the size of the player screen ***

# screen = pygame.display.set_mode((1000,1000)) # this will manually set the screen size

# this grabs the users screen size and sets the screen to that size
screen = pygame.display.set_mode()
screen_W, screen_L = screen.get_size()
screen = pygame.display.set_mode((screen_W,screen_L))


# *** Building the game scene ***

# Game board
board_W = screen_W
board_L = screen_L * 0.9
board = pygame.image.load("images/Board2.jpg").convert()
board = pygame.transform.scale(board, (board_W,board_L)).convert()

# text/fonts
text_surface = test_font.render('Kill Doctor Lucky', True, 'Black').convert_alpha() #('insert text', True or False, 'color of text') The T or F is for anti aliasing, true usually, false if pixel art

# this will create a red box 
#test_surface = pygame.Surface((100,200)) #S must be a capital, pygame.Surface((w,h))
#test_surface.fill('Red')

# *** Room locations ***
rect_width, rect_height = 50, 30
room5_x, room5_y = (screen_W - rect_width) // 4.75, (screen_L - rect_height) // 4

# *** Colors ***
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Creating the buttons
next_turn = pygame.image.load("images/next_turn.png").convert_alpha()
#turn_button = button.Button(0, 1200, next_turn, 0.75) # calling Button class
turn_button = button.Button(0, 1200, next_turn, 0.75) # calling Button class


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
            
    #screen.blit(test_surface,(200,100)) #screen.blit(surface,position), the position is formatted like this: (x,y)
    
    screen.blit(board,(0,0))
    screen.blit(text_surface,(500,500))

    # actions that will happen on click of this button
    if turn_button.draw(screen) == True:
        print('you clicked the button :)')

    pygame.draw.rect(screen, RED, (room5_x, room5_y, rect_width, rect_height))
    

    pygame.display.update()
    clock.tick(60) # Maximum Framerate of 60
    