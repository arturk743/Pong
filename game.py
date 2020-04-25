# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:30:28 2019

@author: Artur
"""
import pygame
import time
from Pong import Pong
from PlayerPaddle import PlayerPaddle
from AIPaddle import AIPaddle
from pygame.locals import *

SPEEDX = 1
SPEEDY = 3
running  = True
pause = False
points = [0,0]
screensize=None
def event_check(type_of_game, pong, player1_paddle, player2_paddle = None): # reaction to palyers behavoiur 
    global pause
    global running
    global SPEEDX
    global SPEEDY
    global points
    global screensize
    for event in pygame.event.get(): #collection of possible player's behavoiurs(mouse, keyboard)
            if event.type == QUIT: #quit the game
                running = False
            if event.type == KEYDOWN: # key press
                if event.key == K_UP:
                    player1_paddle.direction = -1
                elif event.key == K_DOWN:
                    player1_paddle.direction = 1
                elif event.key == K_0:
                    pong.speedx = SPEEDX
                    pong.speedy = SPEEDY
                elif event.key == K_1:
                    pong.speedx = SPEEDX + 1
                    pong.speedy = SPEEDY + 1
                elif event.key == K_2:
                    pong.speedx = SPEEDX + 2
                    pong.speedy = SPEEDY + 2
                elif event.key == K_3:
                    pong.speedx = SPEEDX + 3
                    pong.speedy = SPEEDY + 3
                elif event.key == K_4:
                    pong.speedx = SPEEDX + 4
                    pong.speedy = SPEEDY + 4
                elif event.key == K_5:
                    pong.speedx = SPEEDX + 5
                    pong.speedy = SPEEDY + 5
                elif event.key == K_6:
                    pong.speedx = SPEEDX + 6
                    pong.speedy = SPEEDY + 6
                elif event.key == K_7:
                    pong.speedx = SPEEDX + 7
                    pong.speedy = SPEEDY + 7
                elif event.key == K_8:
                    pong.speedx = SPEEDX + 8
                    pong.speedy = SPEEDY + 8
                elif event.key == K_9:
                    pong.speedx = SPEEDX + 9
                    pong.speedy = SPEEDY + 9
            if event.type == KEYUP: # key press and release 
                if event.key == K_UP and player1_paddle.direction == -1:
                    player1_paddle.direction = 0
                elif event.key == K_DOWN and player1_paddle.direction == 1:
                    player1_paddle.direction = 0
                elif event.key == K_p: # pause
                    pause = True
                elif event.key == K_r: # reset
                    pong = Pong(screensize)
                    points = [0,0]
            if event.type == MOUSEMOTION: # mouse movement
                mouse_position = pygame.mouse.get_rel()
                if abs(mouse_position[1]) < 1: # eliminate small movement
                    pass
                else:
                    if player2_paddle.rect.top == 0 and mouse_position[1] < 0:
                        player2_paddle.direction = 0
                    elif player2_paddle.rect.bottom == player2_paddle.screensize[1]-1 and mouse_position[1] > 0:
                        player2_paddle.direction = 0
                    elif mouse_position[1] < 0:
                        player2_paddle.direction = -1
                    elif mouse_position[1] > 0:
                        player2_paddle.direction = 1
                    else:
                        player2_paddle.direction = 0
                    print(mouse_position)



def game():
    global running
    global pause
    global points
    global pong
    global screensize
    white = (255, 255, 255) 
    green = (0, 255, 0) 
    blue = (0, 0, 128) 
    grey = (100,100,100)
    # load data from conf file
    plik = open('conf.txt','r') 
    type_of_game = plik.readline()
    type_of_game = int(type_of_game[type_of_game.find('-')+1:])
    way_of_playing = plik.readline()
    way_of_playing = int(way_of_playing[way_of_playing.find('-')+1:])
    speed_of_player_paddle = plik.readline()
    speed_of_player_paddle = int(speed_of_player_paddle[speed_of_player_paddle.find('-')+1:])
    screensize = plik.readline()
    screensize = (screensize[screensize.find('-')+1:].rstrip()).split('x')
    screensize = tuple(map(int,screensize))
    difficulty_level = plik.readline()
    difficulty_level = int(difficulty_level[difficulty_level.find('-')+1:])
    print(way_of_playing);
    pygame.init()    
    
    screen = pygame.display.set_mode(screensize) #create screen with given dimension
    
        
    clock = pygame.time.Clock() # limit and track fps
        
    pong = Pong(screensize)
    
    if type_of_game == 1: 
        player1_paddle = PlayerPaddle(screensize,1)
        player1_paddle.speed = speed_of_player_paddle
        player2_paddle = PlayerPaddle(screensize,2)
        player2_paddle.speed = speed_of_player_paddle
    elif type_of_game == 2:
        if way_of_playing == 2: # player use mouse
            player1_paddle = AIPaddle(screensize)
            player1_paddle.speed = difficulty_level
            player2_paddle = PlayerPaddle(screensize)
            player2_paddle.speed = speed_of_player_paddle
        else: # player use keyboard
            player1_paddle = PlayerPaddle(screensize)
            player1_paddle.speed = speed_of_player_paddle
            player2_paddle = AIPaddle(screensize)
            player2_paddle.speed = difficulty_level
        
    while running:
        clock.tick(64) # limit fps to 64
            
        event_check(type_of_game, pong, player1_paddle, player2_paddle)
            
        while pause: # pause game until player presses p
            clock.tick(64)
            for event in pygame.event.get(): 
                if event.type == KEYUP:
                    if event.key == K_p:
                        pause = False
        
        #update position of ball and paddles    
        player1_paddle.update(pong)
        player2_paddle.update(pong)
        if type_of_game == 2 and way_of_playing == 2:
            pong.update(player2_paddle,player1_paddle) 
        else:
            pong.update(player1_paddle,player2_paddle) 
    
        screen.fill(grey) 
        #countig points
        if pong.hit_edge_right: 
            pong = Pong(screensize)
            points[0] += 1
        elif pong.hit_edge_left:
            pong = Pong(screensize)
            points[1] += 1
            
        if points[0] == 3: # display how win if any player reach 3 points
            font = pygame.font.Font('freesansbold.ttf', 64)
            text = font.render('Player 1 Won', True, green, grey)
            textRect = text.get_rect() 
            textRect.center = (screensize[0] // 2, screensize[1] // 2) 
            screen.blit(text, textRect)
            pygame.display.flip()
            clock.tick(0.5)
            running = False
        elif points[1] ==3:
            font = pygame.font.Font('freesansbold.ttf', 64)
            if type_of_game == 1:
                text = font.render('Player 2 Won', True, green, grey)
            else:
                text = font.render('AI Won', True, green, grey)
            textRect = text.get_rect() 
            textRect.center = (screensize[0] // 2, screensize[1] // 2) 
            screen.blit(text, textRect)
            pygame.display.flip()
            clock.tick(0.5)
            running = False
        else:# render new posiotion of ball and paddles
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render('Player 1 : {}     Player 2 : {}'.format(*points), True, white, grey)
            textRect = text.get_rect() 
            textRect.center = (screensize[0] // 2, 16) 
            screen.blit(text, textRect)
            
            pong.render(screen)  
            player1_paddle.render(screen)
            player2_paddle.render(screen)
            pygame.display.flip()
        
    pygame.quit()
        
if __name__ == "__main__":
    game()
    
