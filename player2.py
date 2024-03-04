import pygame
import room

class Player2:

    # All players will be this size
    player_width, player_height = 50, 50

    def __init__(self, surface, pic, room_index, x, y):
        self.surface = surface
        self.surface_W, self.surface_L = surface.get_size()
        self.image = pygame.image.load(pic).convert_alpha()
        self.rect = self.image.get_rect()
        self.room_index = room_index
        # given cords/room cords
        self.x = x
        self.y = y
        # calculated player cords
        self.player_x = 0
        self.player_y = 0
        
    def updatePlayer(self, room_index):

        self.room_index = room_index #setting players current room_index to specified room_index
        
        # resetting player postion
        self.player_x = 0
        self.player_y = 0

        # grabbing cords of given room index
        x, y = room.roomsList[self.room_index].roomX, room.roomsList[self.room_index].roomY # grabbing x and y values of room player is moving to
        
        # if a player is already in the room to be moved to place the current player to the side

        # 0 players in room
        if room.roomsList[self.room_index].room_count == 0:
            self.x = x
            self.y = y
            room.roomsList[self.room_index].room_count += 1 # increasing the amount of people in new room

        # 1 players in room
        elif room.roomsList[self.room_index].room_count == 1:
            self.x = x 
            self.y = y 
            self.player_x = Player2.player_width + 5
            room.roomsList[self.room_index].room_count += 1 # increasing the amount of people in new room

        # 2 players in room
        elif room.roomsList[self.room_index].room_count == 2:
            self.x = x 
            self.y = y 
            self.player_y = Player2.player_height + 5
            room.roomsList[self.room_index].room_count += 1 # increasing the amount of people in new room

        # 3 players in room
        elif room.roomsList[self.room_index].room_count == 3:
            self.x = x
            self.y = y 
            self.player_x = Player2.player_width + 5
            self.player_y = Player2.player_height + 5
            room.roomsList[self.room_index].room_count += 1 # increasing the amount of people in new room

        # Calcualting player location relative to given screen size
        self.player_x += (self.surface_W - Player2.player_width) // self.x
        self.player_y += (self.surface_L - Player2.player_height) // self.y
            
            
    def DrawPlayer(self):
        
        pygame.draw(self.surface, self.image, (self.player_x, self.player_y, Player2.player_width, Player2.player_height))
