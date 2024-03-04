import pygame
import actor
import bullet

class Pool:
    def __init__(self, *args):
        
        self.pool = []              # 담아놀 객체 데이터
        self.objParent = args[0]    # 원본
        
        self.spawnDelay = {}
    
    def MakeActor(self):
        pass
    
    
    # 복제 타이밍에 딜레이 주기
    def SpawnDelay(self, delayTime):
        
        if self.spawnDelay.get(delayTime) == None:
            self.spawnDelay[delayTime] = pygame.time.get_ticks()
        else:
            if (pygame.time.get_ticks() - self.spawnDelay[delayTime]) / 1000 > delayTime:
                self.spawnDelay[delayTime] = pygame.time.get_ticks()
                return True
        return False
    
    # 원본 복제하기
    def SpawnObj(self):
        newActor = self.pool[0]
        check = False
        
        for obj in self.pool:
            if obj.isAlive == False:
                check = True
                newActor = obj
                break
        
        if check == False:
            newActor = self.MakeActor()
            self.pool.append(newActor)
        
        return newActor
    
    # 복제된 모든 데이터 죽이기
    def AllDead(self):
        for obj in self.pool:
            obj.isAlive = False
    
class enemyPool(Pool):
    def __init__(self, *args): 
        super().__init__(*args)
        
        newActor = actor.Enemy(self.objParent.id, self.objParent.shape, self.objParent.hp, self.objParent.power, self.objParent.speed, self.objParent.shotDelay)
        self.pool.append(newActor)
        
    def MakeActor(self):
        return actor.Enemy(self.objParent.id, self.objParent.shape, self.objParent.hp, self.objParent.power, self.objParent.speed, self.objParent.shotDelay)
        
class bulletPool(Pool):
    def __init__(self, *args):
        super().__init__(*args)
        
        newActor = bullet.Bullet(self.objParent.id, self.objParent.shape, self.objParent.power)
        self.pool.append(newActor)
    
    def MakeActor(self):
        return bullet.Bullet(self.objParent.id, self.objParent.shape, self.objParent.power)
        
class bossPool(Pool):
    def __init__(self, *args):
        super().__init__(*args)
        
        newActor = actor.Boss(self.objParent.id, self.objParent.shape, self.objParent.hp, self.objParent.power, self.objParent.speed, self.objParent.shotDelay)
        self.pool.append(newActor)
        
    def MakeActor(self):
        return actor.Boss(self.objParent.id, self.objParent.shape, self.objParent.hp, self.objParent.power, self.objParent.speed, self.objParent.shotDelay)
    
    
class effectPool(Pool):
    def __init__(self, *args):
        super().__init__(*args)
        