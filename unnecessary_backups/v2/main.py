# attempt to make some kind of version of the very blocky version of frogger
# written by TheCodingTrain in JS/p5.js
# then re-factored in video
# https://www.youtube.com/watch?v=c6WdJltqEtM
# 29 Feb 2024 (it's a leap year)

#from common import dsp
#from common import SCREEN_WIDTH, SCREEN_HEIGHT
from common import Common 

cmn = Common()


import pygame as pyg

from pygame.sprite import Group

#import frog
from frog import Frog
#from lanes import Lane
from lanes import createLanes

putInLanes = createLanes()
#from vehicles import Vehicle # createVehicles,
from trafficlanes import TopVehicleLane

pyg.init()



#dsp = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # also known as the "surface"
clock = pyg.time.Clock()
FPS = 60


#print(f"value of putInLanes.laneOne.rect.top is {putInLanes.laneOne.rect.top} while putInLanes.laneOne.ypos is {putInLanes.laneOne.ypos}")

froggie = Frog(
    cmn.SCREEN_WIDTH // 2, 
    cmn.SCREEN_HEIGHT - 55, 
    cmn.cellWidth, 
    cmn.cellHeight, 
    cmn.GREEN
    )
    #frogger = Frog(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 10, 100,  100, GREEN)
    # ypos of sidewalkone: 
    # cmn.screen_rect.centery - 30
#
# I guess i forgot about idea 2: I started to go back to the random spawning
# i'm not random spawning cars, i'm creating cars and adding them to the list
# then accessing the list of cars to send them across the screen
#








#regBus.xpos = regCar.xpos - 60




#def addTraffic():

#    regCarRect = createVehicles.regCar.draw_rect()
#    regCarRect.y = cmn.SCREEN_HEIGHT - (cmn.cellHeight * 6) - 15
#    
#    regCarRect.left = cmn.SCREEN_WIDTH + createVehicles.regCar.width - 5
#    
#    createVehicles.regCar.ypos = regCarRect.y
#    createVehicles.regCar.xpos = regCarRect.x
#    
#    ###
#    createVehicles.regCar.draw() 
#    ###
#
####################################################
#    regBusRect = createVehicles.regBus.draw_rect()
#    regBusRect.y = regCarRect.y# + regCarRect.width
#    
#    regBusRect.left = regCarRect.right - regBusRect.width * 2
#    
#    createVehicles.regBus.ypos = regBusRect.y
#    createVehicles.regBus.xpos = regBusRect.x
#    createVehicles.regBus.draw() 
####################################################
#
#    limeCarRect = createVehicles.LimeCar.draw_rect()
#    limeCarRect.y = regBusRect.y
#    
#    limeCarRect.left = regBusRect.right - regBusRect.width * 2
#    
#    createVehicles.LimeCar.ypos = limeCarRect.y
#    createVehicles.LimeCar.xpos = limeCarRect.x
###################################################
    
#    print(f"createVehicles.LimeCar.xpos is {createVehicles.LimeCar.xpos}")
#    print(f"limeCarRect.x is {limeCarRect.x}")
        #    print(f"createVehicles.regCar.xpos is {createVehicles.regCar.ypos}")
        #    print(f"regCarRect.x is {regCarRect.x}")
        #    print(f"regCarRect.left is {regCarRect.left}")
        #    print(f"regCarRect.right is {regCarRect.right}")


#def VehicleSpawner():
    
    # ideally this would a random vehicle type/color
#    RegCarRect = createVehicles.regCar.draw_rect()
#    Car = createVehicles.regCar
#    
#    #Car.ypos = putInLanes.laneOneRect.top + 10
#    RegCarRect.y = Car.ypos
#    
#    #Car.xpos = cmn.CENTER_X
#    RegCarRect.x = Car.xpos
    #Car.color = cmn.AQUA
    
#    createVehicles.regCar.draw()
    
    #createTopLane.produceVehics()
    #.produceVehics()
#    print(f"createVehicles.regCar.xpos is {createVehicles.regCar.ypos}")
#    print(f"regCarRect.x is {RegCarRect.x}")
#    print(f"regCarRect.left is {RegCarRect.left}")
#    print(f"regCarRect.right is {RegCarRect.right}")
    
    #Car.moveDirLeft()
    #Car.moveDirRight()
    
def main() -> None:

    #.createVehicles()
#    createTopLane.draw()
    
#    vehicleGroup.add(
##        createVehicles.regCar, 
##        createVehicles.regBus, 
##        createVehicles.LimeCar
#    )#, regBus)
#    vehicleGroup.u
    '''
    ypos
    width
    height
    color_list
    '''
    createTopLane = TopVehicleLane(
        cmn.SCREEN_WIDTH + cmn.cellWidth * 2,
        (cmn.CENTER_Y - cmn.cellHeight ) + cmn.cellHeight  + 50,
        
        
        cmn.cellWidth * 2.5, 
        cmn.vehicleHeight,
        cmn.colorList,    
    )    
    
    disp = cmn.screenInfo() # DO NOT MOVE OR COMMENT THIS
    
    while True:
        delta_time = createTopLane.clock.tick(60)  # Get the time passed since the last frame

        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                    pyg.quit()
                    return
            elif event.type == pyg.KEYDOWN and event.key == pyg.K_q:
                pyg.quit()
                return
#            createTopLane.handle_event(event)
        #dsp.fill((10, 150, 240))

        disp.fill(cmn.BLUEISH)
        #dsp.fill('#00000080')
        
        ### these two were working
        #createLanes.sidewalkOne.draw()
        #createLanes.laneOne.draw()
        
        putInLanes.drawLanes()
        
#        if createTopLane.vehicle_spawned:
#            createTopLane.move_vehicles()
#            createTopLane.draw()
#            createTopLane.vehicle_spawned = False
        
        #createTopLane.handle_vehicle_movement()
        createTopLane.handle_vehicle_movement(delta_time)
        createTopLane.draw()

#        createTopLane.handle_vehicle_spawning()
#        createTopLane.update()
#        createTopLane.draw()

        froggie.update()
        
        froggie.draw()
        


        pyg.display.flip()        
        clock.tick(FPS)
        
        
        
if __name__ == '__main__':
    main()

#game()
