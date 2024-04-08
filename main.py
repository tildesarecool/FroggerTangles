# 7 April 2024 
# This is something of a reboot of the script I've been working on for weeks now
# It was getting to large and unwieldly but I couldn't bring myself to start deleting things wholesale
# so I made a copy of all the files then delete some extra files and finally cleaned up the code and deleted 
# old comments I wanted to keep but also didn't need any more. 
# 
# 



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
    vehicTracker = 0
    NumberOfCars = len(carList) 
    #print(f"value of NumberOfCars is {NumberOfCars}")
#    def findxpos() -> int:
#        if carList[vehic].xpos     == cmn.screen_rect.right - (cmn.cellWidth * 2):
#            num = 0
#        elif carList[vehic].xpos - 1 == cmn.screen_rect.right - (cmn.cellWidth * 2):
#            num =  1
#        elif carList[vehic].xpos - 2 == cmn.screen_rect.right - (cmn.cellWidth * 2):
#            num =  2
#        elif carList[vehic].xpos - 3 == cmn.screen_rect.right - (cmn.cellWidth * 2):
#            num =  3
#        else:
#            return False
        
 #       print(f"value of num is {int(num)}")
 #       return int(num)
    
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



        for vehic in range(NumberOfCars):
#            print(f"value of vehic is {vehic}")
#        for car in carList:
            carList[vehic].moveDirLeft()
            #print(f"value of carList[vehic].xpos is {carList[vehic].xpos} and value of cmn.screen_rect.right - (cmn.cellWidth * 2) is {cmn.screen_rect.right - (cmn.cellWidth * 2)}  ")
            
            if  carList[vehic].xpos - vehicTracker == cmn.screen_rect.right - (cmn.cellWidth * 2):
                vehicTracker = 0
                nextCarStart = True
            elif carList[vehic].xpos - 1 == cmn.screen_rect.right - (cmn.cellWidth * 2) :
                vehicTracker = 1
                nextCarStart = True
            elif carList[vehic].xpos - 2 == cmn.screen_rect.right - (cmn.cellWidth * 2) :
                vehicTracker = 2
                nextCarStart = True
            elif carList[vehic].xpos - 3 == cmn.screen_rect.right - (cmn.cellWidth * 2):
                vehicTracker = 3
                nextCarStart = True
            if nextCarStart:
                if vehic <= 2: # > 0 and vehic <= 3:
                    #print(f"bool(carList[vehic].draw()) evaluates to {bool(carList[vehic].draw())} for vehic number {vehic}")
                    print(f"carList[vehic].xpos evaluates to {carList[vehic].xpos - 2} and cmn.screen_rect.right - (cmn.cellWidth * 2) is {cmn.screen_rect.right - (cmn.cellWidth * 2)} for vehic number {vehic}")
                    if carList[vehic].xpos - vehicTracker == cmn.screen_rect.right - (cmn.cellWidth * 2): # and carList[vehic].xpos != carList[vehic - 1].xpos:
                        #if vehic == 0:
                        if vehic + 1 < NumberOfCars:
                            carList[vehic + 1].xpos = carList[vehic].xpos + cmn.cellWidth * 3
                            print(f"bool(carList[vehic].draw()) evaluates to {bool(carList[vehic].draw())} for vehic number {vehic}")
                            nextCarStart = False
                            #if not bool(carList[vehic].draw()):
                            #
                            #    print(f"value of carList[vehic].xpos + 1 - {carList[vehic].xpos + 1} == cmn.screen_rect.right - (cmn.cellWidth * 2) - {cmn.screen_rect.right - (cmn.cellWidth * 2) } - has been found true")
#
                            #    print(f"Currently on vehic {vehic}")
                            
                            #carlistZ_rect = carList[vehic].draw() #carList[vehic].draw()
                            #carList[vehic].draw()
                        #carList[vehic].moveDirLeft()
                
                        
#                            car.draw()
                    #car.moveDirLeft()
                    #carlistZ_rect.x = car.xpos
#                           nextCarStart = False

