import math
import pygame

class Actor:
    def __init__(self, *args):
        self.id = args[0]           # ID
        self.shape = args[1]        # 모양
        self.hp = args[2]           # 체력
        self.power = args[3]        # 파워
        self.speed = args[4]        # 스피드
        self.shotDelay = args[5]    # 총알 딜레이
        # 초기화
        self.xPos = 1.0     # X좌표
        self.yPos = 1.0     # Y좌표
        self.angle = 0.0    # 움직임 각도
        
        self.width = self.shape.get_rect().size[0]      # 가로 크기
        self.height = self.shape.get_rect().size[1]     # 세로 크기
        
        self.aliveTimer = pygame.time.get_ticks()       # 살아 있는 시간
        self.shotTimer = pygame.time.get_ticks()        # 총알 딜레이 시간
        self.damageTimer = pygame.time.get_ticks()      # 데미지 딜레이시간
        
        self.moveTimer = pygame.time.get_ticks()
        
        self.startPosX = 0
        self.startPosY = 0
       
        self.tag = "None"
       
        self.isAlive = False
        
        self.currentHp = self.hp
        
        self.pattern = 0
        self.invincibility = False
        

    def ChangeShotDelay(self, delay):
        self.shotDelay = delay

    def ShotDelay(self):
        
        if self.isAlive == True:
            if (pygame.time.get_ticks() - self.shotTimer) /1000 > self.shotDelay:
                self.shotTimer = pygame.time.get_ticks()
                return True
        
        return False
    
    def ChangeScale(self, width, height):
        self.shape = pygame.transform.scale(self.shape,(width, height))
        self.width = width
        self.height = height
        
    def ChangeRotation(self, renderAngle):
        self.shape = pygame.transform.rotate(self.shape, renderAngle)
    
    def MoveSpawn(self, xPos, yPos, speed, angle, tag):
        self.xPos = xPos
        self.yPos = yPos
        self.speed = speed
        self.angle = angle
        self.tag = tag
        
        self.currentHp = self.hp
        self.pattern = 0
        self.isAlive = True
    
    def AppearSpawn(self, xPos, yPos, tag):
        self.xPos = xPos
        self.yPos = yPos
        self.speed = 0
        self.tag = tag
        
        self.currentHp = self.hp
        self.pattern = 0
        self.isAlive = True

    def MoveDestination(self, xPos, yPos, play_timer):
        
        timer = (pygame.time.get_ticks() - self.moveTimer) / 1000
        
        if timer > play_timer - 0.02:
            self.moveTimer = pygame.time.get_ticks()
        else:
            targetVec = pygame.Vector2(xPos, yPos)
            playerVec = pygame.Vector2(self.startPosX, self.startPosY)
            
            resultVec = pygame.Vector2.lerp(playerVec,targetVec, timer/play_timer)
            
            self.xPos = resultVec.x
            self.yPos = resultVec.y
            
            if timer/play_timer >= 0.98:
                self.moveTimer = pygame.time.get_ticks()
                self.startPosX = self.xPos
                self.startPosY = self.yPos
                return True
                
        return False
    
    def Move(self):
        if self.isAlive == True:
            if self.pattern == 0:
                rads = math.radians(self.angle)
                
                self.xPos += (math.cos(rads) * self.speed)
                self.yPos += (math.sin(rads) * self.speed)
                
        if self.xPos < -300 or \
            self.xPos > 680 or \
            self.yPos < -300 or \
            self.yPos > 840:
                self.isAlive = False
         
    def Hit(self, damage):
        
        self.currentHp -= damage
        
        if self.currentHp < 0:
            self.isAlive = False
            return True
        
        return False    
        
    
    
class Enemy(Actor):
    def __init__(self, *args):
        super().__init__(*args)
        
        self.tag = "Enemy"
        
class Player(Actor):
    def __init__(self, *args):
        super().__init__(*args)
        self.profile = args[6]
        self.initLife = args[7]
        self.initBomber = args[8]
        self.shieldAlive = False
        
        self.tag = "Player"
       
    def SetShield(self, state):
        self.shieldAlive = state
        
    
        
class Boss(Actor):
    def __init__(self, *args):
        super().__init__(*args)
        
        self.tag = "Boss"