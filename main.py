import pygame
import button
import player
import room
import random
from sys import exit

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Kill Doctor Lucky') # title for game
test_font = pygame.font.Font('fonts/m5x7.ttf', 50) #(font type, font size) None is the default

# *** Deciding the size of the player screen ***

# this grabs the users screen size and sets the screen to that size
screen = pygame.display.set_mode()
screen_W, screen_L = screen.get_size()
screen = pygame.display.set_mode((screen_W,screen_L))

# *** Building the game scene ***

# Game board
board_W = screen_W
board_L = screen_L * 0.9 # will add space to bottom of screen
board = pygame.image.load("images/Board2.jpg").convert()
board = pygame.transform.scale(board, (board_W,board_L)).convert()

# *** Room locations ***

# *** Colors ***
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Creating the buttons
next_turn = pygame.image.load("images/next_turn.png").convert_alpha()
turn_button = button.Button(0, 0, next_turn, 0.75) # x, y, 
btn_count = 0

# *** Rooms ***
rooms = room.Rooms.createRooms()
player_start = rooms[0].room_x, rooms[0].room_y

# *** Players ***
drLucky = player.Player(screen, BLACK, player_start[0], player_start[1]) # surface, color, x cord, y cord
player1 = player.Player(screen, RED, player_start[0], player_start[1])


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
        
    screen.blit(board,(0,0))
    
    # actions that will happen on click of this button
    if turn_button.draw(screen) == True:
        
        if btn_count < 23:
            btn_count += 1
            drLucky.player_x, drLucky.player_y = rooms[btn_count].room_x, rooms[btn_count].room_y
        else:
            btn_count = 0
            drLucky.player_x, drLucky.player_y = rooms[btn_count].room_x, rooms[btn_count].room_y

    player1.Draw()
    drLucky.Draw()
    
    pygame.display.update()
    clock.tick(60) # Maximum Framerate of 60
    