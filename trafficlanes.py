from rectboilerplate import GameRect
from common import Common
from lanes import createLanes

cmn = Common()
putInLanes = createLanes()
from pygame.sprite import Group
from vehicles import  Vehicle #createVehicles,


# Idea 1: 
# create three (classes? one class with multiple methods?) for each of the three lanes of traffic:
# upperlane, middle lane, lower lane

# idea 2: 
# create a list of cars objects, one for each color 
# do the same for busses and any other vehicle type i think of (motorcycle?)
# once vehicles are create with all the colors they're added to a list (or tuple) so they're read
# and also added to a sprite group

# then it would just a matter of spawning in a car in a given lane with that lane's assigned direction
# oh and something similar for log/turtle/alligator section in the upper half of the screen. haven't even thought about it yet.

#still thinking about spacing between car spawning
# draw_rect()?


class TopVehicleLane(GameRect):
    '''Create vehicles for the top lane of traffic'''
    def __init__(self, xpos, ypos, width, height, color) -> None:
        super().__init__(xpos, ypos, width, height, color)

        self.carLimit = 1
        self.carList = []
        self.vehicleGroup = Group()
        
        self.colorList = [
            cmn.BLACK, 
            cmn.SILVER, 
            cmn.GREY, 
            cmn.GREEN, 
            cmn.LITEBLUE,
            cmn.LIME,
            cmn.WHITE,
            cmn.BLUEISH,
            cmn.AQUA,
        ]
        

        self.newCar = Vehicle(
            xpos,
            ypos,
            width,
            height,
            color
        )


#        class createVehicles():
#    def __init__(self) -> None:
#        pass

#        self.newCar = Vehicle(
#        putInLanes.laneOne.top + 10,#0,
#        (cmn.CENTER_Y - cmn.cellHeight ) + cmn.cellHeight  + 20,
#        cmn.cellWidth * 3, 
#        cmn.vehicleHeight,
#        cmn.WHITE,
#        )

    def draw(self):
        
#       not sure to use the draw_rect or just draw here        
       self.rect = self.draw_rect()
#        self.newCar.draw()
       
#       self.NewCarRect = self.newCar.rect
#    
#       self.NewCarRect.y = self.newCar.ypos
#       self.NewCarRect.x = self.newCar.xpos
        
        #pass
    
    
    def update(self):
        
        """move the vehicles across the screen"""
        self.newCar.moveDirLeft()
        #self.createVehicles().
        #pass

#        print(f"value of newcar xpos is  {self.newCar.xpos} and ypos {self.newCar.ypos}")        
#        self.newCar.draw()
#        self.newCar.moveDirLeft()

#        self.x += self.settings.bullet_speed
#        self.rect.x = self.x


class MiddleVehicleLane():
    def __init__(self) -> None:
        pass

class BottomVehicleLane():
    def __init__(self) -> None:
        pass    


#class createVehicles():
#    def __init__(self) -> None:
##        pass
#        self.newCar = Vehicle(
#        putInLanes.laneOne.top + 10,#0,
#        (cmn.CENTER_Y - cmn.cellHeight ) + cmn.cellHeight  + 20,
#        cmn.cellWidth * 3, 
#        cmn.vehicleHeight,
#        cmn.WHITE,
#        )
        
