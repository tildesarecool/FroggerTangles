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
from time import sleep



disp = cmn.screenInfo()
#SCREEN_WIDTH = 800
#SCREEN_HEIGHT = 600

#import pygame as pyg

from pygame.sprite import Group

#import frog
from frog import Frog
from lanes import Lane
from cars import Car

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
class createLanes():
    def __init__(self) -> None:
         pass
    
    
    laneOne = Lane(
        #0, 
        40, # 40 px in from left side of screen
        cmn.SCREEN_HEIGHT - (froggie.height * 6) - 20, # how many px up from bottom of screen
        cmn.SCREEN_WIDTH - 50, # the width of the screen minus 50 px
        froggie.height * 5, # 5 times the height of the frog. kind of arbitrary
        cmn.SILVER # predefined color
        )
    #laneOne.rect.x = laneOne.xpos
    #laneOne.rect.y = laneOne.ypos

    sidewalkOne = Lane(
        #0,
        #100,
        laneOne.xpos,
        #laneOne.draw_rect().top,
        #cmn.SCREEN_HEIGHT - (froggie.height * 8) ,
        laneOne.height - 45,
        #laneOne.ypos + froggie.height,
        cmn.SCREEN_WIDTH - 50,
        froggie.height * 1.5,
        cmn.GREY
        )

    EndZone = Lane(
        0,
        #laneOne.draw_rect().top,
        #cmn.SCREEN_HEIGHT - (froggie.height * 8) ,
        0,
        cmn.SCREEN_WIDTH,
        froggie.height * 1.5,
        cmn.AQUA
        )


class createVehicles():
    def __init__(self) -> None:
         pass

    regCar = Car(
        0,
        0,
        froggie.width * 3, 
        froggie.height * 1.5,
        cmn.WHITE,
        "right" # it works with "left" at least
        )
    if regCar.dir == "left":
        regCar.rect.left = cmn.SCREEN_WIDTH - 50
    elif regCar.dir == "right":
        regCar.rect.right = -2

    regBus = Car(
        0,
        0,
        froggie.width * 4, 
        froggie.height * 1.5,
        cmn.BLACK,
        "left" # new parameter -  should probably update addtraffic() below too
        )



#regBus.xpos = regCar.xpos - 60
carsGroup = Group()



carsGroup.add(createVehicles.regCar, createVehicles.regBus)#, regBus)

def addTraffic():
    #carsGroup.draw(disp)
    regCarRect = createVehicles.regCar.draw_rect()
    regCarRect.y = cmn.SCREEN_HEIGHT - (froggie.height * 6) - 15
    #regCarRect.x = cmn.SCREEN_WIDTH - createVehicles.regCar.width - 15
    
    
    #createVehicles.regCar.xpos = regCarRect.x
    createVehicles.regCar.ypos = regCarRect.y
    
    
    
    createVehicles.regCar.draw()    
###################################################
    #createVehicles.regBusRect = createVehicles.regCar.draw_rect()
    #createVehicles.regBusRect.y = createVehicles.regCarRect.y
    #createVehicles.regBus.ypos = createVehicles.regBusRect.y
    #createVehicles.regBus.xpos = createVehicles.regCarRect.x + (createVehicles.regCarRect.width + 50)
    #createVehicles.regBus.draw()
    #regBusRect.right = regCarRect.width - 200
    #regBus.ypos = regCar.ypos
    
    
#    for v in carsGroup:

#        v.draw()

    

def main() -> None:
    
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
        createLanes.sidewalkOne.draw()
        createLanes.laneOne.draw()
        createLanes.EndZone.draw()
        
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
