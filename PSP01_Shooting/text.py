import pygame
import math
import os

class Text:
    def __init__(self, *args):
        self.id = args[0]           # id
        
        self.xPos = args[1]         # 시작위치 X
        self.yPos = args[2]         # 시작위치 Y
        self.xEndPos = args[3]      # 종료위치 X
        self.yEndPos = args[4]      # 죵료위치 Y
        self.speed = args[5]        # 움직임 속도
        self.msg = args[6]          # 문자
        self.size = args[7]         # 폰트 크기
        self.color = args[8]        # 색
        self.alpha = args[9]        # 알파
        self.moving = args[10]       # 움직임 상태
        self.isAlive = False
        
        self.check_custom_font = False
        self.font = ""
        
    def __reset__(self, *args):
        self.xPos = args[0]         # 시작위치 X
        self.yPos = args[1]         # 시작위치 Y
        self.xEndPos = args[2]      # 종료위치 X
        self.yEndPos = args[3]      # 죵료위치 Y
        self.speed = args[4]        # 움직임 속도
        self.msg = args[5]          # 문자
        self.size = args[6]         # 폰트 크기
        self.color = args[7]        # 색
        self.alpha = args[8]        # 알파
        self.moving = args[9]       # 움직임 상태
        self.isAlive = False

    def SetFont(self, path):
        self.check_custom_font = True
        self.font = path


