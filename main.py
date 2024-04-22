# Cycle 2
import pygame
import random
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
turnOrder = 1
roomCount = 0
moveActionPoints = 1
cardActionPoints = 1

playerList.append(drLucky)
playerList.append(player1)
playerList.append(player2)
playerList.append(player3)

TEMP = 0

drLucky.updatePlayer(TEMP) # updating player to index 1 in roomList (room 2)
room.roomsList[0].room_count = 1
player1.updatePlayer(TEMP)
room.roomsList[0].room_count = 2
player2.updatePlayer(TEMP)
room.roomsList[0].room_count = 3
player3.updatePlayer(TEMP)
room.roomsList[0].room_count = 4

# this function will properly rearrange and place all of the players in a room. 
# this should only be called after a player leaves a room, it was made to solve
# an issue with placement in a room directly after a player leaves the said room.
def updateRoom(roomIndex):
    room.roomsList[roomIndex].room_count = 0
    
    for player in playerList:
        if player.room_index == roomIndex:
            player.updatePlayer(roomIndex)
            room.roomsList[roomIndex].room_count += 1


#  *** Game board ***
board_W = screen_W * 0.9
board_L = screen_L
board = pygame.image.load("images/Board2.jpg").convert()
board = pygame.transform.scale(board, (board_W,board_L)).convert()

#  *** Main Menu Screen ***
mainM_W = screen_W
mainM_L = screen_L
mainM = pygame.image.load("images/main_menu.png").convert()
mainM = pygame.transform.scale(mainM, (mainM_W,mainM_L)).convert()

#  *** Credits Screen ***
credits_W = screen_W
credits_L = screen_L
credits = pygame.image.load("images/credits.png").convert()
credits = pygame.transform.scale(credits, (credits_W, credits_L)).convert()

# *** Sidebar ***
sidebar_W = screen_W - board_W

sidebarBackgroundImage = pygame.image.load("images/sidebarBackground.jpg")
sidebarBackground = pygame.transform.scale(sidebarBackgroundImage, (sidebar_W, board_L)).convert()
sidebarBackground_W, sidebarBackground_L = sidebarBackground.get_size()
sidebarBackground_X, sidebarBackground_Y  = (screen_W - sidebarBackground_W) // 1, (screen_L - sidebarBackground_L) // 1

# This logic will decide the scale of the sidebar buttons depending on the screen size
print("Length: ", screen_L, "Width: ", screen_W)

if (screen_L >= 1440):
    sidebarScale = 1.5
    moveButtonScale = 0.5
    cardScale = 0.58
    cardPlacement = 0.05
    currentDisplayTextScale_W = 0.85
    currentDisplayRectScale = 0.15

elif (screen_L >= 1080):
    sidebarScale = 1.2
    moveButtonScale = 0.5
    cardScale = 0.45
    cardPlacement = 0.075
    currentDisplayTextScale_W = 0.8
    currentDisplayRectScale = 0.21
    
elif (screen_L >= 752):
    sidebarScale = 1
    moveButtonScale = 0.3
    cardScale = 0.35
    cardPlacement = 0.075
    currentDisplayTextScale_W = 0.73
    currentDisplayRectScale = 0.30

else:
    sidebarScale = 0.5
    moveButtonScale = 0.5
    cardScale = 0.05
    cardPlacement = 0.1
    currentDisplayTextScale_W = 0.8
    currentDisplayRectScale = 0.2
    

default_font = pygame.font.Font(None, int(min(screen_W, screen_L) * 0.05))
currentPlayerText = default_font.render("Current Player:", True, BLACK)

def displayCurrentPlayer(font, currentPlayer):
    color = currentPlayer.color
  

    text = font.render("Current Player: ", True, color)
    text_x = board_W * currentDisplayTextScale_W
    text_y = 0
    rect_x = text_x + (text_x * currentDisplayRectScale)
    rect_y = 1 # 12
    
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, color, (rect_x, rect_y, 50, 30))

#  *** Buttons ***

# Menu Start Game Button
startGameImage = pygame.image.load("images/StartButton.png")
startGameButton = button.Button(screen, startGameImage, 2.05, 1.05, sidebarScale)

# Menu Credits Button
creditsImage = pygame.image.load("images/CreditsButton.png")
creditsButton = button.Button(screen, creditsImage, 3.6, 1.05, sidebarScale)
# Menu Quit Button
quitMenuImage = pygame.image.load("images/QuitGameButton.png")
quitMenuButton = button.Button(screen, quitMenuImage, 1.4, 1.05, sidebarScale)

