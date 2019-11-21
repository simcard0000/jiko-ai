import os
import re
import pygame
from PIL import Image

#How to use this class
#Put the animation frames in a folder, and give that folderpath to the gifImage object
#You can set the size, placement, and how many frames you want each picture to be!
#The game is currently set to 60 fps.

class gifImage(object):

    def __init__(self, folderPath, x=0, y=0, frameCycleLen = 1):
        self.folderPath = folderPath
        self.imgNames = []
        self.images = []
        self.x = x
        self.y = y
        self.center = (self.x, self.y)
        self.frameNum = 0
        self.frameCycleLen = frameCycleLen
        self.frameCycleCount = 1
        self.getFrames()

    def setCoords(x, y):
        self.x = x  
        self.y = y

    def frameCycleLen(cycleLen):
        self.frameCycleLen = cycleLen

    def getFrames(self):
        self.imgNames = os.listdir(self.folderPath)
        self.imgNames = self.naturalSort(self.imgNames)
        for i in range(len(self.imgNames)):
            self.images.append(pygame.image.load(self.folderPath + "/" + self.imgNames[i]))

    def resize(self, width, height):
        for i in range(len(self.images)):
            self.images[i] = pygame.transform.scale(self.images[i], (width, height))

    def animate(self, screen):
        screen.blit(self.images[self.frameNum], (self.x, self.y))

        if self.frameCycleCount >= self.frameCycleLen: 
            self.frameNum = self.frameNum + 1
            self.frameCycleCount = 1

        if self.frameNum >= len(self.images):
            self.frameNum = 0
        
        self.frameCycleCount = self.frameCycleCount + 1

    def naturalSort(self, l): 
        convert = lambda text: int(text) if text.isdigit() else text.lower() 
        alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
        return sorted(l, key = alphanum_key)
