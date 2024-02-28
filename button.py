import pygame

class Button:
    def __init__(self, img, x, y):
        self.image = img
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.clicked=False
        self.width = img.get_width()
        self.length = img.get_height()


    def drawButton(self, surface):
      
        action = False

        pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            
            if pygame.mouse.get_pressed()[0] and not self.clicked: # Left: [0], Middle: [1], Right: [2] 
                self.clicked = True
                action = True

            if not pygame.mouse.get_pressed()[0]:
                self.clicked=False

        surface.blit(self.image, (self.rect.x, self.rect.y))
        
        return action