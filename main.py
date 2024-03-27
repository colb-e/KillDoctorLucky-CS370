# Cycle 1
import pygame
import player
import room
import button
import card
from sys import exit

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Kill Doctor Lucky') 

# *** User Screen size ***
screen = pygame.display.set_mode()
screen_W, screen_L = screen.get_size()
screen = pygame.display.set_mode((screen_W,screen_L))

# *** Fonts ***

default_font = pygame.font.Font(None, int(min(screen_W, screen_L) * 0.05))

#  *** Colors ***
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# *** Players ***
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

TEMP = 0

drLucky.updatePlayer(TEMP) # updating player to index 1 in roomList (room 2)
player1.updatePlayer(TEMP)
player2.updatePlayer(TEMP)
player3.updatePlayer(TEMP)
drLucky.updatePlayer(TEMP) # updating player to index 1 in roomList (room 2)
drLucky.updatePlayer(TEMP) # updating player to index 1 in roomList (room 2)

#  *** Game board ***
board_W = screen_W * 0.9
board_L = screen_L
board = pygame.image.load("images/Board2.jpg").convert()
board = pygame.transform.scale(board, (board_W,board_L)).convert()

# *** Sidebar ***
sidebar_W = screen_W - board_W

sidebarBackgroundImage = pygame.image.load("images/sidebarBackground.jpg")
sidebarBackground = pygame.transform.scale(sidebarBackgroundImage, (sidebar_W, board_L)).convert()
sidebarBackground_W, sidebarBackground_L = sidebarBackground.get_size()
sidebarBackground_X, sidebarBackground_Y  = (screen_W - sidebarBackground_W) // 1, (screen_L - sidebarBackground_L) // 1

currentPlayerText = default_font.render("Current Player:", True, BLACK)

# This logic will decide the scale of the sidebar buttons depending on the screen size
print("Length: ", screen_L, "Width: ", screen_W)

if (screen_L >= 1440):
    sidebarScale = 1.5
    moveButtonScale = 0.5

elif (screen_L >= 1080):
    sidebarScale = 1.2
    moveButtonScale = 0.5
    
elif (screen_L >= 752):
    sidebarScale = 1
    moveButtonScale = 0.3

else:
    sidebarScale = 0.5
    moveButtonScale = 0.5
#  *** Buttons ***

# Next turn Button
nextTurnImage = pygame.image.load("images/nextturnbutton.png")
nextTurnButton = button.Button(screen, nextTurnImage, 1, 1000, sidebarScale)
nextTurnButton.addToSidebar(board_W, 1, 1000)

# Cards button
cardsBtnImage = pygame.image.load("images/cardsbutton.png")
cardsButton = button.Button(screen, cardsBtnImage, 1, 1000, sidebarScale)
cardsButton.addToSidebar(board_W, 1, 7)

# Rules Button 
rulesBtnImage = pygame.image.load("images/rulesbutton.png")
rulesButton = button.Button(screen, rulesBtnImage, 1, 1000, sidebarScale)
rulesButton.addToSidebar(board_W, 1, 3.45)

# Quit Button 
quitBtnImage = pygame.image.load("images/quitbutton.png")
quitButton = button.Button(screen, quitBtnImage, 1, 1000, sidebarScale)
quitButton.addToSidebar(board_W, 1, 2.3)

