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
import pygame as pyg
from rectboilerplate import GameRect
from common import Common
from lanes import createLanes

cmn = Common()
putInLanes = createLanes()
from pygame.sprite import Group
from vehicles import  Vehicle #createVehicles,

class TopVehicleLane(GameRect):
    '''Create vehicles for the top lane of traffic'''
    def __init__(self, xpos,ypos, width, height, color_list) -> None:
        super().__init__(xpos, ypos, width, height, cmn.colorList[0])
        #super().__init__()

        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.color_list = color_list
        
        self.vehicle_list = []  # List to store vehicle instances
        self.clock = pyg.time.Clock()
        self.time_since_last_move = 0
        #self.time_since_last_spawn = 0
        self.spawn_interval = 500  # Spawn interval in milliseconds (0.5 seconds)
        #self.spawn_event = pyg.USEREVENT + 1
        #self.vehicle_spawned = False
        
        #pyg.time.set_timer(self.spawn_event, self.spawn_interval)

        
        for color in self.color_list:
            new_vehicle = Vehicle(self.xpos,self.ypos,self.width, self.height, color)
            self.vehicle_list.append(new_vehicle)
            #new_vehicle.draw_rect()


#        while i < self.carLimit:
#            self.newCar = Vehicle(
#                xpos,
#                ypos,
#                width,
#                height,
#                'blue'#color
#                #cmn.colorList[i]
#            )
#            i += 1
#
#            self.carList.append(self.newCar)
#            self.vehicleGroup.add(self.newCar)
#        
        print(f"len of car list is {len(self.vehicle_list)}")



######### took these out as experiment to try and get the timer spacing between cars right.

    def move_vehicle(self):
         """move the vehicles across the screen"""
         print("Made it to move vehic method")    
         if self.vehicle_list:
            self.vehicle_list[0].moveDirLeft()
        #print("Made it to move vehic method")    
        
        
        

    def draw(self):
        if self.vehicle_list:
            self.vehicle_list[0].draw()
            #print("Made it to draw method, if loop")
        
#        for vehicle in self.vehicle_list:        
#            vehicle.draw()
            #self.newCar.draw()

    def update(self):
        # Update the movement of the vehicle
        #self.move_vehicle()    
        
        if self.vehicle_list:
            self.vehicle_list[0].moveDirLeft()
            print("Made it to update method, if loop")
            #self.vehicle_list[]
    
 
   
    def handle_vehicle_movement(self, delta_time):
        # Update the timer and move the vehicle if enough time has passed
        #print("Made it to handle vehic mov method")    
        print(f"value of self.clock.get_time() is {self.clock.get_time()}")    
        self.time_since_last_move += delta_time #self.clock.get_time()
        if self.time_since_last_move >= self.spawn_interval:
            # Reset the timer
            self.time_since_last_move = 0
            # Move the vehicle
            self.move_vehicle()    
            print("Made it to handle vehic mov method, if loop")    
    
    
        #self.newCar.moveDirLeft()
 #       for vehicle in self.vehicle_list:
 #           vehicle.moveDirLeft()
            
#    def handle_event(self, event):
#        if event.type == self.spawn_event:
#            # spawn new vehicle
#            new_vehicle = self.vehicle_list.pop(0)
#            new_vehicle.xpos = cmn.SCREEN_WIDTH + cmn.cellWidth * 2
#            self.vehicle_list.append(new_vehicle)
#            self.vehicle_spawned = True
        


    #def handle_vehicle_spawning(self):
    ## Update the timer and spawn a new vehicle if enough time has passed
#
#        self.time_since_last_spawn += self.clock.get_time()
#
#        # Check if enough time has passed to spawn a new vehicle - this doesn't space out either
#        if self.time_since_last_spawn >= self.spawn_interval:
#            # Spawn a new vehicle
#            new_vehicle = self.vehicle_list.pop(0)  # Get the first vehicle from the list
#            new_vehicle.rect.x = cmn.SCREEN_WIDTH + cmn.cellWidth * 2  # Start off-screen
#            self.vehicle_list.append(new_vehicle)  # Add the vehicle to the end of the list
#            #self.draw()
#            self.vehicle_list.
#
#            # Reset the timer
#            self.time_since_last_spawn = 0        




    # since the vehicles all seem to be spawning at once and overlapping each other as the move right/left
    # gpt suggested an intervening step to check on the timer
#        self.time_since_last_spawn += self.clock.get_time()
#        if self.time_since_last_spawn >= self.spawn_interval:
#            # Reset the timer
#            self.time_since_last_spawn = 0  
#            print(f"The timer has reset")


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
        
