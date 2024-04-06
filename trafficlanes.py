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

#
# I guess i forgot about idea 2 above. I started to go back to the random spawning
# i'm not random spawning cars, i'm creating cars and adding them to the list
# then accessing the list of cars to send them across the screen
#

from rectboilerplate import GameRect
from common import Common
from lanes import createLanes

cmn = Common()
putInLanes = createLanes()
from pygame.sprite import Group
from vehicles import  Vehicle #createVehicles,

class TopVehicleLane(GameRect):
    '''Create vehicles for the top lane of traffic'''
    def __init__(self, xpos, ypos, width, height, color=cmn.WHITE) -> None:
        super().__init__(xpos, ypos, width, height, color)

        self.carLimit = 2
        self.carList = []
        self.vehicleGroup = Group()

        i = 0
        while i < self.carLimit:
            self.newCar = Vehicle(
                xpos,
                ypos,
                width,
                height,
                'blue'#color
                #self.colorList[i]
            )
            i += 1

            self.carList.append(self.newCar)
            self.vehicleGroup.add(self.newCar)
        
        print(f"len of car list is {len(self.carList)}")

    def draw(self):
        
        for car in self.carList:        
            car.draw()
            #self.newCar.draw()
    
    
    def update(self):
        
        """move the vehicles across the screen"""
        #self.newCar.moveDirLeft()
        for car in self.carList:
            car.moveDirLeft()


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
        
