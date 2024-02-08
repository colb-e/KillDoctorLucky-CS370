import pygame

class Player:

    player_width, player_height = 50, 30

    def __init__(self, surface, color, player_x, player_y):
        self.surface = surface
        self.color = color
        self.player_x = player_x
        self.player_y = player_y

    def Draw(self):

        screen_W, screen_L = self.surface.get_size() # setting length and width of screen
        x, y = (screen_W - Player.player_width) // self.player_x, (screen_L - Player.player_height) // self.player_y #calculating location based in the size of the screen and given cords
        pygame.draw.rect(self.surface, self.color, (x, y, Player.player_width, Player.player_height)) 