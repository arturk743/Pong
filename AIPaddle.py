# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:31:56 2019

@author: Artur
"""

import pygame
from pygame.locals import *

class AIPaddle(object): # AI's paddle object
    def __init__(self, screensize):
        self.screensize = screensize
        
        self.centerx = screensize[0] - 5
        self.centery=int(screensize[1]*0.5)
        
        self.height = 100
        self.withdt = 10
        
        self.rect = pygame.Rect(0,self.centery - int(self.height*0.5), self.withdt, self.height)
        self.color = (255,100,100)
        
        self.direction = 0; 
        
        self.speed = 10 # how fast AI will be react
        
    def update(self, pong): # update paddle position on screen
        if pong.rect.top < self.rect.top:
            self.centery -= self.speed
        elif pong.rect.bottom > self.rect.bottom:
            self.centery += self.speed
            
        self.rect.center = (self.centerx, self.centery)
        
    def render(self,screen): # draw paddle position on screen
        pygame.draw.rect(screen,self.color, self.rect ,0)
        pygame.draw.rect(screen,(0,0,0), self.rect ,1)