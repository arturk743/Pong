# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:31:34 2019

@author: Artur
"""

import pygame
from pygame.locals import *

SPEEDX = 1
SPEEDY = 3

class Pong(object): # ball object
    def __init__(self, screensize):

        self.screensize = screensize

        self.centerx = int(screensize[0]*0.5)
        self.centery = int(screensize[1]*0.5)

        self.radius = 8

        self.rect = pygame.Rect(self.centerx-self.radius,
                                self.centery-self.radius,
                                self.radius*2, self.radius*2)

        self.color = (100,100,255)

        self.direction = [1,1] # first coordinate: 1 - right, -1 - left; second coordinate : 1 - down, -1 - up

        self.speedx = SPEEDX
        self.speedy = SPEEDY

        self.hit_edge_left = False
        self.hit_edge_right = False

    def update(self, player1_paddle = None, player2_paddle= None): # update ball position on screen

        self.centerx += self.direction[0]*self.speedx
        self.centery += self.direction[1]*self.speedy

        self.rect.center = (self.centerx, self.centery)

        if self.rect.top <= 0:
            self.direction[1] = 1
        elif self.rect.bottom >= self.screensize[1]-1:
            self.direction[1] = -1
        # check if ball hit left or right wall
        if self.rect.right >= self.screensize[0]-1:
            self.hit_edge_right = True
        elif self.rect.left <= 0:
            self.hit_edge_left = True
        # check if ball hit any paddle  
        if self.rect.colliderect(player2_paddle.rect):
            self.direction[0] = -1
            if self.centery < player2_paddle.centery:#ball physics
                self.direction[1] = -1
            elif self.centery > player2_paddle.centery:
                self.direction[1] = 1
            else:
                self.direction[1] = 0
                
        if self.rect.colliderect(player1_paddle.rect):
            self.direction[0] = 1
            if self.centery < player1_paddle.centery:#ball physics
                self.direction[1] = -1
            elif self.centery > player1_paddle.centery:
                self.direction[1] = 1
            else:
                self.direction[1] = 0

    def render(self, screen): # draw ball position on screen
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius, 0)
        pygame.draw.circle(screen, (0,0,0), self.rect.center, self.radius, 1)