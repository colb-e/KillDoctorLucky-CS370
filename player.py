import pygame
import room

class Player:

    # All players will be this size
    player_width, player_height = 50, 30

    def __init__(self, surface, color, room_num, x, y):
        self.surface = surface
        self.surface_W, self.surface_L = surface.get_size()
        self.color = color
        self.room_num = room_num
        self.x = x
        self.y = y
        
    def updatePlayer(self, room_num):
        self.room_num = room_num #setting players current room_num to specified room_num
        
        x, y = room.roomsList[self.room_num].roomX, room.roomsList[self.room_num].roomY # grabbing x and y values of room player is moving to
        
        # possibly we could make an if statement for each amount of players to make placement more predictable
        # we would have an if for 1, 2, 3 players 
        # if a player is already in the new room move to current player to the side
        if room.roomsList[self.room_num].room_count > 0:
            self.x = x - 0.1
            self.y = y 
            room.roomsList[self.room_num].room_count += 1 # increasing the amount of people in new room
            
        else:
            self.x = x
            self.y = y
            room.roomsList[self.room_num].room_count += 1 # increasing the amount of people in new room
        
    def DrawPlayer(self):
        # Calcualting player location relative to given screen size
        player_x = (self.surface_W - Player.player_width) // self.x
        player_y =  (self.surface_L - Player.player_height) // self.y
        
        pygame.draw.rect(self.surface, self.color, (player_x, player_y, Player.player_width, Player.player_height)) 