# Next turn Button
nextTurnImage = pygame.image.load("images/nextturnbutton.png")
nextTurnButton = button.Button(screen, nextTurnImage, 1, 1000, sidebarScale)
nextTurnButton.addToSidebar(board_W, 1, 1000)

# Move Button
moveActionButtonImage = pygame.image.load("images/movebutton.png")
moveActionButton = button.Button(screen, moveActionButtonImage, 1, 1000, sidebarScale)
moveActionButton.addToSidebar(board_W, 1, 7)

# Draw card Button
drawCardButtonImage = pygame.image.load("images/drawcardbutton.png")
drawCardButton = button.Button(screen, drawCardButtonImage, 1, 1000, sidebarScale)
drawCardButton.addToSidebar(board_W, 1, 3.45)

# Cards button
cardsBtnImage = pygame.image.load("images/cardsbutton.png")
cardsButton = button.Button(screen, cardsBtnImage, 1, 1000, sidebarScale)
cardsButton.addToSidebar(board_W, 1, 2.3)

# Kill Button
killBtnImage = pygame.image.load("images/KillButton.png")
killButton = button.Button(screen, killBtnImage, 1, 1000, sidebarScale)
killButton.addToSidebar(board_W, 1, 1.73)

# Rules Button 
rulesBtnImage = pygame.image.load("images/rulesbutton.png")
rulesButton = button.Button(screen, rulesBtnImage, 1, 1000, sidebarScale)
rulesButton.addToSidebar(board_W, 1, 1.38)

# Quit Button 
quitBtnImage = pygame.image.load("images/quitbutton.png")
quitButton = button.Button(screen, quitBtnImage, 1, 1000, sidebarScale)
quitButton.addToSidebar(board_W, 1, 1.16)

# Room movement buttons
moveHereImage = pygame.image.load("images/MoveHereButton.png")
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

# Use Card Buttons
useCardButtonImage = pygame.image.load("images/select_card.png")
useCardButton = button.Button(screen, useCardButtonImage, 2, 2, 0.5)


# *** Cards ***
cardDeck = card.Card.createDeck()
discardPile = []
displayCards = False

movementAction = False

drawCardAction = True
playCard = True

WeaponCard = True
murderPoints = 1
murderAttempt = False

failPoints = 0
failAllowed = False

CardInPlay = None
playerMoving = 10
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
        
        playerIndex = 0 # will stay as 0 we will skip dr lucky with if statement

        # will loop through a list of lists that store the cards in each players hand,
        # for each players hand the function will loop 6 times adding a card to their hand from the deck
        for hand in playerHands:
            
            # will skip giving dr lucky cards
            if playerIndex > 0:
                i = 0 
                while (i < 6):
                    
                    drawCard(playerIndex, playerHands, mainDeck) # add the last card in the deck to the players hand
                    i += 1 # track the number of cards being added
                
            playerIndex += 1

def drawCard(playerIndex, playerHands, mainDeck):

    # if the deck is empty reshuffle the discard and set the deck equal to the shuffled discard
    if len(cardDeck) <= 0:
        # if the discard is also empty tell the player they cannot draw
        if len(discardPile) <= 0:
            print("Cannot draw card, the deck and discard pile are empty!")
        else:
            random.shuffle(discardPile)
            mainDeck = discardPile
            discardPile.clear()

    topCard = mainDeck[-1]
    playerHand = playerHands[playerIndex]
    playerHand.append(topCard)
    mainDeck.pop(-1)
        
startingCards(playerHands, cardDeck)
state = "menu"

