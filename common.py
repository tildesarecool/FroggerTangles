import pygame as pyg
#from lanes import Lane
pyg.init()

# Initialize pygame and create the display surface
#mainLane = Lane()

class Common():
    '''Command variables and settings'''
    def __init__(self):
        
        self.BLACK: str = '#000000'
        self.SILVER: str = '#C0C0C0'
        self.BLACK: str = '#000000'
        self.GREY: str = '#808080'
        self.GREEN: str = '#008000'
        self.LITEBLUE: str = '#6FC3C1'
        self.LIME: str = '#00FF00'
        self.WHITE: str = '#FFFFFF'
        self.BLUEISH: str = (10, 150, 240)
        self.AQUA: str = '#00FFFF'
        
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        
        self.cellWidth = 50
        self.cellHeight = 50
        
        self.CENTER_X = self.SCREEN_WIDTH // 2
        self.CENTER_Y = self.SCREEN_HEIGHT // 2
        
        self.vehicleHeight = self.cellHeight * 1.5
        
        self.screen_rect = self.screenInfo().get_rect()

    def screenInfo(self):
        self.dsp = pyg.display.set_mode(
                (
                    self.SCREEN_WIDTH, 
                    self.SCREEN_HEIGHT
                )
            )
        return self.dsp
    
