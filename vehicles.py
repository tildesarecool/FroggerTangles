from rectboilerplate import GameRect
from pygame.sprite import Sprite
from common import Common
#from lanes import createLanes

cmn = Common()


class Vehicle(GameRect, Sprite): 
    def __init__(self, xpos: int, ypos: int, width: int, height: int, color: list) -> None: #, dir) -> None:
        '''
        xpos: x position
        ypos: yposition
        width: width of rect
        height: height of rect
        color: color of rect
        dir: direction of car left or right
        '''
        #Sprite.__init__(self)
        super().__init__(xpos, ypos, width, height, color)
        
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.color = color
        
    def draw(self):
        '''
        Drawing the vehicles. 
        '''
        self.rect = self.draw_rect()                
        return self.rect
    
    def moveDirLeft(self):
        self.drawIn = self.draw()
        if self.drawIn.right > 0:
            self.drawIn.right -= 3
            self.xpos = self.drawIn.x
        elif self.width * 2 * -1 <= self.drawIn.right:
#            print(f"bool value of {self.width * -1} <= {self.rect.left} is {bool( self.width * -1 <= self.rect.left )}")                
            self.drawIn.left = cmn.SCREEN_WIDTH - 2
            self.drawIn.x = cmn.SCREEN_WIDTH - 2
            self.xpos = self.drawIn.x

carCount = 0
carList = []    

#for car in cmn.colorList:
#cmn.SCREEN_WIDTH + newCar.width
while carCount <= 1:
    newCar = Vehicle(
        cmn.screen_rect.right + cmn.cellWidth * 2, 
        cmn.screen_rect.centery,
        cmn.cellWidth * 2,
        cmn.vehicleHeight,
        cmn.colorList[carCount]
        )
    carCount += 1
    carList.append(newCar)

