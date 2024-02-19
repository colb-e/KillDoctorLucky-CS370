# Cycle 1
import pygame
import player
from sys import exit

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Kill Doctor Lucky') 

# User Screen size
screen = pygame.display.set_mode()
screen_W, screen_L = screen.get_size()
screen = pygame.display.set_mode((screen_W,screen_L))

# Game board
board_W = screen_W
board_L = screen_L
board = pygame.image.load("images/Board2.jpg").convert()
board = pygame.transform.scale(board, (board_W,board_L)).convert()

# Colors 
BLACK = (0, 0, 0)

# Players
drLucky = player.Player(screen, BLACK, 1, 2, 1.8) # drawing dr lucky in room 1


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        # Use escape key to close game (added by Z)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                running = False
                exit()


    # Draw objects to screen
    screen.blit(board,(0,0))

    drLucky.DrawPlayer()

    pygame.display.update()
    clock.tick(60)