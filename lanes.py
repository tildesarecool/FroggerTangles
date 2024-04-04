# attempt to draw some lanes:
# first car lanes, then middle sidewalk, then river with log lanes

# I assume this will be called first so everything else will be on top of them
# just rectangles of different colors and heights - the width of the screen

from rectboilerplate import GameRect
#import pygame as pyg
#from pygame.sprite import Sprite
from common import Common
#from frog import Frog
cmn = Common()

class Lane(GameRect):#, Sprite): 
    '''Rectangles for background to represent lanes'''

    def __init__(self, xpos, ypos, width, height, color) -> None:
        super().__init__(xpos, ypos, width, height, color)
        #Sprite.__init__(self)
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


class createLanes():
    def __init__(self) -> None:
         # GPT Note:
         # Make sure to call drawLanes() after initializing the createLanes 
         # object to position the lanes properly.
         #createLanes.drawLanes(self)
       
        self.sidewalkOne = Lane(
            0,
            cmn.screen_rect.centery - 30, # cmn.screen_rect.centery - 30 works - still gap at 31
            #cmn.CENTER_Y - cmn.cellHeight,# + 15,# * 1.2, # originally * 2

            cmn.SCREEN_WIDTH,
            cmn.cellHeight * 1.5,
            cmn.GREY
            )
        self.laneOne = Lane(
            
           #0, 
            0, # 0 px in from left side of screen
            self.sidewalkOne.ypos - self.sidewalkOne.height,#cmn.CENTER_Y,# - cmn.cellHeight * 2,#cmn.SCREEN_HEIGHT - (froggie.height * 6) - 20, # how many px up from bottom of screen
            cmn.SCREEN_WIDTH,# - 50, # the width of the screen minus 50 px
            
            # below: set a vehicle height in common then multiplied that by 3. Then added 30. So there 
            # can be verticle space between vehicles/top and bottom edge. I can always adjust it
            (cmn.vehicleHeight * 3) + 30, 
            cmn.SILVER # predefined color
            )
   
        self.EndZone = Lane(
            0,
            #laneOne.draw_rect().top,
            #cmn.SCREEN_HEIGHT - (froggie.height * 8) ,
            0,
            cmn.SCREEN_WIDTH,
            cmn.cellHeight * 1.5,
            cmn.AQUA
            )
    
    def drawLanes(self):

        self.laneOne.ypos = (cmn.SCREEN_HEIGHT - self.laneOne.height - (cmn.cellHeight * 1.5))
        self.laneOneRect = self.laneOne.draw_rect()
        #laneOneRect.top = SideWalkRect.bottom + 1
         # self.laneOne.ypos + (self.sidewalkOne.width)

        #laneOneRect.y = self.laneOne.ypos
        
################################################################

        #self.sidewalkOne.ypos = cmn.cellHeight * 2
        self.SideWalkRect = self.sidewalkOne.draw_rect()
        self.SideWalkRect.x = self.sidewalkOne.xpos
        self.SideWalkRect.y = self.sidewalkOne.ypos
        
        
        self.laneOneRect.y = self.SideWalkRect.bottom
        self.laneOneRect.x = self.laneOne.xpos
        #laneOneRect.top = SideWalkRect.bottom
        
        
        #EndZoneRect = self.EndZone.draw_rect()
        self.EndZone.draw_rect()
                
        #print(f"value of self.laneOneRect.top is {laneOneRect.top} and value of SideWalkRect.bottom is {SideWalkRect.bottom}")
        #print(f"value of self.laneOne.ypos is {self.laneOne.ypos}")
        #self.laneOne.xpos = laneOneRect.x
        
        
        #self.laneOne.ypos = laneOneRect.y
        
        
        #laneOneRect.x = self.sidewalkOne.xpos
        #laneOneRect.y = self.sidewalkOne.ypos
        
        

        
        #pass