class TextManager:
    def __init__(self, *args):
        self.gamePad = args[0]
        self.padWidth = args[1]
        self.padHeight = args[2]
        # 관리 딕셔너리
        self.move_textList = {}
        self.alpha_textList = {}
        self.blink_textList = {}
        
        # blink
        self.blink_timer = pygame.time.get_ticks()
        self.blink_state = False
        
        self.fade = False
        self.fadeCount = 0

        self.fadeImage = pygame.Surface(self.gamePad.get_size())
        self.current_path = os.path.dirname(__file__)
        self.font_path = os.path.join(self.current_path, "font")
    
    # 텍스트 출력    
    def SetText(self, id, xPos, yPos, msg, fontSize, color = (255,255,255), alpha = 255):
        if self.move_textList.get(id) == None:
            self.move_textList[id] = Text(id, xPos, yPos, xPos, yPos, 0, msg, fontSize, color, alpha, False)
        else:
            self.move_textList[id].__reset__(xPos, yPos, xPos, yPos, 0, msg, fontSize, color, alpha, False)
            
        self.move_textList[id].isAlive = True
    
    #
    def SetTextBlink(self, id, xPos, yPos, msg, fontSize, color = (255,255,255), alpha = 0):
        if self.blink_textList.get(id) == None:
            self.blink_textList[id] = Text(id, xPos, yPos, xPos, yPos, 0, msg, fontSize, color, alpha, False)
        else:
            self.blink_textList[id].__reset__(xPos, yPos, xPos, yPos, 0, msg, fontSize, color, alpha, False)
            
        self.blink_textList[id].isAlive = True
    
    def SetTextAlpha(self, id, xPos, yPos, msg, fontSize, color = (255,255,255), alpha = 0):
        if self.alpha_textList.get(id) == None:
            self.alpha_textList[id] = Text(id, xPos, yPos, xPos, yPos, 0, msg, fontSize, color, alpha, False)
        else:
            self.alpha_textList[id].__reset__(xPos, yPos, xPos, yPos, 0, msg, fontSize, color, alpha, False)
            
        self.alpha_textList[id].isAlive = True

    def SetTextMove(self, id, startPosX, startPosY, endPosX, endPosY, msg, fontSize, speed = 3, color = (255,255,255), alpha = 255):
        if self.move_textList.get(id) == None:
            self.move_textList[id] = Text(id, startPosX, startPosY, endPosX, endPosY, speed, msg, fontSize, color, alpha, True) 
        else:
            self.move_textList[id].__reset__(startPosX, startPosY, endPosX, endPosY, speed, msg, fontSize, color, alpha, True)
            
        self.move_textList[id].isAlive = True
       
    def SetFont(self, id, font):
        if self.move_textList.get(id) != None:
            self.move_textList[id].SetFont(str(os.path.join(self.font_path,font)))
              
        if self.alpha_textList.get(id) != None:
            self.alpha_textList[id].SetFont(str(os.path.join(self.font_path,font)))
                  
        if self.blink_textList.get(id) != None:
            self.blink_textList[id].SetFont(str(os.path.join(self.font_path,font)))
        

    def Release(self):
        for key in self.move_textList:
            self.move_textList[key].isAlive = False
            
        for key in self.alpha_textList:
            self.alpha_textList[key].isAlive = False
            
        for key in self.blink_textList:
            self.blink_textList[key].isAlive = False 

    def OnExit(self, text_list):
        for id in text_list:
            if self.move_textList.get(id) != None:
                self.move_textList[id].isAlive = False
              
            if self.alpha_textList.get(id) != None:
                self.alpha_textList[id].isAlive = False
                  
            if self.blink_textList.get(id) != None:
                self.blink_textList[id].isAlive = False

    def OnEnter(self, text_list):
        for id in text_list:
            if self.move_textList.get(id) != None:
                self.move_textList[id].isAlive = True
              
            if self.alpha_textList.get(id) != None:
                self.alpha_textList[id].isAlive = True
                  
            if self.blink_textList.get(id) != None:
                self.blink_textList[id].isAlive = True
            
    def RenderText(self):
        for key in self.move_textList:
            if self.move_textList[key].isAlive == True:
                font = pygame.font.Font(self.move_textList[key].font ,self.move_textList[key].size) if self.move_textList[key].check_custom_font == True else pygame.font.SysFont('malgungothic',self.move_textList[key].size)

                text = font.render(self.move_textList[key].msg, True, self.move_textList[key].color)    
                
                if self.move_textList[key].moving == True:
                    rads = math.atan2(self.move_textList[key].yEndPos - self.move_textList[key].yPos, self.move_textList[key].xEndPos - self.move_textList[key].xPos)
                    
                    self.move_textList[key].xPos += (math.cos(rads) * self.move_textList[key].speed)
                    self.move_textList[key].yPos += (math.sin(rads) * self.move_textList[key].speed)
                    
                    self.gamePad.blit(text, (self.move_textList[key].xPos, self.move_textList[key].yPos))
                    
                    if \
                        self.move_textList[key].yPos <= (self.move_textList[key].yEndPos + (math.sin(rads) * self.move_textList[key].speed * 2)) and \
                        self.move_textList[key].yPos >= (self.move_textList[key].yEndPos - (math.sin(rads) * self.move_textList[key].speed * 2)) and \
                        self.move_textList[key].xPos <= (self.move_textList[key].xEndPos + (math.cos(rads) * self.move_textList[key].speed * 2)) and \
                        self.move_textList[key].xPos >= (self.move_textList[key].xEndPos - (math.cos(rads) * self.move_textList[key].speed * 2)):
                        self.move_textList[key].moving = False

                else:
                    self.gamePad.blit(text, (self.move_textList[key].xPos, self.move_textList[key].yPos))
                   
        for key in self.alpha_textList:
            if self.alpha_textList[key].isAlive == True:
                font = pygame.font.Font(self.alpha_textList[key].font ,self.alpha_textList[key].size) if self.alpha_textList[key].check_custom_font == True else pygame.font.SysFont('malgungothic',self.alpha_textList[key].size)

                text = font.render(self.alpha_textList[key].msg, True, self.alpha_textList[key].color)    
                
                if self.alpha_textList[key].alpha < 255:
                    self.alpha_textList[key].alpha += 5
               
                text.set_alpha(self.alpha_textList[key].alpha)
                                
                self.gamePad.blit(text, (self.alpha_textList[key].xPos, self.alpha_textList[key].yPos))
                    
        for key in self.blink_textList:
            if self.blink_textList[key].isAlive == True:    
                font = pygame.font.Font(self.blink_textList[key].font ,self.blink_textList[key].size) if self.blink_textList[key].check_custom_font == True else pygame.font.SysFont('malgungothic',self.blink_textList[key].size)

                text = font.render(self.blink_textList[key].msg, True, self.blink_textList[key].color)         
                
                if (pygame.time.get_ticks() - self.blink_timer) / 1000 > 0.5:
                    if self.blink_state == True:
                        self.blink_state = False
                    else:
                        self.blink_state = True
                    
                    self.blink_timer = pygame.time.get_ticks()
                    
                if self.blink_state == True:
                    self.gamePad.blit(text, (self.blink_textList[key].xPos, self.blink_textList[key].yPos))
        
        if self.fade == True:
            if self.fadeCount < 255:
                self.fadeCount += 5
        else:
            if self.fadeCount > 0:
                self.fadeCount -= 5
        
        self.fadeImage.set_alpha(self.fadeCount)
        self.fadeImage.fill((0,0,0))
        self.gamePad.blit(self.fadeImage,(0,0))



    
        
    