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

# Fonts

default_font = pygame.font.Font(None, int(min(screen_W, screen_L) * 0.05))

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
turnOrder = 0
roomCount = 0
playerList.append(drLucky)
playerList.append(player1)
playerList.append(player2)
playerList.append(player3)

TEMP = 3

drLucky.updatePlayer(TEMP) # updating player to index 1 in roomList (room 2)
player1.updatePlayer(TEMP)
player2.updatePlayer(TEMP)
player3.updatePlayer(TEMP)
drLucky.updatePlayer(TEMP) # updating player to index 1 in roomList (room 2)
drLucky.updatePlayer(TEMP) # updating player to index 1 in roomList (room 2)

# Game board
board_W = screen_W * 0.9
board_L = screen_L
board = pygame.image.load("images/Board2.jpg").convert()
board = pygame.transform.scale(board, (board_W,board_L)).convert()

# Sidebar
sidebar_W = screen_W - board_W

currentPlayerText = default_font.render("Current Player:", True, BLACK)

# Buttons
nextTurnImage = pygame.image.load("images/next_turn.png")
nextTurnButton = button.Button(screen, nextTurnImage, 1, 1000, 1.5)
nextTurnButton.addToSidebar(board_W, 1, 1000)

# Room movement buttons
moveHereImage = pygame.image.load("images/move_here.png")
room1 = button.Button(screen, moveHereImage, 2.15, 1.8, 0.5)
room2 = button.Button(screen, moveHereImage, 1.6, 1.8, 0.5)
room3 = button.Button(screen, moveHereImage, 1.57, 3, 0.5)
room4 = button.Button(screen, moveHereImage, 2.2, 3.2, 0.5)
room5 = button.Button(screen, moveHereImage, 3.7, 3, 0.5)
room6 = button.Button(screen, moveHereImage, 3.6, 1.75, 0.5)
room7 = button.Button(screen, moveHereImage, 3.55, 1.2, 0.5)
room8 = button.Button(screen, moveHereImage, 9, 1.1, 0.5)
room9 = button.Button(screen, moveHereImage, 11, 1.32, 0.5)
room10 = button.Button(screen, moveHereImage, 13, 1.75, 0.5)
room11 = button.Button(screen, moveHereImage, 9.6, 3.5, 0.5)
room12 = button.Button(screen, moveHereImage, 12, 16, 0.5)
room13 = button.Button(screen, moveHereImage, 3.5, 17, 0.5)
room14 = button.Button(screen, moveHereImage, 2.2, 25, 0.5)
room15 = button.Button(screen, moveHereImage, 2.2, 7.2, 0.5)
room16 = button.Button(screen, moveHereImage, 1.61, 16, 0.5)
room17 = button.Button(screen, moveHereImage, 1.22, 18, 0.5)
room18 = button.Button(screen, moveHereImage, 1.26, 3.5, 0.5)
room19 = button.Button(screen, moveHereImage, 1.22, 1.75, 0.5)
room20 = button.Button(screen, moveHereImage, 1.25, 1.32, 0.5)
room21 = button.Button(screen, moveHereImage, 1.28, 1.09, 0.5)
room22 = button.Button(screen, moveHereImage, 1.62, 1.21, 0.5)
room23 = button.Button(screen, moveHereImage, 2.23, 1.16, 0.5)
room24 = button.Button(screen, moveHereImage, 2.15, 1.52, 0.5)

roomButtonsList = [room1, room2, room3, room4, room5, room6, room7, room8, room9, room10,
                   room11, room12, room13, room14, room15, room16, room17, room18, room19,
                   room20, room21, room22, room23, room24]



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

    # will select the list of adjacent rooms equal to the current player room index
    currentRoom = room.allAdjacentRooms[playerList[turnOrder].room_index]

    # for each adjacent room in the selected list 
    for adjacentRoom in currentRoom:
        # draw the button for the this room index and if it is clicked
        if roomButtonsList[adjacentRoom].drawButton(screen) == True:

            previousRoomIndex = playerList[turnOrder].room_index # save old room index
            print("Moved player ", turnOrder)
            
            
           
            # move player to the adjacent room this button is equal to
            playerList[turnOrder].updatePlayer(adjacentRoom)
            print("From room ", previousRoomIndex, " to room ", adjacentRoom )

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