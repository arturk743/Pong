# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:32:13 2019

@author: Artur
"""
import pygame
from pygame.locals import *

class PlayerPaddle(object):  # palyer's paddle object
    def __init__(self, screensize, side = 1): #side = 1 : left side; side = 2 : right side
        self.side = side
        self.screensize = screensize
        if side == 2: 
            self.centerx =screensize[0] - 5
        else:
            self.centerx =5
        self.centery=int(screensize[1]*0.5)
        
        self.height = 100
        self.withdt = 10
        
        self.rect = pygame.Rect(0,self.centery - int(self.height*0.5), self.withdt, self.height)
        self.color = (100,255,100)
        
        self.speed = 4 # how fast player paddle can move
        self.direction = 0
        
    def update(self, *arg): # update paddle position on screen
        self.centery += self.direction*self.speed
        
        self.rect.center = (self.centerx, self.centery)
        
        if self.rect.top < 0:
            self.rect.top =0
        if self.rect.bottom > self.screensize[1]-1:
            self.rect.bottom = self.screensize[1]-1
        
    def render(self,screen): # draw paddle position on screen
        pygame.draw.rect(screen,self.color, self.rect ,0)
        pygame.draw.rect(screen,(0,0,0), self.rect ,1)