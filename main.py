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
#from time import sleep



#disp = cmn.screenInfo()
#SCREEN_WIDTH = 800
#SCREEN_HEIGHT = 600

#import pygame as pyg

from pygame.sprite import Group

#import frog
from frog import Frog
#from lanes import Lane
from lanes import createLanes
putInLanes = createLanes()

from vehicles import createVehicles, Vehicle
from trafficlanes import TopVehicleLane

pyg.init()




#dsp = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # also known as the "surface"
clock = pyg.time.Clock()
FPS = 60



froggie = Frog(
    cmn.SCREEN_WIDTH // 2, 
    cmn.SCREEN_HEIGHT - 55, 
    cmn.cellWidth, 
    cmn.cellHeight, 
    cmn.GREEN
    )
    #frogger = Frog(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 10, 100,  100, GREEN)
    
    




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

    createTopLane = TopVehicleLane()
    createTopLane.produceVehics()

#    vehicleGroup.add(
##        createVehicles.regCar, 
##        createVehicles.regBus, 
##        createVehicles.LimeCar
#    )#, regBus)
#    vehicleGroup.u
    
    disp = cmn.screenInfo() # DO NOT MOVE OR COMMENT THIS
    
    while True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                    pyg.quit()
                    return
            elif event.type == pyg.KEYDOWN and event.key == pyg.K_q:
                pyg.quit()
                return
        #dsp.fill((10, 150, 240))

        disp.fill(cmn.BLUEISH)
        #dsp.fill('#00000080')
        
        ### these two were working
        #createLanes.sidewalkOne.draw()
        #createLanes.laneOne.draw()
        
        putInLanes.drawLanes()
#        putInLanes.sidewalkOne.rect.b
        createTopLane.update()
        
        #createLanes.EndZone.draw()
        
        #addTraffic()
        #VehicleSpawner()
        
        #createVehicles.regCar.draw()
        #regBus.draw()
        

        froggie.update()
        
        froggie.draw()
        


        pyg.display.flip()        
        clock.tick(FPS)
        
        
        
if __name__ == '__main__':
    main()

#game()
