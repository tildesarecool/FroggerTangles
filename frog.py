
from rectboilerplate import GameRect
import pygame as pyg
from pygame.sprite import Sprite
from common import Common
cmn = Common()



class Frog(GameRect, Sprite): 
    def __init__(self, xpos, ypos, width, height, color) -> None:
        Sprite.__init__(self)
        super().__init__(xpos, ypos, width, height, color)

        self.xpos = xpos
        self.ypos = ypos
        self.ypos_start = ypos
        self.width = width
        self.height = height
        self.color = color
        
        self.move_amount = 7  # Amount to move at a time
        self.move_counter = 0  # Counter to track movement
        
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        
# gpt suggested these changes: the self.image lines here in __init__ and moving the self.rect line up here
# i asked gpt if i could just use simple rectangle rather making it a surface so I'm going to try it that way first
        #self.image = pyg.Surface((width, height))
        #self.image.fill(color)
        #self.rect = self.image.get_rect(topleft=(xpos, ypos))

    def draw(self):
        '''
        Drawing the frog: start at bottom/middle
        '''
        self.rect = self.draw_rect()
        #self.update()
        
    def update(self):

        keys = pyg.key.get_pressed()
        if keys[pyg.K_a]:
            self.moving_left = True
        else:
            self.moving_left = False
##################################################
            
        keys = pyg.key.get_pressed()
        if keys[pyg.K_d]:
            self.moving_right = True
        else:
            self.moving_right = False
##################################################


        keys = pyg.key.get_pressed()
        if keys[pyg.K_w]:
            self.moving_up = True
        else:
            self.moving_up = False
            
##################################################

        keys = pyg.key.get_pressed()
        if keys[pyg.K_s]:
            
            self.moving_down = True
        else:
            self.moving_down = False
            
##################################################
            
        if self.moving_right:
            
            if self.xpos <= float(cmn.SCREEN_WIDTH - self.width):
                self.xpos += 7
                
            elif self.xpos >= float(cmn.SCREEN_WIDTH - self.width - 5):
                self.xpos = float(cmn.SCREEN_WIDTH - self.width - 5)
##################################################

        if self.moving_left:
            if self.xpos > 0:
                self.xpos -= 7
            elif self.xpos <= 5.0:
                self.xpos = 5.0

##################################################

        if self.moving_up:
            if self.ypos >= 5:
                self.ypos -= 7.0
                self.moving_up = False
            elif self.ypos >= self.ypos_start:
                self.ypos = self.ypos_start
                self.moving_up = False




##################################################

        if self.moving_down:
            if self.ypos <= self.ypos_start - 5:
                self.ypos += 7
            elif self.rect.bottom >= self.ypos_start:
                self.rect.bottom = float(self.ypos_start - 1)

                


##################################################


'''
class Frog(GameRect, Sprite): 
    def __init__(self, xpos, ypos, width, height, color) -> None:
        Sprite.__init__(self)
        super().__init__(xpos, ypos, width, height, color)

        self.xpos = xpos, 
        self.ypos = ypos, 
        self.width = width, 
        self.height = height, 
        self.color = color

    def draw(self):
        
        #Drawing the frog: start at bottom/middle
        
        self.rect = self.draw_rect() #self.draw_rect()
        
    def update(self):



        pass
        
'''