# Cycle 1
import pygame
import player
import player2
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

# Character Images
fay = "images/fay-chanceworthy-pixilart.png"
drlucky = "images/doctor-lucky-pixilart.png"
gail = "images/gail-russo-pixilart.png"
proximo = "images/proximo-domingo-pixilart.png"

# Buttons
sidebar_W = screen_W - board_W

nextTurnImage = pygame.image.load("images/nextturnbutton.png")
btn_scale = 1.5 # will change the Length of the button
nextTurn_W, nextTurn_L = nextTurnImage.get_size() # grabbing image size
nextTurn_W = sidebar_W # setting the width of the image to the width of the sidebar
nextTurn_l = (nextTurn_L* btn_scale) # multiplying given scale with the image length
nextTurnimage = pygame.transform.scale(nextTurnImage, (nextTurn_W, nextTurn_L)) # adjusting to new image size
nextTurn_X, nextTurn_Y = (screen_W - nextTurn_W) // 1, (screen_L - nextTurn_L) // 1000 # placing the button in a relative Location the // 1 and the // 1000 decide the placement
nextTurnButton = button.Button(nextTurnImage, nextTurn_X, nextTurn_Y) # calling the button class

quitImage = pygame.image.load("images/quitbutton.png")
btn_scale = 1.5 # change the Length of the button
quit_W, quit_L = quitImage.get_size() # grabbing image size
quit_W = sidebar_W # setting the width of the image to the width of the sidebar
quit_l = (quit_L* btn_scale) # multiplying given scale with the image length
quitimage = pygame.transform.scale(quitImage, (quit_W, quit_L)) # adjusting to new image size
quit_X, quit_Y = (screen_W - quit_W) // 1, (screen_L - quit_L) // 1 # placing the button in a relative Location the // 1 and the // 1 decide the placement
quitButton = button.Button(quitImage, quit_X, quit_Y) # calling the button class

rulesImage = pygame.image.load("images/rulesbutton.png")
btn_scale = 1.5 # change the Length of the button
rules_W, rules_L = rulesImage.get_size() # grabbing image size
rules_W = sidebar_W # setting the width of the image to the width of the sidebar
rules_l = (rules_L* btn_scale) # multiplying given scale with the image length
rulesimage = pygame.transform.scale(rulesImage, (rules_W, rules_L)) # adjusting to new image size
rules_X, rules_Y = (screen_W - rules_W) // 1, (screen_L - rules_L) // 3 # placing the button in a relative Location the // 1 and the // 3 decide the placement
rulesButton = button.Button(rulesImage, rules_X, rules_Y) # calling the button class

cardsImage = pygame.image.load("images/cardsbutton.png")
btn_scale = 1.5 # change the Length of the button
cards_W, cards_L = cardsImage.get_size() # grabbing image size
cards_W = sidebar_W # setting the width of the image to the width of the sidebar
cards_l = (cards_L* btn_scale) # multiplying given scale with the image length
cardsimage = pygame.transform.scale(cardsImage, (cards_W, cards_L)) # adjusting to new image size
cards_X, cards_Y = (screen_W - cards_W) // 1, (screen_L - cards_L) // 1.5 # placing the button in a relative Location the // 1 and the // 1.5 decide the placement
cardsButton = button.Button(cardsImage, cards_X, cards_Y) # calling the button class

# Players

# grabbing starting room x and y for players to start in


drLucky = player.Player(screen, BLACK, 0, 2, 1.8) # drawing dr lucky in room 1
player_1 = player.Player(screen, RED, 0, 2, 1.8)
player_2 = player.Player(screen, BLUE, 0, 2, 1.8)
player_3 = player.Player(screen, GREEN, 0, 2, 1.8)


playerList = []
turnOrder = 0
roomCount = 0
playerList.append(drLucky)
playerList.append(player_1)
playerList.append(player_2)
playerList.append(player_3)

TEMP = 23

drLucky.updatePlayer(TEMP) # updating player to index 1 in roomList (room 2)
player_1.updatePlayer(TEMP)
player_2.updatePlayer(TEMP)
player_3.updatePlayer(TEMP)
drLucky.updatePlayer(TEMP) # updating player to index 1 in roomList (room 2)
drLucky.updatePlayer(TEMP) # updating player to index 1 in roomList (room 2)
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        #  Use escape key to close game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                running = False
                exit()

    # Draw objects to screen
    screen.blit(board,(0,0))
    
    # if the next turn button is clicked
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


# if the quit button is clicked
    if quitButton.drawButton(screen) == True:
            pygame.quit()
            running = False
            exit()
            
# if the rules button is clicked
    if rulesButton.drawButton(screen) == True:
        running = True
        
# if the cards button is clicked
    if cardsButton.drawButton(screen) == True:
        running = True


    drLucky.DrawPlayer()
    player_1.DrawPlayer()
    player_2.DrawPlayer()
    player_3.DrawPlayer()

    pygame.display.update()
    clock.tick(60)