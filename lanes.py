# attempt to draw some lanes:
# first car lanes, then middle sidewalk, then river with log lanes

# I assume this will be called first so everything else will be on top of them
# just rectangles of different colors and heights - the width of the screen

from rectboilerplate import GameRect
#import pygame as pyg
from pygame.sprite import Sprite
from common import Common
cmn = Common()

class Lane(GameRect, Sprite): 
    '''Rectangles for background to represent lanes'''

    def __init__(self, xpos, ypos, width, height, color) -> None:
        super().__init__(xpos, ypos, width, height, color)
        Sprite.__init__(self)
#    def __init__(self, xpos, ypos, width, height, color) -> None:
#        super().__init__( xpos, ypos, width, height, color)
#        #Sprite.__init__(self) # not entirely clear I need sprite init() just for lanes draw
#        #
##        pass
#        self.xpos = xpos
#        self.ypos = ypos
#    #    #self.ypos_start = ypos
#        self.width = width
#        self.height = height
#        self.color = color
#        
        #self.rect = self.draw_rect()

    def draw(self ):#, xpos, ypos, width, height, color):
        '''
        Drawing the lane(s): on the screen
        '''
        #
        self.rect = self.draw_rect()
        #self.rect
#        self.xpos = xpos
#        self.ypos = ypos
#        #self.ypos_start = ypos
#        self.width = width
#        self.height = height
#        self.color = color