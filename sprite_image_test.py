# A majority of this was accomplished by Kimberly.
# Anything that is not stated to be my contribution was done by her.

import pygame
from sys import exit
import math
from pygame.locals import * 

# Initializing pygame
pygame.init()

# Set screen size
window_width = 800
window_height = 600
# Create game window and make resizable
screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)

# Set text font (added by Zhenia, but orginially done by Colby in another test program)
# test_font = pygame.font.Font('fonts/m5x7.ttf', 50) #(font type, font size)

# Text for indicating the red player's turn (done by Zhenia)
# turn_red = test_font.render("Red's turn", True, (255,0,0)).convert_alpha()
# turn_red_end = test_font.render("Red's turn", True, (0,0,0)).convert_alpha()

# Text for indicating the blue player's turn (done by Zhenia)
# turn_blue = test_font.render("Blue's turn", True, (0,0,255)).convert_alpha()
# turn_blue_end = test_font.render("Blue's turn", True, (0,0,0)).convert_alpha()

# Variable to keep track of the current player
currentPlayer = 1

# Clock object to control the frame rate
clock = pygame.time.Clock()

# Set window name
pygame.display.set_caption("Kill Doctor Lucky")

# Render board image
board = pygame.image.load("images/Board2.jpg")

# Room positions
room_positions = [(250, 50), (525, 50), (600, 50), (600, 110),
                  (600, 250), (500, 250), (330, 175)]

# Player class 1 (done by Z)
class Player1(pygame.sprite.Sprite):
            
    def __init__(self, pic, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # set surface size
        self.image = pygame.image.load(pic).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # set initial position

    # Update player position to the closest room
    def update_position(self, x, y):
        # Calculate the distance to each room and find the closest one
        closest_room = min(room_positions, key=lambda pos: math.hypot(pos[0] - x, pos[1] - y))
        self.rect.center = closest_room  # Update player position to the center of closest room


# Player class 2
class Player2(pygame.sprite.Sprite):
    def __init__(self, color, x, y):  # player class constructor
        super().__init__()
        self.image = pygame.Surface((50, 50))  # set surface size
        self.image.fill(color)  # set color
        self.rect = self.image.get_rect() #
        self.rect.center = (x, y)  # set initial position

    # Update player position to the closest room
    def update_position(self, x, y):
        # Calculate the distance to each room and find the closest one
        closest_room = min(room_positions, key=lambda pos: math.hypot(pos[0] - x, pos[1] - y))
        self.rect.center = closest_room  # Update player position to the center of closest room

# Button class
class Button(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height, text=''):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.text = "End turn!"
        self.font = pygame.font.Font(None, 36)
        self.render_text()

    def render_text(self):
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.image.blit(text_surface, text_rect)

# Create players
player1 = Player1("images/fay-chanceworthy-pixilart.png", 500, 250)  # create player 1 (with sprite image) done by Z
player2 = Player2((0, 0, 255), 500, 250)  # create player 2 (blue at position 500, 250)

# Create Dr. Lucky
drLucky = Player1("images/doctor-lucky-pixilart.png", 250, 50) #create Dr. Lucky (black at position 250, 50)

# Create sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(player1, player2, drLucky)  # add sprites to the group

# Create end turn button
end_turn_button = Button((255, 255, 255), 50, 50, 100, 50, 'End Turn')
all_sprites.add(end_turn_button)  # add button to the group

# Variable to keep track of Dr. Lucky's current room 
drLucky_current_room = 0

while True:
    for event in pygame.event.get():
        # Closing the window
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Resize event
        elif event.type == pygame.VIDEORESIZE:
            window_width, window_height = event.size

        # Mouse click
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the end turn button is clicked
            if end_turn_button.rect.collidepoint(event.pos):
                # Move Dr. Lucky to the next room
                drLucky_current_room = (drLucky_current_room + 1) % len(room_positions)
                drLucky.rect.center = room_positions[drLucky_current_room]

                # Switch players
                currentPlayer = 3 - currentPlayer

            else:
                # Move player to where the mouse is clicked
                x, y = event.pos
                if currentPlayer == 1:
                    # Tell it's the player's turn (added by Zhenia)
                    # screen.blit(turn_blue_end, (5,5))
                    # screen.blit(turn_red, (5,5))
                    
                    player1.update_position(x, y)
                    
                else:
                    # Tell it's the player's turn (added by Zhenia)
                    # screen.blit(turn_red_end, (5,5))
                    # screen.blit(turn_blue, (5,5))
                    
                    player2.update_position(x, y)
                    


    # Display board
    screen.blit(board, (200, 0))

    # Render pawns and button
    all_sprites.draw(screen)

    pygame.display.update()
    clock.tick(60)
