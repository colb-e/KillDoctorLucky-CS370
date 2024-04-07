import pygame
import player3
import rooms2
import button2
from sys import exit

screen = pygame.display.set_mode()
screen_W, screen_L = screen.get_size()

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Kill Doctor Lucky')
        
        # *** User Screen size ***
        
        screen = pygame.display.set_mode((screen_W,screen_L))
        self.screen = screen
        
        
        self.stateManager = StateManager('board')
        self.board = Board(self.screen, self.stateManager)
        
        # Dictionary of states
        self.states = {'board': self.board}
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    
            self.states[self.stateManager.getState()].run()
            pygame.display.update()
            self.clock.tick(60)


class Board:
    
    def __init__(self, display, States):
        self.display = display
        self.States = States
    
    def run(self):
    
        # *** User Screen size ***
        # screen = pygame.display.set_mode((screen_W,screen_L))

        # *** Fonts ***

        default_font = pygame.font.Font(None, int(min(screen_W, screen_L) * 0.05))
        
        #  *** Colors ***
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        BLUE = (0, 0, 255)
        GREEN = (0, 255, 0)

        # *** Players ***
        drLucky = player3.Player3(screen, BLACK, 0, 2, 1.8) # drawing dr lucky in room 1
        player_1 = player3.Player3(screen, RED, 0, 2, 1.8)
        player_2 = player3.Player3(screen, BLUE, 0, 2, 1.8)
        player_3 = player3.Player3(screen, GREEN, 0, 2, 1.8)


        playerList = []
        turnOrder = 0
        roomCount = 0
        playerList.append(drLucky)
        playerList.append(player_1)
        playerList.append(player_2)
        playerList.append(player_3)

        TEMP = 0

        drLucky.updatePlayer(TEMP) # updating player to index 1 in roomList (room 2)
        player_1.updatePlayer(TEMP)
        player_2.updatePlayer(TEMP)
        player_3.updatePlayer(TEMP)
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

        elif (screen_L >= 1080):
            sidebarScale = 1.2

        elif (screen_L >= 800):
            sidebarScale = 1

        else:
            sidebarScale = 0.5

        #  *** Buttons ***

        # Next turn Button
        nextTurnImage = pygame.image.load("images/nextturnbutton.png")
        nextTurnButton = button2.Button2(screen, nextTurnImage, 1, 1000, sidebarScale)
        nextTurnButton.addToSidebar(board_W, 1, 1000)

        # Cards button
        cardsBtnImage = pygame.image.load("images/cardsbutton.png")
        cardsButton = button2.Button2(screen, cardsBtnImage, 1, 1000, sidebarScale)
        cardsButton.addToSidebar(board_W, 1, 7)

        # Rules Button 
        rulesBtnImage = pygame.image.load("images/rulesbutton.png")
        rulesButton = button2.Button2(screen, rulesBtnImage, 1, 1000, sidebarScale)
        rulesButton.addToSidebar(board_W, 1, 3.45)

        # Quit Button 
        quitBtnImage = pygame.image.load("images/quitbutton.png")
        quitButton = button2.Button2(screen, quitBtnImage, 1, 1000, sidebarScale)
        quitButton.addToSidebar(board_W, 1, 2.3)

        # Room movement buttons
        moveHereImage = pygame.image.load("images/move_here.png")
        room1 = button2.Button2(screen, moveHereImage, 2.15, 1.8, 0.5)
        room2 = button2.Button2(screen, moveHereImage, 1.6, 1.8, 0.5)
        room3 = button2.Button2(screen, moveHereImage, 1.57, 3, 0.5)
        room4 = button2.Button2(screen, moveHereImage, 2.2, 3.2, 0.5)
        room5 = button2.Button2(screen, moveHereImage, 3.7, 3, 0.5)
        room6 = button2.Button2(screen, moveHereImage, 3.6, 1.75, 0.5)
        room7 = button2.Button2(screen, moveHereImage, 3.55, 1.2, 0.5)
        room8 = button2.Button2(screen, moveHereImage, 9, 1.1, 0.5)
        room9 = button2.Button2(screen, moveHereImage, 11, 1.32, 0.5)
        room10 = button2.Button2(screen, moveHereImage, 13, 1.75, 0.5)
        room11 = button2.Button2(screen, moveHereImage, 9.6, 3.5, 0.5)
        room12 = button2.Button2(screen, moveHereImage, 12, 16, 0.5)
        room13 = button2.Button2(screen, moveHereImage, 3.5, 17, 0.5)
        room14 = button2.Button2(screen, moveHereImage, 2.2, 25, 0.5)
        room15 = button2.Button2(screen, moveHereImage, 2.2, 7.2, 0.5)
        room16 = button2.Button2(screen, moveHereImage, 1.61, 16, 0.5)
        room17 = button2.Button2(screen, moveHereImage, 1.22, 18, 0.5)
        room18 = button2.Button2(screen, moveHereImage, 1.26, 3.5, 0.5)
        room19 = button2.Button2(screen, moveHereImage, 1.22, 1.75, 0.5)
        room20 = button2.Button2(screen, moveHereImage, 1.25, 1.32, 0.5)
        room21 = button2.Button2(screen, moveHereImage, 1.28, 1.09, 0.5)
        room22 = button2.Button2(screen, moveHereImage, 1.62, 1.21, 0.5)
        room23 = button2.Button2(screen, moveHereImage, 2.23, 1.16, 0.5)
        room24 = button2.Button2(screen, moveHereImage, 2.15, 1.52, 0.5)

        roomButtonsList = [room1, room2, room3, room4, room5, room6, room7, room8, room9, room10,
                        room11, room12, room13, room14, room15, room16, room17, room18, room19,
                        room20, room21, room22, room23, room24]


        # *** Main game loop ***
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Draw objects to screen
            screen.blit(board, (0, 0))
            screen.blit(sidebarBackground, (sidebarBackground_X, sidebarBackground_Y))
            
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
                rooms2.roomsList[previousRoomIndex].room_count -= 1

                # if the turn order is at the last player loop back to the first in the order
                if turnOrder == 3:

                    turnOrder = 0

                # else change the turn order index to the current index + 1
                else:
                    turnOrder += 1

            if cardsButton.drawButton(screen) == True:
                pass

            if rulesButton.drawButton(screen) == True:
                pass

            if quitButton.drawButton(screen) == True:
                pygame.quit()
                exit()

            # will select the list of adjacent rooms equal to the current player room index
            currentRoom = rooms2.allAdjacentRooms[playerList[turnOrder].room_index]

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
                    rooms2.roomsList[previousRoomIndex].room_count -= 1

                    # if the turn order is at the last player loop back to the first in the order
                    if turnOrder == 3:

                        turnOrder = 0

                    # else change the turn order index to the current index + 1
                    else:
                        turnOrder += 1

            drLucky.DrawPlayer()
            player_1.DrawPlayer()
            player_2.DrawPlayer()
            player_3.DrawPlayer()
        
        





# States
class StateManager:
    def __init__(self, currentState):
        self.currentState = currentState
        self.stateStack = []
        self.previousState = None
        
    def getState(self):
        return self.currentState
    
    def enterState(self, state):
        # if len(self.stateStack) > 1:
            # self.previousState = self.stateStack[-1]
        self.currentState = state
        # self.stateStack.append(state)
        
    # def exitState(self):
        # self.stateStack.pop()
