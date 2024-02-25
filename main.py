# Cycle 1
import pygame
import player
import room
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
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Players

drLucky = player.Player(screen, BLACK, 0, 2, 1.8) # drawing dr lucky in room 1
player1 = player.Player(screen, RED, 0, 2, 1.8)
player2 = player.Player(screen, BLUE, 0, 2, 1.8)
player3 = player.Player(screen, GREEN, 0, 2, 1.8)

playerList = []

playerList.append(drLucky)
playerList.append(player1)
playerList.append(player2)
playerList.append(player3)

TEMP = 23

drLucky.updatePlayer(TEMP) # updating player to index 1 in roomList (room 2)
player1.updatePlayer(TEMP)
player2.updatePlayer(TEMP)
player3.updatePlayer(TEMP)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Draw objects to screen
    screen.blit(board,(0,0))

    drLucky.DrawPlayer()
    player1.DrawPlayer()
    player2.DrawPlayer()
    player3.DrawPlayer()

    pygame.display.update()
    clock.tick(60)