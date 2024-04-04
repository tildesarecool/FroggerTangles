#import rectboilerplate
#from common import dsp

from rectboilerplate import GameRect

#import pygame as pyg

from pygame.sprite import Sprite

from common import Common
from lanes import createLanes

cmn = Common()
putInLanes = createLanes()


class Vehicle(GameRect, Sprite): 
    def __init__(self, xpos, ypos, width, height, color) -> None: #, dir) -> None:
        '''
        xpos: x position
        ypos: yposition
        width: width of rect
        height: height of rect
        color: color of rect
        dir: direction of car left or right
        '''
        Sprite.__init__(self)
        super().__init__(xpos, ypos, width, height, color)

        self.xpos = xpos
        self.ypos = ypos
        #self.ypos_start = ypos
        self.width = width
        self.height = height
        self.color = color
        #self.dir = dir
        
        self.StartLeftPos = self.width * -1 #0
        self.StartRightPos = cmn.SCREEN_WIDTH + 50 # should be 50 px to the right of the screen. right?
        
        
        # I moved this from the draw method to this init() method and nothing is apparently broken 
        # so I'm going to leave it here.
        # I think this makes more sense since the draw() method is in the game loop
        # this  rect assignment is happening 60 times per second which seems uncessary.
        self.rect = self.draw_rect()                
#        self.rect = self.draw_rect()        
        self.rect.left = cmn.SCREEN_WIDTH - self.width * 2

    def draw(self):
        '''
        Drawing the vehicles. 
        '''
        self.rect = self.draw()                
    def moveDirLeft(self):
            
        if self.rect.right > 0:# and self.rect.right < cmn.SCREEN_WIDTH:
            #self.rect.left =  self.rect.width  + cmn.SCREEN_WIDTH
            self.rect.right -= 3
            self.xpos = self.rect.x
            #print(f"Current x position is {self.xpos}")
            #print(f"Current rect right value is {self.rect.right}")
            #print(f"Current rect left value is {self.rect.left}")
            #print(f"value of self.width * -1 is {self.width * -1}")

        elif self.width * 2 * -1 <= self.rect.right : #or self.rect.right <= 1:
            #print(f"Value of SCREEN_WIDTH - self.rect.width is {float(SCREEN_WIDTH - self.width)}")
            #print(f"Current x position is in else is {self.xpos}")
            print(f"bool value of {self.width * -1} <= {self.rect.left} is {bool( self.width * -1 <= self.rect.left )}")                
            self.rect.left = cmn.SCREEN_WIDTH - 2
            self.rect.x = cmn.SCREEN_WIDTH - 2
            self.xpos = self.rect.x
        #elif dir == "right":
    def moveDirRight(self):
        if self.rect.left < cmn.SCREEN_WIDTH:
            self.rect.left += 3
            self.xpos = self.rect.x
        elif cmn.SCREEN_WIDTH + (self.width * 2) >= self.rect.left:
            self.rect.right = self.StartLeftPos #self.width * -1
            self.rect.x = self.StartLeftPos
            self.xpos = self.rect.x
            

#class createVehicles():
#    def __init__(self) -> None:
#         pass
#     
##    regCar = Vehicle(
##        0,
##        (cmn.CENTER_Y - cmn.cellHeight ) + cmn.cellHeight  + 20 ,#putInLanes.laneOneRect.top + 10,
##        cmn.cellWidth * 3, 
##        cmn.vehicleHeight,
##        cmn.WHITE,
##        #"left".lower() # it works with "left" at least
##        )
#    
##    if regCar.dir == "left":
##        regCar.rect.left = cmn.SCREEN_WIDTH - 5
##    elif regCar.dir == "right":
##        regCar.rect.right = 0
#
#    regBus = Vehicle(
#        0,
#        0,
#        cmn.cellWidth * 4, 
#        cmn.vehicleHeight,
#        cmn.BLACK,
##        "left".lower() # new parameter -  should probably update addtraffic() below too
#        )
#    #regBus.rect.bottom # no errors form this line. not sure what that means
#    
#    LimeCar = Vehicle(
#        cmn.SCREEN_WIDTH + cmn.cellWidth * 2,
#        0,
#        cmn.cellWidth * 3,
#        cmn.vehicleHeight,
#        cmn.LIME,
##        "left".lower()
#    )
