import pygame as pyg
#from lanes import Lane
pyg.init()


# Initialize pygame and create the display surface
#mainLane = Lane()

class Common():
    '''Command variables and settings'''
    def __init__(self):

        self.FPS = 60
        
        self.BLACK: str = '#000000'
        self.SILVER: str = '#C0C0C0'
        self.GREY: str = '#808080'
        self.GREEN: str = '#008000'
        self.LITEBLUE: str = '#6FC3C1'
        self.LIME: str = '#00FF00'
        self.WHITE: str = '#FFFFFF'
        self.BLUEISH: str = (10, 150, 240)
        self.AQUA: str = '#00FFFF'
        
        self.windowFillColor = self.BLUEISH
        
        self.colorList = [
            self.BLACK, 
            self.SILVER, 
            self.GREY, 
            self.GREEN, 
            self.LITEBLUE,
            self.LIME,
            self.WHITE,
            self.BLUEISH,
            self.AQUA,
        ]
        
        self.SCREEN_WIDTH = 320 * 3
        self.SCREEN_HEIGHT = 240 * 3
        
        self.cellWidth = 50
        self.cellHeight = 50
        
        self.CENTER_X = self.SCREEN_WIDTH // 2
        self.CENTER_Y = self.SCREEN_HEIGHT // 2
        
        self.vehicleHeight = self.cellHeight # this was working as 1.5

        self.dsp = pyg.display.set_mode(
                (
                    self.SCREEN_WIDTH, 
                    self.SCREEN_HEIGHT
                )
            )
        
        self.screen_rect = self.dsp.get_rect()

