import pygame
import room

class Player:

    # All players will be this size
    player_width, player_height = 50, 30

    def __init__(self, surface, color, room_index, x, y):
        self.surface = surface
        self.surface_W, self.surface_L = surface.get_size()
        self.color = color
        self.room_index = room_index
        # given cords/room cords
        self.x = x
        self.y = y
        # calculated player cords
        self.player_x = 0
        self.player_y = 0
        
    def updatePlayer(self, room_index):

        self.room_index = room_index #setting players current room_index to specified room_index

        # grabbing cords of given room index
        # each set is equal to a different postion in each room
        x1, y1 = room.roomsList[self.room_index].roomX1, room.roomsList[self.room_index].roomY1 
        x2, y2 = room.roomsList[self.room_index].roomX2, room.roomsList[self.room_index].roomY2
        x3, y3 = room.roomsList[self.room_index].roomX3, room.roomsList[self.room_index].roomY3
        x4, y4 = room.roomsList[self.room_index].roomX4, room.roomsList[self.room_index].roomY4
        

        # 0 players in room
        if room.roomsList[self.room_index].room_count == 0:
            self.x = x1
            self.y = y1
            room.roomsList[self.room_index].room_count += 1 # increasing the amount of people in new room

        # 1 players in room
        elif room.roomsList[self.room_index].room_count == 1:
            self.x = x2
            self.y = y2 
            room.roomsList[self.room_index].room_count += 1 # increasing the amount of people in new room

        # 2 players in room
        elif room.roomsList[self.room_index].room_count == 2:
            self.x = x3
            self.y = y3 
            room.roomsList[self.room_index].room_count += 1 # increasing the amount of people in new room

        # 3 players in room
        elif room.roomsList[self.room_index].room_count == 3:
            self.x = x4
            self.y = y4 
            room.roomsList[self.room_index].room_count += 1 # increasing the amount of people in new room

        # Calcualting player location relative to given screen size
        self.player_x = (self.surface_W - Player.player_width) // self.x
        self.player_y = (self.surface_L - Player.player_height) // self.y
            
            
    def DrawPlayer(self):
        
        pygame.draw.rect(self.surface, self.color, (self.player_x, self.player_y, Player.player_width, Player.player_height)) 
