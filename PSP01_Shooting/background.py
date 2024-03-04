# 대각선은 현재 미구현

class Background:
    def __init__(self, *args):
        
        self.shape = args[0]        # 배경 이미지
        self.xSpeed = args[1]       # 배경 x 좌표
        self.ySpeed = args[2]       # 배경 y 좌표
        
        self.width = self.shape.get_rect().size[0]  # 가로 크기
        self.height = self.shape.get_rect().size[1] # 세로 크기
        
        self.xPos = 0
        self.yPos = 0
        
        if self.xSpeed == 0:
            self.xPosSub = 0
        else:
            self.xPosSub = - self.width
            
        if self.ySpeed == 0:
            self.yPosSub = 0
        else:
            self.yPosSub = - self.height
        
        

    def Move(self):
        self.xPos += self.xSpeed
        self.xPosSub += self.xSpeed
        
        if self.xSpeed > 0:
            if self.xPos >= self.width:
                self.xPos = self.xPosSub - self.width
            if self.xPosSub >= self.width:
                self.xPosSub = self.xPos - self.width
        elif self.xSpeed < 0:
            if self.xPos <= -self.width:
                self.xPos = self.xPosSub + self.width
            if self.xPosSub <= -self.width:
                self.xPosSub = self.xPos + self.width
        
        
        self.yPos += self.ySpeed
        self.yPosSub += self.ySpeed
        
        if self.ySpeed > 0:
            if self.yPos >= self.height:
                self.yPos = self.yPosSub - self.height
            if self.yPosSub >= self.height:
                self.yPosSub = self.yPos - self.height
        elif self.ySpeed < 0:
            if self.yPos <= -self.height:
                self.yPos = self.yPosSub + self.height
            if self.yPosSub <= -self.height:
                self.yPosSub = self.yPos + self.height

        
            
        
            
        
        