# *** Main game loop ***
while True:
    
    # While the state is the menu, draw the menu
    while (state == "menu"):
        
        screen.blit(mainM, (0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
        #  Use escape key to close game and space to switch states
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    running = False
                    exit()
            
             # Start Game Button
        if startGameButton.drawButton(screen) == True:
            state = "board"
            
        # Credits Button
        if creditsButton.drawButton(screen) == True:
            state = "credits"
        
        # Quit Menu Button
        if quitMenuButton.drawButton(screen) == True:
            pygame.quit()
            running = False
            exit()
                    
                    
                    
                    
                    
        pygame.display.update()
        clock.tick(60)
        
        
    # While the state is the credits, display the credits screen
    while (state == "credits"):
        screen.blit(credits, (0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
        #  Use escape key to close game and space to switch states
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    running = False
                    exit()
                if event.key == pygame.K_SPACE:
                    state = "menu"
                    
        pygame.display.update()
        clock.tick(60)


    # Main game loop
    while (state == "board"):
        currentPlayerHand = playerHands[turnOrder] # equal to the list that stores the current players cards
        
        # Draw objects to screen
        screen.blit(board, (0, 0))
        screen.blit(sidebarBackground, (sidebarBackground_X, sidebarBackground_Y))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # ****** SIDEBAR BUTTONS ******
                
        # ** Next Turn Button **
        # When a player ends their turn we will move Dr lucky to the next room
        # and increment the turn order, this button should be the only way for 
        # the turn order to update
        if nextTurnButton.drawButton(screen) == True:
            
            moveActionPoints = 1
            murderPoints = 1
            failPoints = 0
            WeaponCard = True
            drawCardAction = True
            playCard = True
            murderAttempt = False
            movementAction = False
            displayCards = False

            print("Moved Dr. Lucky")
            previousRoomIndex = playerList[0].room_index

            # if Dr. Lucky is in room 24 move them to room 1
            if previousRoomIndex == 23:

                playerList[0].updatePlayer(0)
                print("to room index 0")

            else:

                newRoomIndex = previousRoomIndex + 1
                playerList[0].updatePlayer(newRoomIndex)
                print("to room index ", newRoomIndex)

            room.roomsList[previousRoomIndex].room_count -= 1
            room.roomsList[newRoomIndex].room_count += 1
            updateRoom(previousRoomIndex)

            # If there is more people than just Dr lucky in the room he just moved into..
            if (room.roomsList[newRoomIndex].room_count > 1):
                if (turnOrder == 3):
                    X = 1
                else:
                    X = turnOrder + 1
                
                Y = True
                
                while(Y == True):
                    
                    if (playerList[X].room_index == newRoomIndex):
                        turnOrder = X
                        Y = False
                        
                    elif(X == 3):
                        X = 1
                        
                    else:
                        X += 1
                  
            # if the turn order is at the last player loop back to the first human player and skip Dr. Lucky
            elif turnOrder == 3:

                turnOrder = 1 # this will stay as 1 since Dr. lucky will only take an action when a player ends their turn

            # else change the turn order index to the current index + 1
            else:
                turnOrder += 1
            
        # ** Move button **
        if moveActionButton.drawButton(screen) == True:
            if moveActionPoints > 0:
                
                movementAction = True

            elif moveActionPoints == 0:
                print("No movement points left, use a card to move if possible")

        # ** Draw card button **
        if drawCardButton.drawButton(screen) == True:
            
            currentPlayerRoom = playerList[turnOrder].room_index
            currentSightLines = room.allSightLines[currentPlayerRoom]
            outOfSight = True

            
            for siteLineRoom in currentSightLines:
                #print(room.roomsList[siteLineRoom].room_count)
                if room.roomsList[siteLineRoom].room_count > 0:
                        outOfSight = False

            if (room.roomsList[currentPlayerRoom].room_count == 1 and outOfSight == True):

                if (drawCardAction == True):
                    drawCard(turnOrder, playerHands, cardDeck)
                    drawCardAction = False
                    playCard = False
                else:
                    print("You cannot draw a card, you have either drawn or played a card already.")
            
        # ** Cards Button **
        # when a user clicks the cards button it will either display the cards or stop displaying them
        if cardsButton.drawButton(screen) == True:

            if (displayCards == True):
                displayCards = False
            else:   
                displayCards = True

        # ** Kill button **
        if killButton.drawButton(screen) == True:
            if (murderAttempt == False):

                murderAttempt = True
                drawCardAction = False # if player plays a card set drawcard to false

                currentPlayerRoom = playerList[turnOrder].room_index
                drLuckyRoom = playerList[0].room_index
                currentSightLines = room.allSightLines[currentPlayerRoom]
                outOfSight = True

                # Check each room in site and if any room has a player in it set outOfSight to false
                for siteLineRoom in currentSightLines:
                    #print(room.roomsList[siteLineRoom].room_count)

                    # eventually rename canKill to outOfSite and possibly add a var that will save the room in site that is occupied
                    if room.roomsList[siteLineRoom].room_count > 0:
                        outOfSight = False

                print("player ", turnOrder, " room location: ", currentPlayerRoom)
                print("Dr. Lucky room location: ", drLuckyRoom)

                # if the current player is alone in a room with Dr. Lucky and out of site they can attack
                if currentPlayerRoom == drLuckyRoom and outOfSight == True and room.roomsList[drLuckyRoom].room_count == 2:
                    print("you can kill Dr. Lucky, player ", turnOrder, " WINS!")
                else:
                    print("you cannot kill doctor Lucky")
            else:
                print("You cannot attempt to Kill Dr. Lucky again this turn.")
        
        if rulesButton.drawButton(screen) == True:
            pass

        if quitButton.drawButton(screen) == True:
            pygame.quit()
            exit()
        
        # When a movement action is triggered this will execute
        if (movementAction == True):
            
            # will select the list of adjacent rooms equal to the current player room index
            currentRoom = room.allAdjacentRooms[playerList[turnOrder].room_index]

            # for each adjacent room in the selected list 
            for adjacentRoom in currentRoom:
                # draw the button for the this room index and if it is clicked
                if roomButtonsList[adjacentRoom].drawButton(screen) == True:
                    
                    # Movement card testing
                    print("Movement Points after play: ", moveActionPoints)
                    print("---------- END -----------")


                    previousRoomIndex = playerList[turnOrder].room_index # save old room index
                    print("Moved player ", turnOrder)
                    
                    # move player to the adjacent room this button is equal to
                    playerList[turnOrder].updatePlayer(adjacentRoom)
                    print("From room ", previousRoomIndex, " to room ", adjacentRoom )

                    # after the player has moved to the next room decrease the count of the previous room by 1
                    room.roomsList[previousRoomIndex].room_count -= 1
                    room.roomsList[adjacentRoom].room_count += 1
                    updateRoom(previousRoomIndex)

                    moveActionPoints -= 1
                    movementAction = False
                    CardInPlay = None
            
            # This section will print the option for the player to move to the room
            # specified on their movement card
            if CardInPlay != None:  

                if roomButtonsList[CardInPlay.room_index].drawButton(screen) == True:

                    # Movement card testing
                    print("Movement Points after play: ", moveActionPoints)
                    
                    previousRoomIndex = playerList[turnOrder].room_index # save old room index
                    print("Moved player ", turnOrder)

                    playerList[turnOrder].updatePlayer(CardInPlay.room_index)
                    print("From room ", previousRoomIndex, " to room ", CardInPlay.room_index)

                    room.roomsList[previousRoomIndex].room_count -= 1
                    room.roomsList[CardInPlay.room_index].room_count += 1
                    updateRoom(previousRoomIndex)

                    moveActionPoints -= 1
                    movementAction = False
                    CardInPlay = None
                    
        drLucky.DrawPlayer()
        player1.DrawPlayer()
        player2.DrawPlayer()
        player3.DrawPlayer()

        displayCurrentPlayer(default_font, playerList[turnOrder])

        #logic for displaying Cards to current player
        if (displayCards == True):
            
            # will place first card in top right
            card_x = 0
            card_y = 0
            count = 0

            for card in currentPlayerHand:
                
                card.showCardTest(screen, card_x, 0, cardScale)
                
                # On click of this button execute a function that will use a card but have
                # if statements deciding action based on card type. if a player has already
                # played a card the select buttons will not be shown
                if (playCard == True):
                    if useCardButton.drawUseCardButton(screen, card_x, 0.2) == True:

                        if (card.card_type == 'move'):
                            
                            oldMovePoints = moveActionPoints # testing movement cards

                            movementAction = True
                            moveActionPoints += card.value
                        
                        if (card.card_type == 'weapon'):

                            # after a weapon card is played a player cannot play another
                            if (WeaponCard == False):
                                print("You cannot play another Weapon card!")
                            else:
                                WeaponCard = False
                                drawCardAction = False # if player plays a card set drawcard to false
                                if (playerList[turnOrder].room_index == card.room_index):
                                    murderPoints = card.bonus_value
                                else:
                                    murderPoints = card.value

                                print("Player ", turnOrder, " has ", murderPoints, " murderPoints.")
                        
                        if (card.card_type == 'fail'):

                            if (failAllowed == True):
                                failPoints += card.value
                                print("Added ", card.value, " to the fail points, Total: ", failPoints)
                            else:
                                print("You cannot use that card until a murder attempt occurs")
                        

                        CardInPlay = card
                        #drawCardAction = False # if player plays a card set drawcard to false
                        displayCards = False

                        # if the card being used is a fail card it will be removed from player rather than being placed into the discard pile
                        if (card.card_type == 'fail'):
                            currentPlayerHand.pop(count)
                        else: 
                            discardPile.append(card)
                            currentPlayerHand.pop(count)
                                

                card_x += cardPlacement
                count += 1

        # TEMP FOR TESTING | this will show the card that player 1 has
        #print(player1Hand[0].room_index)
        #player1Hand[0].showCard(screen, 2, 2, 0.1)
        #player1Hand[0].showCardTest(screen, 0.4, 0.4, 0.1)

        pygame.display.update()
        clock.tick(60)