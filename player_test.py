import pygame
from pygame.locals import *
import random
import sys
from sys import exit

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Kill Doctor Lucky') # title for game
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

# character class
class Character:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = 10
        self.selected = False
            
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        if self.selected:
            pygame.draw.circle(screen, RED, (self.x, self.y), self.radius, 2)
        
# issue found below VV
player = Character("character.png", 100, 100)
            

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


    
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                player.x -= 50
            elif event.key == K_RIGHT:
                player.x += 50
            elif event.key == K_UP:
                player.y -= 50
            elif event.key == K_DOWN:
                player.y += 50
    
    player.draw(screen)
    pygame.display.update()

    clock.tick(60) # Maximum Framerate of 60


    

    
    


        
        

            
