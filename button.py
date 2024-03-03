import pygame

class Button:
    def __init__(self, surface, img, x, y, scale):
        self.image = img
        self.surface_W, self.surface_L = surface.get_size() 
        img_W, img_L = img.get_size() # grabbing image size
        
        img_W = (img_W * scale) # multiplying given scale with the image width
        img_L = (img_L * scale) # multiplying given scale with the image length
        self.image = pygame.transform.scale(img, (img_W, img_L)) # adjusting to new image size
        
        btn_X, btn_Y = (self.surface_W - img_W) // x, (self.surface_L - img_L) // y # placing the button in a relative location the // 1 and the // 1000 decide the placement
        self.rect=self.image.get_rect()
        self.rect.topleft=(btn_X, btn_Y)
        self.clicked=False
        

    # This function will add a created button to the sidebar. This function will use the scale that was stated when the button was created and 
    # adjust the width of the button to the width of the sidebar. We will be able to give another x and y value to postion where on the sidebar
    # that we would like to place the button.
    def addToSidebar(self, board_W, x, y):

        btn_W, btn_L = self.image.get_size()
        btn_W = self.surface_W - board_W
        
        self.image = pygame.transform.scale(self.image, (btn_W, btn_L))

        btn_X, btn_Y = (self.surface_W - btn_W) // x, (self.surface_L - btn_L) // y
        self.rect=self.image.get_rect()
        self.rect.topleft=(btn_X, btn_Y)

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
