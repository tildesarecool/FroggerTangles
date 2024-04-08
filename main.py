# 
# 
# 
# 
# 
# 
# 7 April 2024 (it's a leap year)


from common import Common 
cmn = Common()

import pygame as pyg
from frog import Frog
from vehicles import Vehicle, newCar, carList

clock = pyg.time.Clock()

froggie = Frog(
    cmn.SCREEN_WIDTH // 2, 
    cmn.SCREEN_HEIGHT - 55, 
    cmn.cellWidth, 
    cmn.cellHeight, 
    cmn.colorList[3]
    )


def main() -> None:

    disp = cmn.dsp # DO NOT MOVE OR COMMENT THIS
    
    if pyg.get_init == False:    
        pyg.init()
    
#    carList[0].xpos = cmn.SCREEN_WIDTH + newCar.width
#    carList[1].xpos = cmn.SCREEN_WIDTH + newCar.width
    #newCar.xpos = cmn.screen_rect.centerx# + (newCar.width * 2)
    #carList[1].xpos = cmn.screen_rect.centerx
    nextCarStart = False
    while True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                    pyg.quit()
                    return
            elif event.type == pyg.KEYDOWN and event.key == pyg.K_q:
                pyg.quit()
                return

        disp.fill(cmn.windowFillColor)
        
        #newCar.draw()
        #Vehicle.draw()
        #newCar.draw()
        #newCar.moveDirLeft()
        
        carlistZ_rect = carList[0].draw()
        carList[0].moveDirLeft()
#        carlistZ_rect = carList[0].draw()
        
#        carlistZ_rect.left
        #newcar_rect = newCar.draw()
        #newcar_rect.left
        
        #print(f"carlistZ_rect.right is {carlistZ_rect.right}")
        
        
        #print(f"value of cmn.screen_rect.centerx, {cmn.screen_rect.centerx + 1}, is now equal to carList[0] xpos, {carList[0].xpos}")            
        #print(f"length of carList is {len(carList)}")
        #print(f"carList[0] xpos ture/false value is currently {bool(carList[1].xpos == cmn.screen_rect.centerx + 1) }")
        #print(f"value of cmn.screen_rect.centerx, {cmn.screen_rect.centerx - 1}, is now equal to carlistZ_rect.right + (cmn.cellWidth * 2), {carlistZ_rect.right + (cmn.cellWidth * 3)}")        
#        print(f"value of cmn.screen_rect.centerx, {cmn.screen_rect.centerx}, is now equal to carlistZ_rect.right + (cmn.cellWidth * 2), {carlistZ_rect.right + (cmn.cellWidth * 2)}")        

        #if carlistZ_rect.right + (cmn.cellWidth * 3) == (cmn.screen_rect.centerx - 1): # THIS ONE WORKS
        #print(f"value of carlistZ_rect.width // 2 is {carlistZ_rect.width // 2}")
        #if carlistZ_rect.right == cmn.screen_rect.right - carlistZ_rect.width : # this also works
        
        
        
#        if carlistZ_rect.right  == cmn.screen_rect.right - (cmn.cellWidth // 2) or \
#           carlistZ_rect.right - 1 == cmn.screen_rect.right - (cmn.cellWidth // 2) or \
#           carlistZ_rect.right - 2  == cmn.screen_rect.right - (cmn.cellWidth // 2) or \
#           carlistZ_rect.right - 3 == cmn.screen_rect.right - (cmn.cellWidth // 2):
#        if carlistZ_rect.left  == cmn.screen_rect.right - (cmn.cellWidth // 2) or \
#           carlistZ_rect.left - 1 == cmn.screen_rect.right - (cmn.cellWidth // 2) or \
#           carlistZ_rect.left - 2  == cmn.screen_rect.right - (cmn.cellWidth // 2) or \
#           carlistZ_rect.left - 3 == cmn.screen_rect.right - (cmn.cellWidth // 2):
        if  carlistZ_rect.left     == cmn.screen_rect.right - (cmn.cellWidth * 2)    or \
            carlistZ_rect.left - 1 == cmn.screen_rect.right - (cmn.cellWidth * 2)    or \
            carlistZ_rect.left - 2 == cmn.screen_rect.right - (cmn.cellWidth * 2)    or \
            carlistZ_rect.left - 3 == cmn.screen_rect.right - (cmn.cellWidth * 2):
            
            nextCarStart = True
#            print(f"value of cmn.screen_rect.centerx - 2, {cmn.screen_rect.centerx - 2}, is now equal to carlistZ_rect.right + (cmn.cellWidth * 2), {carlistZ_rect.right + (cmn.cellWidth * 2)}")        
#            print(f"value of cmn.screen_rect.centerx - 1, {cmn.screen_rect.centerx - 1}, is now equal to carlistZ_rect.right + cmn.cellWidth, {carlistZ_rect.right + cmn.cellWidth}")
            #newCar.rect.left = 100
#            print(f"value of cmn.screen_rect.centerx, {cmn.screen_rect.centerx}, is now equal to carlistZ_rect.right + (cmn.cellWidth * 2), {carlistZ_rect.right + (cmn.cellWidth * 3)}")        

            #print(f"value of carlistZ_rect.left, {carlistZ_rect.left}, (or -1 or -2 or -3) cmn.screen_rect.right - (cmn.cellWidth * 2) is now equal to  {cmn.screen_rect.right - (cmn.cellWidth * 2)}")
            
#        if nextCarStart == True:
#            carList[1].draw()
#            carList[1].moveDirLeft()
        
        if nextCarStart == True:
            for car in carList:
                if car.xpos + 1 == cmn.screen_rect.right - (cmn.cellWidth * 2):
                    car.draw()
                    car.moveDirLeft()
                    print(f"car xpos + 1 is {car.xpos + 1} and cmn.screen_rect.right - (cmn.cellWidth * 2) is {cmn.screen_rect.right - (cmn.cellWidth * 2)}")
                    
                    
                    











            #print(f"value of carList[1] xpos is, {carList[1].xpos}")
            

            
#            print(f"value of cmn.screen_rect.centerx + 1, {cmn.screen_rect.centerx + 1}, is now equal to carList[0] xpos, {carList[0].xpos}")    
#            secCar = newCar
#            carList.append[secCar]
#            carList[1].draw()
#            carList[1].moveDirLeft()
                #print(f"carList[1] xpos is now {carList[1].xpos}")
#            print(f"value of cmn.screen_rect.centerx, {cmn.screen_rect.centerx + 1}, is now equal to carlistZ_rect.right, {carlistZ_rect.right}")            
        
        #newCar.xpos = cmn.screen_rect.centerx

        froggie.update()
        froggie.draw()

        pyg.display.flip()        
        clock.tick(cmn.FPS)
        
        
        
        
if __name__ == '__main__':
    main()

#game()