# Room movement buttons
moveHereImage = pygame.image.load("images/move_here.png")
room1 = button.Button(screen, moveHereImage, 2.15, 1.8, moveButtonScale)
room2 = button.Button(screen, moveHereImage, 1.6, 1.8, moveButtonScale)
room3 = button.Button(screen, moveHereImage, 1.57, 3, moveButtonScale)
room4 = button.Button(screen, moveHereImage, 2.2, 3.2, moveButtonScale)
room5 = button.Button(screen, moveHereImage, 3.7, 3, moveButtonScale)
room6 = button.Button(screen, moveHereImage, 3.6, 1.75, moveButtonScale)
room7 = button.Button(screen, moveHereImage, 3.55, 1.2, moveButtonScale)
room8 = button.Button(screen, moveHereImage, 9, 1.1, moveButtonScale)
room9 = button.Button(screen, moveHereImage, 11, 1.32, moveButtonScale)
room10 = button.Button(screen, moveHereImage, 13, 1.75, moveButtonScale)
room11 = button.Button(screen, moveHereImage, 9.6, 3.5, moveButtonScale)
room12 = button.Button(screen, moveHereImage, 12, 16, moveButtonScale)
room13 = button.Button(screen, moveHereImage, 3.5, 17, moveButtonScale)
room14 = button.Button(screen, moveHereImage, 2.2, 25, moveButtonScale)
room15 = button.Button(screen, moveHereImage, 2.2, 7.2, moveButtonScale)
room16 = button.Button(screen, moveHereImage, 1.61, 16, moveButtonScale)
room17 = button.Button(screen, moveHereImage, 1.22, 18, moveButtonScale)
room18 = button.Button(screen, moveHereImage, 1.26, 3.5, moveButtonScale)
room19 = button.Button(screen, moveHereImage, 1.22, 1.75, moveButtonScale)
room20 = button.Button(screen, moveHereImage, 1.25, 1.32, moveButtonScale)
room21 = button.Button(screen, moveHereImage, 1.28, 1.09, moveButtonScale)
room22 = button.Button(screen, moveHereImage, 1.62, 1.21, moveButtonScale)
room23 = button.Button(screen, moveHereImage, 2.23, 1.16, moveButtonScale)
room24 = button.Button(screen, moveHereImage, 2.15, 1.52, moveButtonScale)

roomButtonsList = [room1, room2, room3, room4, room5, room6, room7, room8, room9, room10,
                   room11, room12, room13, room14, room15, room16, room17, room18, room19,
                   room20, room21, room22, room23, room24]

# *** Cards ***
cardDeck = card.Card.createDeck()
displayCards = False
player1Hand = []
player2Hand = []
player3Hand = []
player4Hand = []

playerHands = []
playerHands.append(player1Hand)
playerHands.append(player2Hand)
playerHands.append(player3Hand)
playerHands.append(player4Hand)

def startingCards(playerHands, mainDeck):
        
        playerIndex = 0 # to keep track of the player we are giving cards to

        # will loop through a list of lists that store the cards in each players hand,
        # for each players hand the function will loop 6 times adding a card to their hand from the deck
        for hand in playerHands:
            i = 0 
            while (i < 6):
                
                drawCard(playerIndex, playerHands, mainDeck) # add the last card in the deck to the players hand
                i += 1 # track the number of cards being added
            
            playerIndex += 1

def drawCard(playerIndex, playerHands, mainDeck):
    topCard = mainDeck[-1]
    playerHand = playerHands[playerIndex]
    playerHand.append(topCard)
    mainDeck.pop(-1)
    
def playCard(turnorder):
    pass


#drawCard(0, playerHands, cardDeck)
startingCards(playerHands, cardDeck)
# *** Main game loop ***
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Draw objects to screen
    screen.blit(board, (0, 0))
    screen.blit(sidebarBackground, (sidebarBackground_X, sidebarBackground_Y))
    
    currentPlayerHand = playerHands[turnOrder] # equal to the list that stores the current players cards
    
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

    # when a user clicks the cards button it will either display the cards or stop displaying them
    if cardsButton.drawButton(screen) == True:
        if displayCards == True:
            displayCards = False
        else:   
            displayCards = True
      
    if rulesButton.drawButton(screen) == True:
        pass

    if quitButton.drawButton(screen) == True:
        pygame.quit()
        exit()

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


    #cardDeck[0].showCard(screen, 2, 2, 0.1)
    
    drLucky.DrawPlayer()
    player1.DrawPlayer()
    player2.DrawPlayer()
    player3.DrawPlayer()
    
     #logic for displaying Cards to current player
    if (displayCards == True):
        placement = 2
        for card in currentPlayerHand:
            
            card.showCard(screen, placement, 2, 0.1)
            placement += 0.5


    # TEMP FOR TESTING | this will show the card that player 1 has
    print(player1Hand[0].room_index)
    player1Hand[0].showCard(screen, 2, 2, 0.1)


    pygame.display.update()
    clock.tick(60)