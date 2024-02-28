# Cycle 1
import pygame
import player
import room
import button
from sys import exit

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Kill Doctor Lucky') 

# User Screen size
screen = pygame.display.set_mode()
screen_W, screen_L = screen.get_size()
screen = pygame.display.set_mode((screen_W,screen_L))

# Game board
board_W = screen_W * 0.9
board_L = screen_L
board = pygame.image.load("images/Board2.jpg").convert()
board = pygame.transform.scale(board, (board_W,board_L)).convert()

# Colors 
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Buttons

# here we will adjust the size and placement of the image based on the screen size
# it should be in the sidebar
nextTurnImage = pygame.image.load("images/next_turn.png")
nextTurnButton = button.Button(nextTurnImage, 100, 100)

# Players

# grabbing starting room x and y for players to start in


drLucky = player.Player(screen, BLACK, 0, 2, 1.8) # drawing dr lucky in room 1
player1 = player.Player(screen, RED, 0, 2, 1.8)
player2 = player.Player(screen, BLUE, 0, 2, 1.8)
player3 = player.Player(screen, GREEN, 0, 2, 1.8)


playerList = []
turnOrder = 0
roomCount = 0
playerList.append(drLucky)
playerList.append(player1)
playerList.append(player2)
playerList.append(player3)

TEMP = 5

drLucky.updatePlayer(TEMP) # updating player to index 1 in roomList (room 2)
player1.updatePlayer(TEMP)
player2.updatePlayer(TEMP)
player3.updatePlayer(TEMP)
drLucky.updatePlayer(TEMP) # updating player to index 1 in roomList (room 2)
drLucky.updatePlayer(TEMP) # updating player to index 1 in roomList (room 2)
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Draw objects to screen
    screen.blit(board,(0,0))
    
    # if the button is clicked
    if nextTurnButton.drawButton(screen) == True:
        
        print("Moved player ", turnOrder)
        previousRoomIndex = playerList[turnOrder].room_index

        # if player is in room 24 move them to room 1
        if previousRoomIndex == 23:

            playerList[turnOrder].updatePlayer(0)
            print("to room index 0")

        # else move to player to the room index they are in + 1
        else:

            newRoomIndex = previousRoomIndex + 1
            playerList[turnOrder].updatePlayer(newRoomIndex)
            print("to room index ", newRoomIndex)

        # after the player has moved to the next room decrease the count of the previous room by 1
        room.roomsList[previousRoomIndex].room_count -= 1

        # if the turn order is at the last player loop back to the first in the order
        if turnOrder == 3:

            turnOrder = 0

        # else change the turn order index to the current index + 1
        else:
            turnOrder += 1


    drLucky.DrawPlayer()
    player1.DrawPlayer()
    player2.DrawPlayer()
    player3.DrawPlayer()

    pygame.display.update()
    clock.tick(60)