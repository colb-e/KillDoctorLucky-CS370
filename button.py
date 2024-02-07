import pygame

class Button():

    def __init__(self, x, y, image, scale):
        self.width = image.get_width()
        self.height = image.get_height()
        self.image = pygame.transform.scale(image, (int(self.width * scale), int(self.height * scale))) 
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y) # location of rectangles top left corner
        self.clicked = False

    def draw(self, surface):
        
        action = False

        # get mouse postion
        pos = pygame.mouse.get_pos()
        
        # check for on hover and clicking input
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: # left click: 0, middle click: 1, right click: 2
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0: # if the button is not being left clicked, self.clicked = false
                self.clicked = False

        # draw button 
        surface.blit(self.image, (self.rect.x, self.rect.y))
        print(self.width)
        print(self.height)
        return action