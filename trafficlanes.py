from rectboilerplate import GameRect
from common import Common
cmn = Common()
from pygame.sprite import Group
from vehicles import createVehicles, Vehicle


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


class TopVehicleLane():
    def __init__(self) -> None:
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
        
    #RegCarRect = createVehicles.regCar.draw_rect()
    
    
    #Car.ypos = putInLanes.laneOneRect.top + 10
    #RegCarRect.y = Car.ypos
    
    #Car.xpos = cmn.CENTER_X
    #RegCarRect.x = Car.xpos
        #self.produceVehics()
        

    def produceVehics(self):
        
        if len(self.vehicleGroup) < self.carLimit:
            
            self.newCar = Vehicle(
                0,
                (cmn.CENTER_Y - cmn.cellHeight ) + cmn.cellHeight  + 20,
                cmn.cellWidth * 3, 
                cmn.vehicleHeight,
                cmn.WHITE,
                )
            self.NewCarRect = self.newCar.draw_rect()
            
            self.NewCarRect.y = self.newCar.ypos
            self.NewCarRect.x = self.newCar.xpos

            #self.newCar.moveDirLeft()
            #self.newCar.draw()
            
            self.vehicleGroup.add(self.newCar)
            self.carList.append(self.newCar)
            print(f"length of the carList is {len(self.carList)}") # <= {self.rect.left} is {bool( self.width * -1 <= self.rect.left )}")
            
    def update(self):
        """move the vehicles across the screen"""
        print(f"value of newcar xpos is  {self.newCar.xpos} and ypos {self.newCar.ypos}")        
        self.newCar.draw()
        self.newCar.moveDirLeft()

#        self.x += self.settings.bullet_speed
#        self.rect.x = self.x
            

class MiddleVehicleLane():
    def __init__(self) -> None:
        pass

class BottomVehicleLane():
    def __init__(self) -> None:
        pass    