#            if  carlistZ_rect.left     == cmn.screen_rect.right - (cmn.cellWidth * 2)    or \
#                carlistZ_rect.left - 1 == cmn.screen_rect.right - (cmn.cellWidth * 2)    or \
#                carlistZ_rect.left - 2 == cmn.screen_rect.right - (cmn.cellWidth * 2)    or \
#                carlistZ_rect.left - 3 == cmn.screen_rect.right - (cmn.cellWidth * 2):                
                
                    #print(f"One of the carlistZ_rect.left == cmn.screen_rect.right - (cmn.cellWidth * 2) values found true ")
                    
#                print(f"Currently on vehic {vehic}")
                
#                nextCarStart = True
#                if nextCarStart == True:
                #if vehic < NumberOfCars:
##############################################################                
#        carlistZ_rect = carList[0].draw()
#        carList[0].moveDirLeft()
#        if  carlistZ_rect.left     == cmn.screen_rect.right - (cmn.cellWidth * 2)    or \
#            carlistZ_rect.left - 1 == cmn.screen_rect.right - (cmn.cellWidth * 2)    or \
#            carlistZ_rect.left - 2 == cmn.screen_rect.right - (cmn.cellWidth * 2)    or \
#            carlistZ_rect.left - 3 == cmn.screen_rect.right - (cmn.cellWidth * 2):
#            
#            nextCarStart = True
#
##        if nextCarStart == True:
##            carList[1].draw()
##            carList[1].moveDirLeft()        
#
#        if nextCarStart == True:
#            for car in carList:
#                if car.xpos + 1 == cmn.screen_rect.right - (cmn.cellWidth * 2):
#                    car.draw()
#                    car.moveDirLeft()
#                    print(f"car xpos + 1 is {car.xpos + 1} and cmn.screen_rect.right - (cmn.cellWidth * 2) is {cmn.screen_rect.right - (cmn.cellWidth * 2)}")
#
#
##############################################################



        froggie.update()
        froggie.draw()

        pyg.display.flip()        
        clock.tick(cmn.FPS)
        
        
if __name__ == '__main__':
    main()

#game()


#            if  carlistZ_rect.left     == cmn.screen_rect.right - (cmn.cellWidth * 2)    or \
#                carlistZ_rect.left - 1 == cmn.screen_rect.right - (cmn.cellWidth * 2)    or \
#                carlistZ_rect.left - 2 == cmn.screen_rect.right - (cmn.cellWidth * 2)    or \
#                carlistZ_rect.left - 3 == cmn.screen_rect.right - (cmn.cellWidth * 2):                

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

#            print(f"value of cmn.screen_rect.centerx - 2, {cmn.screen_rect.centerx - 2}, is now equal to carlistZ_rect.right + (cmn.cellWidth * 2), {carlistZ_rect.right + (cmn.cellWidth * 2)}")        
#            print(f"value of cmn.screen_rect.centerx - 1, {cmn.screen_rect.centerx - 1}, is now equal to carlistZ_rect.right + cmn.cellWidth, {carlistZ_rect.right + cmn.cellWidth}")
            #newCar.rect.left = 100
#            print(f"value of cmn.screen_rect.centerx, {cmn.screen_rect.centerx}, is now equal to carlistZ_rect.right + (cmn.cellWidth * 2), {carlistZ_rect.right + (cmn.cellWidth * 3)}")        

            #print(f"value of carlistZ_rect.left, {carlistZ_rect.left}, (or -1 or -2 or -3) cmn.screen_rect.right - (cmn.cellWidth * 2) is now equal to  {cmn.screen_rect.right - (cmn.cellWidth * 2)}")
            

#print(f"value of carList[1] xpos is, {carList[1].xpos}")
            

            
#            print(f"value of cmn.screen_rect.centerx + 1, {cmn.screen_rect.centerx + 1}, is now equal to carList[0] xpos, {carList[0].xpos}")    
#            secCar = newCar
#            carList.append[secCar]
#            carList[1].draw()
#            carList[1].moveDirLeft()
#print(f"carList[1] xpos is now {carList[1].xpos}")
#            print(f"value of cmn.screen_rect.centerx, {cmn.screen_rect.centerx + 1}, is now equal to carlistZ_rect.right, {carlistZ_rect.right}")            
        
#newCar.xpos = cmn.screen_rect.centerx