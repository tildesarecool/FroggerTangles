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


from vehicles import createVehicles

pyg.init()




#dsp = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # also known as the "surface"
clock = pyg.time.Clock()
FPS = 20



froggie = Frog(
    cmn.SCREEN_WIDTH // 2, 
    cmn.SCREEN_HEIGHT - 55, 
    cmn.cellWidth, 
    cmn.cellHeight, 
    cmn.GREEN
    )
    #frogger = Frog(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 10, 100,  100, GREEN)
    
    




#regBus.xpos = regCar.xpos - 60




def addTraffic():

    regCarRect = createVehicles.regCar.draw_rect()
    regCarRect.y = cmn.SCREEN_HEIGHT - (cmn.cellHeight * 6) - 15
    
    regCarRect.left = cmn.SCREEN_WIDTH + createVehicles.regCar.width - 5
    
    createVehicles.regCar.ypos = regCarRect.y
    createVehicles.regCar.xpos = regCarRect.x
    
    
    createVehicles.regCar.draw()    
    print(f"createVehicles.regCar.xpos is {createVehicles.regCar.ypos}")
    print(f"regCarRect.x is {regCarRect.x}")
    print(f"regCarRect.left is {regCarRect.left}")
    print(f"regCarRect.right is {regCarRect.right}")
    
###################################################
    regBusRect = createVehicles.regBus.draw_rect()
    regBusRect.y = regCarRect.y# + regCarRect.width
    
    regBusRect.left = regCarRect.right - regBusRect.width * 2
    
    createVehicles.regBus.ypos = regBusRect.y
    createVehicles.regBus.xpos = regBusRect.x
###################################################

    limeCarRect = createVehicles.LimeCar.draw_rect()
    limeCarRect.y = regBusRect.y
    
    limeCarRect.left = regBusRect.right - regBusRect.width * 2
    
    createVehicles.LimeCar.ypos = limeCarRect.y
    createVehicles.LimeCar.xpos = limeCarRect.x
    
#    print(f"createVehicles.LimeCar.xpos is {createVehicles.LimeCar.xpos}")
#    print(f"limeCarRect.x is {limeCarRect.x}")


def main() -> None:
    putInLanes = createLanes()
    
    vehicleGroup = Group()
    vehicleGroup.add(
        createVehicles.regCar, 
        createVehicles.regBus, 
        createVehicles.LimeCar
    )#, regBus)
    
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
        
        
        #createLanes.EndZone.draw()
        
        addTraffic()
        
        #createVehicles.regCar.draw()
        #regBus.draw()
        

        froggie.update()
        
        froggie.draw()
        


        pyg.display.flip()        
        clock.tick(FPS)
        
        
        
if __name__ == '__main__':
    main()

#game()
