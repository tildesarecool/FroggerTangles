from common import Common

from abc import ABC, abstractmethod
import pygame as pyg

cmn = Common()
disp = cmn.dsp

class GameRect(ABC):
    '''A very generic shape Rectangle'''
    
    def __init__(self, xpos: int, ypos: int, width: int, height: int, color: list) -> None:
        self.xpos = xpos 
        self.ypos = ypos
        self.width = width
        self.height = height
        self.color = color
    
    def draw_rect(self):
        rect = pyg.Rect(self.xpos, self.ypos, self.width, self.height)
        pyg.draw.rect(disp, self.color, rect)
        
        return rect
    
    @abstractmethod
    def draw(self):
        pass
        
