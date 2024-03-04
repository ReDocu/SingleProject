import math
import pygame

class Bullet:
    def __init__(self, *args):
        self.id = args[0]       # 총알 ID
        self.shape = args[1]    # 총알 형태
        self.power = args[2]    # 총알 공격력
        
        self.xPos = 0.0                             # x 좌표
        self.yPos = 0.0                             # y 좌표
        self.width = self.shape.get_rect().size[0]    # 가로 크기
        self.height = self.shape.get_rect().size[1]   # 세로 크기
        
        self.angle = 180
        self.speed = 0
        
        self.rotateShape = self.shape
        
        self.tag = "None"
        
        self.pattern = 0
        
        self.startPosX = 0
        self.startPosY = 0
        self.targetPosX = 0
        self.targetPosY = 0
        
        self.isAlive = False
    
    def ChangeSpeed(self, speed):
        self.speed = speed
        
    def AngleFire(self, xPos, yPos, speed, angle, tag):
        self.xPos = xPos
        self.yPos = yPos
        self.speed = speed
        self.angle = angle
        self.tag = tag
        
        self.pattern = 0
        self.isAlive = True
        
    def TargetFire(self, xPos, yPos, targetPosX, targetPosY, tag, speed):
        
        self.xPos = xPos
        self.yPos = yPos
        self.startPosX = xPos
        self.startPosY = yPos
        self.targetPosX = targetPosX
        self.targetPosY = targetPosY
        self.tag = tag
        self.speed = speed
        
        self.pattern = 1
        self.isAlive = True
        
        return math.atan2(self.targetPosY - self.startPosY,self.targetPosX - self.startPosX)

    
    def ChangeScale(self, width, height):
        self.shape = pygame.transform.scale(self.shape,(width, height))
        self.width = width
        self.height = height
        
    def ChangeRotation(self, renderAngle):
        self.rotateShape = pygame.transform.rotate(self.shape, renderAngle)
        self.width = self.rotateShape.get_rect().size[0]
        self.height = self.rotateShape.get_rect().size[1]
        
    def CollisionEnemy(self, target):
        
        if self.isAlive == False:
            return False
        
        if target.isAlive == False:
            return False
        
        pointX = self.xPos + self.width/2
        pointY = self.yPos + self.height/2    
    
        if target.xPos < pointX and pointX < target.xPos + target.width:
            if target.yPos < pointY and pointY < target.yPos + target.height:
                if self.tag == "Player" and target.tag == "Enemy":
                    return True
        return False
    
    def CollisionPlayer(self, target):
        if self.isAlive == False:
            return False
        
        if target.isAlive == False:
            return False
        
        pointX = self.xPos + self.width/2
        pointY = self.yPos + self.height/2    
    
        if target.xPos < pointX and pointX < target.xPos + target.width:
            if target.yPos < pointY and pointY < target.yPos + target.height:
                if self.tag == "Enemy" and target.tag == "Player":
                    return True
        return False
        
    def Move(self):
        
        if self.isAlive == True:
            if self.pattern == 0:
                rads = math.radians(self.angle)
                
                self.xPos += (math.cos(rads) * self.speed)
                self.yPos += (math.sin(rads) * self.speed)
        
            if self.pattern == 1:
                rads = math.atan2(self.targetPosY - self.startPosY,self.targetPosX - self.startPosX)

                self.xPos += (math.cos(rads) * self.speed)
                self.yPos += (math.sin(rads) * self.speed)

        if self.xPos < -100 or \
            self.xPos > 580 or \
            self.yPos < -100 or \
            self.yPos > 740:
                self.isAlive = False
        
        