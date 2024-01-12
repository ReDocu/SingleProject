### Main 
import pygame
import sys
import os

# 프로그램 세팅
WindowName = '프로그램'
WindowWidth = 480
WindowHeight = 640

# 윈도우 헨들러
# global : surface 로 사용

static_frame = 30



def GameSetting():
    global surface

    pygame.init()
    surface = pygame.display.set_mode((WindowWidth,WindowHeight))
    pygame.display.set_caption(WindowName)
    

def runGame():
    global surface

    onGame = False
    while not onGame:
        event = pygame.event.pool()

        





if __name__ == '__main__':
    GameSetting()