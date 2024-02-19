import pygame

class Player:

    # All players will be this size
    player_width, player_height = 50, 30

    def __init__(self, surface, color, room_num, x, y):
        self.surface = surface
        self.surface_W, self.surface_L = surface.get_size()
        self.color = color
        self.room = room_num
        # Calcualting player location relative to given screen size
        self.player_x = (self.surface_W - Player.player_width) // x
        self.player_y =  (self.surface_L - Player.player_height) // y
         
    def DrawPlayer(self):
       pygame.draw.rect(self.surface, self.color, (self.player_x, self.player_y, Player.player_width, Player.player_height)) 
