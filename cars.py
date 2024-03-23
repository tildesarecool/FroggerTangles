#import rectboilerplate
#from common import dsp

from rectboilerplate import GameRect

#import pygame as pyg

from pygame.sprite import Sprite

from common import Common

cmn = Common()



class Car(GameRect, Sprite): 
    def __init__(self, xpos, ypos, width, height, color, dir) -> None:
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
        self.dir = dir
        
        self.StartLeftPos = 0
        self.StartRightPos = cmn.SCREEN_WIDTH - 50

        
        # I moved this from the draw method to this init() method and nothing is apparently broken 
        # so I'm going to leave it here.
        # I think this makes more sense since the draw() method is in the game loop
        # this  rect assignment is happening 60 times per second which seems uncessary.
        
        self.rect = self.draw_rect()
        
        self.xpos = cmn.SCREEN_WIDTH - self.width - 15

    def draw(self):
        '''
        Drawing the frog: start at bottom/middle
        '''
        #self.rect = self.draw_rect()
        #self.update()
        
        if self.dir == "left":
            self.moving_left = self.dir
            self.moveDirection(self.moving_left)
        elif self.dir == "right":        
            self.moving_right = self.dir
            self.moveDirection(self.moving_right)
        
    #def update(self):
    def moveDirection(self, dir):
#        if self.moving_right:
            
#            if self.xpos <= float(cmn.SCREEN_WIDTH - self.width):
#                self.xpos += 7
                
#            elif self.xpos >= float(cmn.SCREEN_WIDTH - self.width - 5):
#                self.xpos = float(cmn.SCREEN_WIDTH - self.width - 5)
##################################################

        #if self.moving_left: # I'm passing in the direction as parameter now
        if dir == "left": 
            #self.xpos -= 3
            self.rect.x = self.xpos
            #if self.xpos > 0:
            #    self.xpos -= 3
            if self.rect.left > 0:
                self.rect.left -= 3
                self.xpos = self.rect.x
                #print(f"Current x position is {self.xpos}")
                #print(f"Current rect right value is {self.rect.right}")
                #print(f"Current rect left value is {self.rect.left}")
                #print(f"value of self.width * -1 is {self.width * -1}")

                #print(f"value of cmn.SCREEN_WIDTH - (self.width * -1) is {cmn.SCREEN_WIDTH - (self.width * -1)}")
            #elif self.rect.left <= 1:# or self.xpos <= 1.0:
            
            elif self.width * -1 <= self.rect.left : #or self.rect.right <= 1:
                #print(f"Value of SCREEN_WIDTH - self.rect.width is {float(SCREEN_WIDTH - self.width)}")
                #print(f"Current x position is in else is {self.xpos}")
                print(f"bool value of {self.width * -1} <= {self.rect.left} is {bool( self.width * -1 <= self.rect.left )}")                
                self.rect.left = cmn.SCREEN_WIDTH - 2
                self.rect.x = cmn.SCREEN_WIDTH - 2
                self.xpos = self.rect.x
        elif dir == "right":
            self.rect.x = self.xpos
            #if self.xpos > 0:
            #    self.xpos -= 3
            #print(f"Current x position is {self.xpos}")
            self.rect.right = -2
            print(f"Current rect right value is {self.rect.right}")
            if self.rect.right <  cmn.SCREEN_WIDTH:
                self.rect.right += 3
                self.xpos = self.rect.x
                #print(f"Current x position is {self.xpos}")
                #print(f"Current rect right value is {self.rect.right}")
                #print(f"Current rect left value is {self.rect.left}")
                #print(f"value of self.width * -1 is {self.width * -1}")

                print(f"value of self.rect.right is {self.rect.right} and value of cmn.SCREEN_WIDTH is {cmn.SCREEN_WIDTH}")
            #elif self.rect.left <= 1:# or self.xpos <= 1.0:
            
            elif self.width  >= (cmn.SCREEN_WIDTH + self.width): #self.rect.left : #or self.rect.right <= 1:
                #print(f"Value of SCREEN_WIDTH - self.rect.width is {float(SCREEN_WIDTH - self.width)}")
                #print(f"Current x position is in else is {self.xpos}")
                print(f"bool value of {self.width * -1} <= {self.rect.left} is {bool( self.width * -1 <= self.rect.left )}")                
                #self.rect.right = cmn.SCREEN_WIDTH - 2
                self.rect.right = -2
                self.rect.x = -2
                self.xpos = self.rect.x
