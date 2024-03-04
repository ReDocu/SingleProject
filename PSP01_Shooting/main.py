import pygame
import sys
import os

# Custom Class
import background
import actor
import text
import bullet
import pool

import random

from time import sleep

padWidth = 480
padHeight = 640
static_frame = 30

#################################################
# 배경
image_backgrounds = {}
data_backgrounds = {}
play_backgrounds = {}

# 프로필
image_player_profiles = {}

image_bomb = {}

# 플레이어
image_players = {}
image_monsters = {}
image_bosses = {}
image_bullets = {}
   
# 보스

data_players = {}
data_monsters = {}
data_bosses = {}
data_bullets = {}

play_players = {}
play_monsters = {}
play_bosses = {}
play_bullets = {}

    
# 이펙트
image_effects = {}
data_effects = {}
play_effects = {}

# 사운드
game_sounds = {}
game_etc_sounds ={}

#################################################
mode = 0

scene = 0
stage = 0

game_clear = False
save_timer = 0
select_player = 1

score = 0

#################################################
# 플레이어 관리 코드
player_life = 3
player_bomber_count = 3

outro_phase = -1

boss00_phase = -1
boss01_phase = -1
boss02_phase = -1

boss00_angle = 0
boss01_angle = 0
boss02_angle = 0

debug = False

#############################################
# Game Resource Setting
def readGameResource():
    global image_backgrounds, image_player_profiles, image_players , image_monsters , image_bosses, image_bullets, image_effects, image_bomb
    
    current_path = os.path.dirname(__file__)
    
    image_path = os.path.join(current_path, "image")
    
    ######
    # 배경
    image_backgrounds["Intro"] = pygame.image.load(os.path.join(image_path,'intro_background.jpg'))
    
    image_backgrounds["Desert"] = pygame.image.load(os.path.join(image_path,'background00.png'))
    image_backgrounds["Desert"] = pygame.transform.scale(image_backgrounds["Desert"],(padWidth,padHeight))
    image_backgrounds["Sea"] = pygame.image.load(os.path.join(image_path,'background01.png'))
    image_backgrounds["Sea"] = pygame.transform.scale(image_backgrounds["Sea"],(padWidth,padHeight))
    image_backgrounds["Mountain"] = pygame.image.load(os.path.join(image_path,'background02.png'))
    image_backgrounds["Mountain"] = pygame.transform.scale(image_backgrounds["Mountain"],(padWidth,padHeight))
    
    # 플레이어
    # 1번 전투기
    image_players["1"] = (pygame.image.load(os.path.join(image_path,"player_01.png")))
    image_players["1"] = pygame.transform.scale(image_players["1"],(40,42))
    image_player_profiles["1"] = (pygame.image.load(os.path.join(image_path,"player_01_main.png")))
    image_player_profiles["1"] = pygame.transform.scale(image_player_profiles["1"],(151,180))
    
    # 2번 전투기
    image_players["2"] =(pygame.image.load(os.path.join(image_path,"player_02.png")))
    image_players["2"] = pygame.transform.scale(image_players["2"],(40,48))
    image_player_profiles["2"] = (pygame.image.load(os.path.join(image_path,"player_02_main.png")))
    image_player_profiles["2"] = pygame.transform.scale(image_player_profiles["2"],(163,180))
    
    image_bomb["1"] = (pygame.image.load(os.path.join(image_path,"bomb_01.png")))
    image_bomb["1"] = pygame.transform.scale(image_bomb["1"],(40,40))
    # 몬스터
    # 팩맨 빨강
    image_monsters["1"] = (pygame.image.load(os.path.join(image_path,"monster01.png")))
    image_monsters["1"] = pygame.transform.scale(image_monsters["1"],(48,48))
    image_monsters["2"] = pygame.transform.flip(image_monsters["1"], True, False)
    
    image_monsters["3"] = (pygame.image.load(os.path.join(image_path,"monster01.png")))
    image_monsters["3"] = pygame.transform.scale(image_monsters["3"],(48,48))
    image_monsters["4"] = pygame.transform.flip(image_monsters["3"], True, False)
    
    # 팩맨 노랑
    image_monsters["5"] = (pygame.image.load(os.path.join(image_path,"monster02.png")))
    image_monsters["5"] = pygame.transform.scale(image_monsters["5"],(48,48))
    image_monsters["6"] = pygame.transform.flip(image_monsters["5"], True, False)
    
    # 팩맨 초록
    image_monsters["7"] = (pygame.image.load(os.path.join(image_path,"monster03.png")))
    image_monsters["8"] = pygame.transform.scale(image_monsters["7"],(48,48))
    image_monsters["8"] = pygame.transform.flip(image_monsters["7"], True, False)
    
    # 팩맨 파랑
    image_monsters["9"] = (pygame.image.load(os.path.join(image_path,"monster04.png")))
    image_monsters["9"] = pygame.transform.scale(image_monsters["9"],(48,48))
    image_monsters["10"] = pygame.transform.flip(image_monsters["9"], True, False)
    
    
    # 보스 사막
    image_bosses["1"] = (pygame.image.load(os.path.join(image_path,"Stage00boss.png")))
    image_bosses["1"] = pygame.transform.scale(image_bosses["1"],(256,256))
    
    image_bosses["2"] = (pygame.image.load(os.path.join(image_path,"Stage01boss.png")))
    image_bosses["2"] = pygame.transform.scale(image_bosses["2"],(256,256))
    
    image_bosses["3"] = (pygame.image.load(os.path.join(image_path,"Stage02boss.png")))
    image_bosses["3"] = pygame.transform.scale(image_bosses["3"],(386,200))
    
    # 총알
    image_bullets["1"] = (pygame.image.load(os.path.join(image_path,"origin_missile.png")))
    image_bullets["2"] = (pygame.image.load(os.path.join(image_path,"heart_bullet_original.png")))
    image_bullets["2"] = pygame.transform.scale(image_bullets["2"],(23,23))
    
    image_bullets["5"] = (pygame.image.load(os.path.join(image_path,"bullet001.png")))
    image_bullets["5"] = pygame.transform.scale(image_bullets["5"],(23,46))
    image_bullets["6"] = (pygame.image.load(os.path.join(image_path,"bullet002.png")))
    image_bullets["6"] = pygame.transform.scale(image_bullets["6"],(23,23))
    image_bullets["7"] = (pygame.image.load(os.path.join(image_path,"bullet003.png")))
    image_bullets["7"] = pygame.transform.scale(image_bullets["7"],(23,23))
    image_bullets["8"] = (pygame.image.load(os.path.join(image_path,"bullet004.png")))
    image_bullets["8"] = pygame.transform.scale(image_bullets["8"],(23,23))
    image_bullets["9"] = (pygame.image.load(os.path.join(image_path,"bullet005.png")))
    image_bullets["9"] = pygame.transform.scale(image_bullets["9"],(46,46))
    
    
    # 이펙트
    image_effects["1"] = (pygame.image.load(os.path.join(image_path,"explosion.png")))
    
def saveResourceData():
    # 가져오는 전역변수
    global image_backgrounds, image_player_profiles, image_players , image_monsters , image_bosses, image_bullets, image_effects
    global data_backgrounds, data_players, data_monsters, data_bosses, data_bullets, data_effects

    # 배경
    data_backgrounds["Intro"] = background.Background(image_backgrounds["Intro"], 1, 0)
    
    data_backgrounds["Desert"] = background.Background(image_backgrounds["Desert"], 0, 3)
    data_backgrounds["Sea"] = background.Background(image_backgrounds["Sea"], 0, 3)
    data_backgrounds["Mountain"] = background.Background(image_backgrounds["Mountain"], 0, 3)
   
    # 플레이어
    data_players["1"] = actor.Player("1", image_players["1"], 10, 5, 5, 0.3, image_player_profiles["1"],3,3)
    data_players["2"] = actor.Player("2", image_players["2"], 10, 5, 5, 0.5, image_player_profiles["2"],3,3)
    data_players["2"].SetShield(True)
    # 몬스터
    # 사막 몬스터
    data_monsters["1"] = actor.Enemy("1", image_monsters["1"], 1,5,5,0.5)
    data_monsters["2"] = actor.Enemy("2", image_monsters["2"], 1,5,5,0.5)
    data_monsters["3"] = actor.Enemy("3", image_monsters["3"], 1,5,5,0.5)
    data_monsters["4"] = actor.Enemy("4", image_monsters["4"], 1,5,5,0.5)
    data_monsters["5"] = actor.Enemy("5", image_monsters["5"], 1,5,5,0.5)
    data_monsters["6"] = actor.Enemy("6", image_monsters["6"], 1,5,5,0.5)
    data_monsters["7"] = actor.Enemy("3", image_monsters["7"], 1,5,5,0.5)
    data_monsters["8"] = actor.Enemy("4", image_monsters["8"], 1,5,5,0.5)
    data_monsters["9"] = actor.Enemy("5", image_monsters["9"], 1,5,5,0.5)
    data_monsters["10"] = actor.Enemy("6", image_monsters["10"], 1,5,5,0.5)

    # 보스 데이터 세팅
    data_bosses["1"] = actor.Boss("1", image_bosses["1"], 1000, 5,5,0.5)
    data_bosses["2"] = actor.Boss("2", image_bosses["2"], 1000, 5,5,0.5)
    data_bosses["3"] = actor.Boss("3", image_bosses["3"], 1000, 5,5,0.5)
    
    # 총알
    data_bullets["1"] = bullet.Bullet("1", image_bullets["1"], 2)
    data_bullets["2"] = bullet.Bullet("2", image_bullets["2"], 2)
    
    data_bullets["5"] = bullet.Bullet("5", image_bullets["5"], 2)
    data_bullets["6"] = bullet.Bullet("6", image_bullets["6"], 2)
    data_bullets["7"] = bullet.Bullet("7", image_bullets["7"], 2)
    data_bullets["8"] = bullet.Bullet("8", image_bullets["8"], 2)
    data_bullets["9"] = bullet.Bullet("9", image_bullets["9"], 2)

def makePooling():
    global data_backgrounds, data_players, data_monsters, data_bosses, data_bullets, data_effects
    global play_monsters, play_bullets, play_bosses, play_effects
    
    
    play_monsters["1"] = pool.enemyPool(data_monsters["1"])
    play_monsters["2"] = pool.enemyPool(data_monsters["2"])
    play_monsters["3"] = pool.enemyPool(data_monsters["3"])
    play_monsters["4"] = pool.enemyPool(data_monsters["4"])
    play_monsters["5"] = pool.enemyPool(data_monsters["5"])
    play_monsters["6"] = pool.enemyPool(data_monsters["6"])
    play_monsters["7"] = pool.enemyPool(data_monsters["7"])
    play_monsters["8"] = pool.enemyPool(data_monsters["8"])
    play_monsters["9"] = pool.enemyPool(data_monsters["9"])
    play_monsters["10"] = pool.enemyPool(data_monsters["10"])
    
    play_bosses["1"] = pool.bossPool(data_bosses["1"])
    play_bosses["2"] = pool.bossPool(data_bosses["2"])
    play_bosses["3"] = pool.bossPool(data_bosses["3"])
    
    
    play_bullets["1"] = pool.bulletPool(data_bullets["1"])
    play_bullets["2"] = pool.bulletPool(data_bullets["2"])
    
    play_bullets["5"] = pool.bulletPool(data_bullets["5"])
    play_bullets["6"] = pool.bulletPool(data_bullets["6"])
    play_bullets["7"] = pool.bulletPool(data_bullets["7"])
    play_bullets["8"] = pool.bulletPool(data_bullets["8"])
    play_bullets["9"] = pool.bulletPool(data_bullets["9"])
    pass    

def readSoundResource():
    global game_sounds
    
    current_path = os.path.dirname(__file__)
    
    sound_path = os.path.join(current_path, "sound")
    
    game_sounds["intro_sound"] = pygame.mixer_music.load(os.path.join(sound_path,'intro_main_sound.mp3'))
   
    game_etc_sounds["shoot"] = pygame.mixer.Sound(os.path.join(sound_path,'Bullets_shoot.mp3'))
    game_etc_sounds["collision"] = pygame.mixer.Sound(os.path.join(sound_path,'collision.mp3'))
    
    

def managerSetting():
    global gamePad
    global textManager
   
    textManager = text.TextManager(gamePad,padWidth,padHeight)


#############################################
# Static 함수
def findCenterText(msg,size):
    
    font = pygame.font.SysFont('malgungothic',size)
    text = font.render(msg, True, (0,0,0))
    
    pos = text.get_rect(center = gamePad.get_rect().center)
    
    return [pos.x, pos.y]

def DrawObject(obj, xPos, yPos):
    global gamePad
    gamePad.blit(obj,(xPos,yPos))

def ChangeScene(number):
    global stage_timer, save_timer, scene
    global intro_phase, hud_phase
    global currentBG
    global stage00_phase, boss00_phase, stage01_phase, boss01_phase, stage02_phase, boss02_phase, outro_phase
    global boss00_angle, boss01_angle, boss02_angle
    global play_bosses, play_monsters, play_bullets
    
    textManager.Release()
    textManager.fade = False
    
    save_timer = 0
    stage_timer = pygame.time.get_ticks()
    scene = number
    
    if scene == 0:
        currentBG = data_backgrounds["Intro"]
    elif scene == 2:
        currentBG = data_backgrounds["Intro"]
    
    ###phase Management
    intro_phase = -1
    hud_phase = -1
    
    outro_phase = -1
    #
    stage00_phase = -1
    stage01_phase = -1
    stage02_phase = -1
    #
    boss00_phase = -1
    boss01_phase = -1
    boss02_phase = -1
    #
    boss00_angle = 0
    boss01_angle = 0
    boss02_angle = 0
    
    for key in play_bullets:
        play_bullets[key].AllDead()
                            
    for key in play_monsters:
        play_monsters[key].AllDead()
                            
    for key in play_bosses:
        play_bosses[key].AllDead()                    



def ChangeStage(number):
    global stage_timer, stage, scene,currentPlayer
    global currentBG
    
    stage_timer = pygame.time.get_ticks()
    stage = number
    
    if scene == 1:
        if stage == 0:
            currentBG = data_backgrounds["Desert"]
        elif stage == 1:
            currentBG = data_backgrounds["Sea"]
        elif stage == 2:
            currentBG = data_backgrounds["Mountain"]
    
    currentPlayer.isAlive = False
    
    #if stage == 0
    
    
def SelectPlayer(number):
    global currentPlayer
    global player_life, player_bomber_count
    
    currentPlayer = data_players[str(select_player)]
    player_life = currentPlayer.initLife
    player_bomber_count = currentPlayer.initBomber
    
    currentPlayer.xPos = 70 + (130 * (select_player - 1))
    currentPlayer.yPos = 550
    
    currentPlayer.startPosX = currentPlayer.xPos
    currentPlayer.startPosY = currentPlayer.yPos
    

def ResetData():
    global score, currentPlayer, player_life, player_bomber_count
    
    score = 0
    player_life = currentPlayer.initLife
    player_bomber_count = currentPlayer.initBomber

#############################################
# Intro

def Intro(event):
    global intro_phase
    global scene, stage, stage_timer, save_timer, game_clear, select_player, currentPlayer, score
    global textManager
    global game_sounds
    
    timer = (pygame.time.get_ticks() - stage_timer) / 1000
    
    if timer > 0.0 and intro_phase < 0:
        pos = findCenterText("몬스터를 찾아서",48)
        textManager.SetTextMove("number1",-600,pos[1] - 200 ,pos[0] + 35,pos[1] - 200,"몬스터를 찾아서", 54, 20,(128,128,96))
        textManager.SetFont("number1","NanumPenScript-Regular.ttf")
        
        pygame.mixer.music.play(-1)
        score = 0
        
        
        intro_phase = 0
    elif timer > 1.0 and intro_phase < 1:
        pos = findCenterText("3팀 슈팅 프로젝트",40)
        textManager.SetTextMove("number2", pos[0] + 200 ,pos[1] + 600, pos[0] + 200,pos[1] - 100,"3팀 슈팅 프로젝트", 42, 8,(196,196,96))
        textManager.SetFont("number2","Dongle-Bold.ttf")
        intro_phase = 1
    elif timer > 4.0 and intro_phase < 2:
        pos = findCenterText("이름",40)
        textManager.SetTextAlpha("member1", pos[0] + 150 ,pos[1] - 30,"구 혜령", 36,(196,196,96))
        textManager.SetFont("member1","Dongle-Light.ttf")
        textManager.SetTextAlpha("member2", pos[0] + 150 ,pos[1] + 0,"김 기운", 36,(196,196,96))
        textManager.SetFont("member2","Dongle-Light.ttf")
        textManager.SetTextAlpha("member3", pos[0] + 150 ,pos[1] + 30,"김 현구", 36,(196,196,96))
        textManager.SetFont("member3","Dongle-Light.ttf")
        textManager.SetTextAlpha("member4", pos[0] + 150 ,pos[1] + 60,"이 도규", 36,(196,196,96))
        textManager.SetFont("member4","Dongle-Light.ttf")
        intro_phase = 2
    elif timer > 5.5 and intro_phase < 3:
        pos = findCenterText("Press 'Enter' or 'Z' Key to Start",40)
        textManager.SetTextBlink("number3",pos[0] + 126,pos[1] + 200,"Press 'Enter' or 'Z' Key to Start", 32,(128,128,96))
        textManager.SetFont("number3","Dongle-Light.ttf")
        intro_phase = 3
    
    elif intro_phase == 3:
        if event.type in [pygame.KEYDOWN]:
            if event.key == pygame.K_RETURN or event.key == pygame.K_z:
                textManager.OnExit(["number1", "number2","number3", "member1","member2","member3", "member4"])
                intro_phase = 4
                stage_timer = pygame.time.get_ticks()
    
    elif intro_phase == 4:
        pos = findCenterText("몬스터를 찾아서",48)
        
        textManager.SetText("title2",50,50,"플레이어 선택",54,(128,128,96))
        textManager.SetFont("title2","Dongle-Bold.ttf")
        
        # 정보
        textManager.SetText("intro_power",240,150,"Power",24,(196,196,96))
        textManager.SetFont("title2","Dongle-Light.ttf")
        
        textManager.SetText("intro_speed",240,210,"Speed",24,(196,196,96))
        textManager.SetFont("title2","Dongle-Light.ttf")
        
        textManager.SetText("intro_delay",240,270,"Delay",24,(196,196,96))
        textManager.SetFont("title2","Dongle-Light.ttf")
        
        textManager.SetText("wait_update",55 + 260,570 ,"업데이트 중...",36,(255,0,128))
        textManager.SetFont("wait_update","Dongle-Bold.ttf")
        
        ready_time = 5
        select_time = int(ready_time - timer)
        textManager.SetText("timer_update",55 + 260, 490 ,f"선택 시간 : {select_time}",20,(196,196,96))

        if select_time <= 0:
            textManager.OnExit(["title2", "intro_power","intro_speed", "intro_delay","wait_update","timer_update"])
            intro_phase = 5
            stage_timer = pygame.time.get_ticks()


        if event.type in [pygame.KEYDOWN]:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                select_player -= 1
            
                if select_player < 1:
                    select_player = len(data_players)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                select_player += 1
                
                if select_player > len(data_players):
                    select_player = 1
                    
            SelectPlayer(select_player)
           
            if event.key == pygame.K_z or event.key == pygame.K_RETURN:
                textManager.OnExit(["title2", "intro_power","intro_speed", "intro_delay","wait_update","timer_update"])
                intro_phase = 5
    elif intro_phase == 5:
        if currentPlayer.MoveDestination(padWidth/2 - 50,padHeight/2,2) == True:
            intro_phase = 6
            stage_timer = pygame.time.get_ticks()
    elif intro_phase == 6:
        if currentPlayer.MoveDestination(padWidth/2 - 50,-400, 3) == True:
            intro_phase = 7
    elif intro_phase == 7:
            textManager.fade = True
            save_timer = pygame.time.get_ticks()
            game_clear = True
            intro_phase = 8
    
    if game_clear == True: 
        if (pygame.time.get_ticks() - save_timer) / 1000 > 4.0:
            ChangeScene(1)
            ChangeStage(0)
            game_clear = False

def IntroRender():
    global gamePad, intro_phase         
    global currentPlayer
    
    if intro_phase == 4:
        DrawObject(currentPlayer.profile, 50,175)
        
        # 최대 힘 0 ~ 10
        pygame.draw.rect(gamePad, (196,196,96), [240, 190, currentPlayer.power * 20, 20])
        pygame.draw.rect(gamePad, (196,196,96), [240, 190, 200, 20], 2)
        
        # 최대 속도 0 ~ 10
        pygame.draw.rect(gamePad, (196,196,96), [240, 250, currentPlayer.speed * 20, 20])
        pygame.draw.rect(gamePad, (196,196,96), [240, 250, 200, 20], 2)
        
        # 최대 딜레이 0 ~ 1
        pygame.draw.rect(gamePad, (196,196,96), [240, 310, (1 - currentPlayer.shotDelay) * 200, 20])
        pygame.draw.rect(gamePad, (196,196,96), [240, 310, 200, 20], 2)
        
        # 필살기 레이아웃 박스
        pygame.draw.rect(gamePad, (196,196,96), [30, 380, 420, 100], 2)
        
        # 캐릭터 창 레이아웃 박스
        pygame.draw.rect(gamePad, (196,196,96), [30, 520, 420, 100], 2)
        
        for id in range(0, len(data_players)):
            
            if data_players[str(id + 1)].shieldAlive == True:
                pygame.draw.circle(gamePad,(255,255,255),(70 + (130 * id) + 20 ,550 + 24),36)

            DrawObject(data_players[str(id + 1)].shape, 70 + (130 * id),550)

        pygame.draw.rect(gamePad, (255,0,0), [55 + 130 * (int(currentPlayer.id) - 1), 530, 70, 80], 2)
            
    elif intro_phase >= 5:
        if currentPlayer.shieldAlive == True:
            pygame.draw.circle(gamePad,(255,255,255),(currentPlayer.xPos + 20,currentPlayer.yPos + 24),36)
    
        DrawObject(currentPlayer.shape, currentPlayer.xPos, currentPlayer.yPos)

def StageHUD():
    global hud_phase
    global stage_timer
    global textManager
    global player_life, player_bomber_count
    global score

    textManager.SetText("title2",20,0,f"SCORE : {score} ",32,(128,128,96))
    textManager.SetFont("title2","Dongle-Bold.ttf")
    
    if hud_phase == -1:
        
        textManager.SetText("bomb",300,0,f"Bomb ",32,(128,128,96))
        textManager.SetFont("bomb","Dongle-Bold.ttf")
        
        hud_phase = 0

def StageHUDRender():
    global currentPlayer
    global player_life, player_bomber_count
    for i in range (0,player_life):
        DrawObject(currentPlayer.shape, 10 + (i * 50), 40)
        
    for i in range (0, player_bomber_count):
        DrawObject(image_bomb["1"],300 + (i * 50), 40)

start_time = 3.0

def Stage00(event):
    global scene, score, stage, stage_timer, save_timer, game_clear, currentPlayer, game_clear
    global textManager
    global stage00_phase, boss00_phase
    global currentBoss
    global boss00_angle
    
    timer = (pygame.time.get_ticks() - stage_timer) / 1000
    
    if stage00_phase < 0:
        stage00_phase = 0
        currentPlayer.startPosX = 250
        currentPlayer.startPosY = 850
        
       
        pos = findCenterText("사막의 폭풍",54)
        textManager.SetTextMove("Stage01",-600,pos[1]- 100 ,pos[0] + 150,pos[1] - 100,"사막의 폭풍", 54, 20,(128,128,96))
        
        textManager.SetFont("Stage01","Dongle-Bold.ttf")
    elif stage00_phase == 0:
        if currentPlayer.MoveDestination(250 ,500, 3) == True:
            currentPlayer.isAlive = True
            stage_timer = pygame.time.get_ticks()
            stage00_phase = 1
    elif timer > 1.0 and stage00_phase == 1:
        pos = findCenterText("사막의 폭풍",54)
        textManager.SetTextMove("Stage01",pos[0] + 150,pos[1] - 100,900,pos[1] - 100 ,"사막의 폭풍", 54, 20,(128,128,96))
        stage00_phase = 2
    elif timer > start_time and stage00_phase < 3:
        stage00_phase = 3
        
        # 5 / 10 / 40 / 50
    elif timer > start_time + 5.0 and stage00_phase < 4:
        stage00_phase = 4
    elif timer > start_time + 10.0 and stage00_phase < 5:
        stage00_phase = 5
    elif timer > start_time + 40.0 and stage00_phase < 6:
        stage00_phase = 6    
    elif timer > start_time + 50.0 and stage00_phase < 7:
        currentBoss = play_bosses["1"].SpawnObj()
        currentBoss.AppearSpawn(100,-256,"Enemy")
        currentBoss.startPosX = 100
        currentBoss.startPosY = -256
        stage00_phase = 7
    elif stage00_phase == 8:
        if currentPlayer.MoveDestination(padWidth/2 - 50,-400, 3) == True:
            stage00_phase = 9
    elif stage00_phase == 9:
        textManager.fade = True
        save_timer = pygame.time.get_ticks()
        game_clear = True
        stage00_phase = 10
    
    if stage00_phase == 3:
        if play_monsters["2"].SpawnDelay(0.8) == True:
            play_monsters["2"].SpawnObj().MoveSpawn(400, -100, 3, 110 + random.randrange(0,40), "Enemy")

    if stage00_phase == 4:
        if play_monsters["1"].SpawnDelay(0.8) == True:
            monster = play_monsters["1"].SpawnObj()
            monster.MoveSpawn(50, -100, 3, 80 - random.randrange(0,40), "Enemy")

    if stage00_phase == 5:
        if play_monsters["3"].SpawnDelay(1.0) == True:       
            setSize = random.randint(36,128)
            
            monster = play_monsters["3"].SpawnObj()
            monster.MoveSpawn(50, -100, 3, 80 - random.randrange(0,40), "Enemy")
            monster.ChangeScale(setSize,setSize)

        if play_monsters["4"].SpawnDelay(1.0) == True:
            
            setSize = random.randint(36,128)
            
            monster = play_monsters["4"].SpawnObj()
            monster.MoveSpawn(400, -100, 3, 110 + random.randrange(0,40), "Enemy")
            monster.ChangeScale(setSize,setSize)
    
    if stage00_phase == 7:
        if play_monsters["5"].SpawnDelay(1.0) == True:       
            setSize = random.randint(36,48)
            
            monster = play_monsters["5"].SpawnObj()
            monster.MoveSpawn(-100, 300, 3, -20 + random.randrange(0,40), "Enemy")
            monster.ChangeScale(setSize,setSize)
            
        if play_monsters["6"].SpawnDelay(1.0) == True:       
            setSize = random.randint(36,48)
            
            monster = play_monsters["6"].SpawnObj()
            monster.MoveSpawn(530, 300, 3, 160 + random.randrange(0,40), "Enemy")
            monster.ChangeScale(setSize,setSize)
            
        if currentBoss.currentHp < 0:
            
            currentPlayer.startPosX = currentPlayer.xPos
            currentPlayer.startPosY = currentPlayer.yPos
            
            currentPlayer.isAlive = False
            
            for key in play_bullets:
                play_bullets[key].AllDead()
                            
            for key in play_monsters:
                for monster in play_monsters[key].pool:                         
                    if monster.isAlive == True:
                        if monster.Hit(5) == True:
                            score += 100
            stage00_phase = 8

    # 보스패턴
    if currentBoss.isAlive == True:
        
        if boss00_phase == -1:
            if currentBoss.MoveDestination(100,50,3) == True:
                boss00_phase = 0
         
        if boss00_phase == -1:
            if currentBoss.ShotDelay():
            
                xPos = currentBoss.xPos + currentBoss.width/2
                yPos = currentBoss.yPos + currentBoss.height/2
                
                newBullet = play_bullets["5"].SpawnObj()
                newBullet.AngleFire(xPos ,yPos,15,60,"Enemy")
                newBullet.ChangeRotation(30)
                newBullet = play_bullets["5"].SpawnObj()
                newBullet.AngleFire(xPos ,yPos,15,90,"Enemy")
                newBullet.ChangeRotation(0)
                newBullet = play_bullets["5"].SpawnObj()
                newBullet.AngleFire(xPos,yPos,15,120,"Enemy")
                newBullet.ChangeRotation(-30)
        elif boss00_phase == 0:
            currentBoss.ChangeShotDelay(0.3)
            
            if currentBoss.ShotDelay():
                xPos = currentBoss.xPos + currentBoss.width/2
                yPos = currentBoss.yPos + currentBoss.height/2
                
                boss00_angle += 5
                
                if boss00_angle > 360:
                    boss00_angle = 0
                
                newBullet = play_bullets["5"].SpawnObj()
                newBullet.AngleFire(xPos ,yPos,15,boss00_angle + 90,"Enemy")
                newBullet.ChangeRotation(360 - boss00_angle)
                
                newBullet = play_bullets["5"].SpawnObj()
                newBullet.AngleFire(xPos ,yPos,15,(180 + boss00_angle) + 90,"Enemy")
                newBullet.ChangeRotation(360 - (180 + boss00_angle))
       
    # 몬스터 패턴
    for monster in play_monsters["1"].pool:
        if monster.isAlive == True:
            if monster.ShotDelay() == True:
                xPos = monster.xPos + monster.width/2
                yPos = monster.yPos + monster.height/2
                    
                newBullet = play_bullets["5"].SpawnObj()
                newBullet.AngleFire(xPos,yPos,15,90,"Enemy")
                newBullet.ChangeRotation(0)
    
    for monster in play_monsters["2"].pool:
        if monster.isAlive == True:
            if monster.ShotDelay() == True:
                xPos = monster.xPos + monster.width/2
                yPos = monster.yPos + monster.height/2
                    
                newBullet = play_bullets["5"].SpawnObj()
                newBullet.AngleFire(xPos,yPos,15,90,"Enemy")
                newBullet.ChangeRotation(0)
                
    for monster in play_monsters["3"].pool:
        if monster.isAlive == True:
            if monster.ShotDelay() == True:
                xPos = monster.xPos + monster.width/2
                yPos = monster.yPos + monster.height/2
                    
                newBullet = play_bullets["5"].SpawnObj()
                newBullet.AngleFire(xPos,yPos,15,90,"Enemy")
                newBullet.ChangeRotation(0)
                
    for monster in play_monsters["4"].pool:
        if monster.isAlive == True:
            if monster.ShotDelay() == True:
                xPos = monster.xPos + monster.width/2
                yPos = monster.yPos + monster.height/2
                    
                newBullet = play_bullets["5"].SpawnObj()
                newBullet.AngleFire(xPos,yPos,15,90,"Enemy")
                newBullet.ChangeRotation(0)
    
    for monster in play_monsters["5"].pool:
        if monster.isAlive == True:
            if monster.ShotDelay() == True:
                xPos = monster.xPos + monster.width/2
                yPos = monster.yPos + monster.height/2
                    
                newBullet = play_bullets["6"].SpawnObj()
                newBullet.TargetFire(xPos,yPos,currentPlayer.xPos, currentPlayer.yPos, "Enemy", 3) 
                
    for monster in play_monsters["6"].pool:
        if monster.isAlive == True:
            if monster.ShotDelay() == True:
                xPos = monster.xPos + monster.width/2
                yPos = monster.yPos + monster.height/2
                    
                newBullet = play_bullets["6"].SpawnObj()
                newBullet.TargetFire(xPos,yPos,currentPlayer.xPos, currentPlayer.yPos, "Enemy", 3) 
    
    if game_clear == True:
        if (pygame.time.get_ticks() - save_timer) / 1000 > 4.0:
            ChangeScene(1)
            ChangeStage(1)
            game_clear = False
    
def Stage00Render():
    global stage00_phase
    global currentBoss
    
    if currentBoss.isAlive == True:
        pygame.draw.rect(gamePad, (0,255,0), [currentBoss.xPos , currentBoss.yPos + currentBoss.height, (currentBoss.currentHp) * (currentBoss.width / currentBoss.hp), 20])
        
    # gamePad, 색깔 [rect -]
   
def Stage01(event):
    global scene, score, stage, stage_timer, save_timer, game_clear, currentPlayer, game_clear
    global stage01_phase, boss01_phase, boss01_angle
    global textManager
    global currentBoss
    
    timer = (pygame.time.get_ticks() - stage_timer) / 1000
    
    if stage01_phase < 0:
        stage01_phase = 0
        currentPlayer.startPosX = 250
        currentPlayer.startPosY = 850
        
        pos = findCenterText("바다 괴물",54)
        textManager.SetTextMove("Stage02",-600,pos[1]- 100 ,pos[0] + 150,pos[1] - 100,"바다 괴물", 54, 20,(0,128,255))
        
        textManager.SetFont("Stage02","Dongle-Bold.ttf")
        
    elif stage01_phase == 0:
        if currentPlayer.MoveDestination(250 ,500, 3) == True:
            currentPlayer.isAlive = True
            stage_timer = pygame.time.get_ticks()
            stage01_phase = 1
    elif timer > 1.0 and stage01_phase == 1:
        pos = findCenterText("바다 괴물",54)
        textManager.SetTextMove("Stage02",pos[0] + 150,pos[1] - 100,900,pos[1] - 100 ,"바다 괴물", 54, 20,(0,128,255))
        stage01_phase = 2
    elif timer > 5.0 and stage01_phase < 3:
        currentBoss = play_bosses["2"].SpawnObj()
        currentBoss.AppearSpawn(100,-256,"Enemy")
        currentBoss.startPosX = 100
        currentBoss.startPosY = -256
        stage01_phase = 3
    elif stage01_phase == 3:
        if currentBoss.currentHp < 0:
            
            currentPlayer.startPosX = currentPlayer.xPos
            currentPlayer.startPosY = currentPlayer.yPos
            
            currentPlayer.isAlive = False
            
            for key in play_bullets:
                play_bullets[key].AllDead()
                            
            for key in play_monsters:
                for monster in play_monsters[key].pool:                         
                    if monster.isAlive == True:
                        if monster.Hit(5) == True:
                            score += 100
            stage01_phase = 4
    elif stage01_phase == 4:
        currentPlayer.startPosX = currentPlayer.xPos
        currentPlayer.startPosY = currentPlayer.yPos
        currentPlayer.isAlive = False
        stage01_phase = 5
    elif stage01_phase == 5:
        if currentPlayer.MoveDestination(padWidth/2 - 50,-400, 3) == True:
            stage01_phase = 6
    elif stage01_phase == 6:
        textManager.fade = True
        save_timer = pygame.time.get_ticks()
        game_clear = True
        stage01_phase = 7

    # 보스패턴
    if currentBoss.isAlive == True:
        
        if boss01_phase == -1:
            if currentBoss.MoveDestination(100,50,3) == True:
                boss01_phase = 0
         
        if boss01_phase == -1:
            if currentBoss.ShotDelay():
            
                xPos = currentBoss.xPos + currentBoss.width/2
                yPos = currentBoss.yPos + currentBoss.height/2
                
                newBullet = play_bullets["5"].SpawnObj()
                newBullet.AngleFire(xPos ,yPos,15,60,"Enemy")
                newBullet.ChangeRotation(30)
                newBullet = play_bullets["5"].SpawnObj()
                newBullet.AngleFire(xPos ,yPos,15,90,"Enemy")
                newBullet.ChangeRotation(0)
                newBullet = play_bullets["5"].SpawnObj()
                newBullet.AngleFire(xPos,yPos,15,120,"Enemy")
                newBullet.ChangeRotation(-30)
        elif boss01_phase == 0:
            currentBoss.ChangeShotDelay(0.3)
            
            if currentBoss.ShotDelay():
                xPos = currentBoss.xPos + currentBoss.width/2
                yPos = currentBoss.yPos + currentBoss.height/2
                
                boss01_angle += 10
                
                if boss01_angle > 360:
                    boss01_angle = 0
                
                if play_monsters["7"].SpawnDelay(1.0) == True:       
                    setSize = random.randint(36,48)
            
                    monster = play_monsters["7"].SpawnObj()
                    monster.MoveSpawn(-100, 300, 3, -20 + random.randrange(0,40), "Enemy")
                    monster.ChangeScale(setSize,setSize)
            
                if play_monsters["8"].SpawnDelay(1.0) == True:       
                    setSize = random.randint(36,48)
            
                    monster = play_monsters["8"].SpawnObj()
                    monster.MoveSpawn(530, 300, 3, 160 + random.randrange(0,40), "Enemy")
                    monster.ChangeScale(setSize,setSize)
                    
                if play_monsters["9"].SpawnDelay(1.0) == True:       
                    setSize = random.randint(36,48)
            
                    monster = play_monsters["9"].SpawnObj()
                    monster.MoveSpawn(0, -100, 3, 40 + random.randrange(0,30), "Enemy")
                    monster.ChangeScale(setSize,setSize)
            
                if play_monsters["10"].SpawnDelay(1.0) == True:       
                    setSize = random.randint(36,48)
            
                    monster = play_monsters["10"].SpawnObj()
                    monster.MoveSpawn(480, -100, 3, 120 + random.randrange(0,30), "Enemy")
                    monster.ChangeScale(setSize,setSize)    
                
                newBullet = play_bullets["5"].SpawnObj()
                newBullet.AngleFire(xPos ,yPos,15,boss01_angle + 90,"Enemy")
                newBullet.ChangeRotation(360 - boss01_angle)
                
                newBullet = play_bullets["5"].SpawnObj()
                newBullet.AngleFire(xPos ,yPos,15,(180 + boss01_angle) + 90,"Enemy")
                newBullet.ChangeRotation(360 - (180 + boss01_angle))
                
                newBullet = play_bullets["6"].SpawnObj()
                newBullet.TargetFire(xPos,yPos, currentPlayer.xPos, currentPlayer.yPos,"Enemy",5)


        
    if game_clear == True:
        if (pygame.time.get_ticks() - save_timer) / 1000 > 4.0:
            ChangeScene(1)
            ChangeStage(2)
            game_clear = False

def Stage01Render():
    global stage01_phase
    global currentBoss
    
    if currentBoss.isAlive == True:
        pygame.draw.rect(gamePad, (0,255,0), [currentBoss.xPos , currentBoss.yPos + currentBoss.height, (currentBoss.currentHp) * (currentBoss.width / currentBoss.hp), 20])

def Stage02(event):
    global scene, score, stage, stage_timer, save_timer, game_clear, currentPlayer, game_clear
    global stage02_phase, boss02_angle, boss02_phase, currentBoss
    global textManager
    
    timer = (pygame.time.get_ticks() - stage_timer) / 1000
     
    if stage02_phase < 0:
        stage02_phase = 0
        currentPlayer.startPosX = 250
        currentPlayer.startPosY = 850
        
        pos = findCenterText("사막 지대",54)
        textManager.SetTextMove("Stage03",-600,pos[1]- 100 ,pos[0] + 150,pos[1] - 100,"산악 지대", 54, 20,(255,128,0))
        
        textManager.SetFont("Stage03","Dongle-Bold.ttf")
        
    elif stage02_phase == 0:
        if currentPlayer.MoveDestination(250 ,500, 3) == True:
            currentPlayer.isAlive = True
            stage_timer = pygame.time.get_ticks()
            stage02_phase = 1
    elif timer > 1.0 and stage02_phase == 1:
        pos = findCenterText("산악 지대",54)
        textManager.SetTextMove("Stage03",pos[0] + 150,pos[1] - 100,900,pos[1] - 100 ,"산악 지대", 54, 20,(255,128,0))
        stage02_phase = 2
    elif timer > 5.0 and stage02_phase < 3:
        currentBoss = play_bosses["3"].SpawnObj()
        currentBoss.AppearSpawn(50,-256,"Enemy")
        currentBoss.startPosX = 50
        currentBoss.startPosY = -256
        stage02_phase = 3
    elif stage02_phase == 3:
        if currentBoss.currentHp < 0:
            
            currentPlayer.startPosX = currentPlayer.xPos
            currentPlayer.startPosY = currentPlayer.yPos
            
            currentPlayer.isAlive = False
            
            for key in play_bullets:
                play_bullets[key].AllDead()
                            
            for key in play_monsters:
                for monster in play_monsters[key].pool:                         
                    if monster.isAlive == True:
                        if monster.Hit(5) == True:
                            score += 100
            stage02_phase = 4
    elif stage02_phase == 4:
        currentPlayer.startPosX = currentPlayer.xPos
        currentPlayer.startPosY = currentPlayer.yPos
        currentPlayer.isAlive = False
        stage02_phase = 5
    elif stage02_phase == 5:
        if currentPlayer.MoveDestination(padWidth/2 - 50,-400, 3) == True:
            stage02_phase = 6
    elif stage02_phase == 6:
        textManager.fade = True
        save_timer = pygame.time.get_ticks()
        game_clear = True
        stage02_phase = 7

    # 보스패턴
    if currentBoss.isAlive == True:
        
        if boss02_phase == -1:
            if currentBoss.MoveDestination(50,50,3) == True:
                boss02_phase = 0
         
        if boss02_phase == -1:
            if currentBoss.ShotDelay():
            
                xPos = currentBoss.xPos + currentBoss.width/2
                yPos = currentBoss.yPos + currentBoss.height/2
                
                newBullet = play_bullets["5"].SpawnObj()
                newBullet.AngleFire(xPos ,yPos,15,60,"Enemy")
                newBullet.ChangeRotation(30)
                newBullet = play_bullets["5"].SpawnObj()
                newBullet.AngleFire(xPos ,yPos,15,90,"Enemy")
                newBullet.ChangeRotation(0)
                newBullet = play_bullets["5"].SpawnObj()
                newBullet.AngleFire(xPos,yPos,15,120,"Enemy")
                newBullet.ChangeRotation(-30)
        elif boss02_phase == 0:
            currentBoss.ChangeShotDelay(0.6)
            
            if currentBoss.ShotDelay():
                xPos = currentBoss.xPos + currentBoss.width/2
                yPos = currentBoss.yPos + currentBoss.height/2
                
                boss02_angle += 10
                
                if boss02_angle > 360:
                    boss02_angle = 0
                
                newBullet = play_bullets["5"].SpawnObj()
                newBullet.AngleFire(xPos ,yPos,15,boss02_angle + 90,"Enemy")
                newBullet.ChangeRotation(360 - boss02_angle)
                
                newBullet = play_bullets["5"].SpawnObj()
                newBullet.AngleFire(xPos ,yPos,15,(180 + boss02_angle) + 90,"Enemy")
                newBullet.ChangeRotation(360 - (180 + boss02_angle))
                
                newBullet = play_bullets["5"].SpawnObj()
                newBullet.AngleFire(xPos ,yPos,15,boss02_angle,"Enemy")
                newBullet.ChangeRotation(360 - boss02_angle + 90)
                
                newBullet = play_bullets["5"].SpawnObj()
                newBullet.AngleFire(xPos ,yPos,15,(180 + boss02_angle),"Enemy")
                newBullet.ChangeRotation(360 - (180 + boss02_angle + 90))
                
                newBullet = play_bullets["6"].SpawnObj()
                newBullet.TargetFire(xPos,yPos, currentPlayer.xPos, currentPlayer.yPos,"Enemy",5)
                
                newBullet = play_bullets["6"].SpawnObj()
                newBullet.TargetFire(0,0, currentPlayer.xPos, currentPlayer.yPos,"Enemy",5)
                
                newBullet = play_bullets["6"].SpawnObj()
                newBullet.TargetFire(padWidth,0, currentPlayer.xPos, currentPlayer.yPos,"Enemy",5)


        
    if game_clear == True:
        if (pygame.time.get_ticks() - save_timer) / 1000 > 4.0:
            ChangeScene(2)
            ChangeStage(0)
            game_clear = False

def Stage02Render():
    global stage02_phase
    global currentBoss
    
    if currentBoss.isAlive == True:
        pygame.draw.rect(gamePad, (0,255,0), [currentBoss.xPos , currentBoss.yPos + currentBoss.height, (currentBoss.currentHp) * (currentBoss.width / currentBoss.hp), 20])

def Outro(event):
    global textManager
    global outro_phase
    global score
    
    if outro_phase < 0:
        textManager.OnExit(["title2", "bomb"])
        outro_phase = 0
    elif outro_phase == 0:
      
        textManager.SetText("title2",50,100,"Game Over",108,(128,128,96))
        textManager.SetFont("title2","Dongle-Bold.ttf")
        
        textManager.SetText("score",50,300,f"SCORE : {score}",54,(128,128,96))
        textManager.SetFont("score","Dongle-Bold.ttf")
        
        pos = findCenterText("Press 'Enter' Key to Start",40)
        textManager.SetTextBlink("intro_pass",pos[0] + 126,pos[1] + 150,"Press 'Enter' Key to Start", 32,(128,128,96))
        textManager.SetFont("intro_pass","Dongle-Light.ttf")
        
        outro_phase = 1
        
    if event.type in [pygame.KEYDOWN]:
        if event.key == pygame.K_RETURN:
            ChangeScene(0)

def OutroRender():
    pass

# Game Life Cycle
def InitPlay():
    global currentBG
    global currentPlayer, select_player, currentBoss
    # 초기 세팅 값
    ChangeScene(0)
    
    currentBG = data_backgrounds["Intro"]
    currentPlayer = data_players["1"]
    select_player = int(currentPlayer.id)
    
    currentBoss = data_bosses["1"]
    
    
def Update(event):
    global currentBG, currentPlayer
    global scene,stage
    global score
    global player_bomber_count, player_life
    global debug
    global game_etc_sounds
    
    pressed = pygame.key.get_pressed()
    
    if scene == 0:
        Intro(event)
    elif scene == 1:
        if stage == 0:
            Stage00(event)
        elif stage == 1:
            Stage01(event)
        elif stage == 2:
            Stage02(event)
        
        if currentPlayer.isAlive == True:
            # 캐릭터 움직임 제어
            if pressed[pygame.K_LEFT]:
                currentPlayer.xPos -= currentPlayer.speed
            if pressed[pygame.K_RIGHT]:
                currentPlayer.xPos += currentPlayer.speed
            if pressed[pygame.K_UP]:
                currentPlayer.yPos -= currentPlayer.speed
            if pressed[pygame.K_DOWN]:
                currentPlayer.yPos += currentPlayer.speed
        
            if currentPlayer.xPos < 0:
                currentPlayer.xPos = 0
            elif currentPlayer.xPos > padWidth - currentPlayer.width:
                currentPlayer.xPos = padWidth - currentPlayer.width
        
            if currentPlayer.yPos < 0:
                currentPlayer.yPos = 0
            elif currentPlayer.yPos > padHeight - currentPlayer.height:
                currentPlayer.yPos = padHeight - currentPlayer.height
            
            # 캐릭터 총알 발사
            if pressed[pygame.K_z]:
                if currentPlayer.ShotDelay() == True:
                    xPos = currentPlayer.xPos + currentPlayer.width/2
                    yPos = currentPlayer.yPos
                    
                    game_etc_sounds["shoot"].play()
                    
                    if currentPlayer.id == "1":
                        # 총알 세팅
                        newBullet = play_bullets["1"].SpawnObj()
                        newBullet.AngleFire(xPos + 10,yPos,15,270,"Player")
                        newBullet = play_bullets["1"].SpawnObj()
                        newBullet.AngleFire(xPos -6 ,yPos,15,270,"Player")
                        newBullet = play_bullets["1"].SpawnObj()
                        newBullet.AngleFire(xPos - 22,yPos,15,270,"Player")
                        
                    if currentPlayer.id == "2":
                        # 총알 세팅
                        newBullet = play_bullets["2"].SpawnObj()
                        newBullet.AngleFire(xPos + 8,yPos,15,240,"Player")
                        newBullet = play_bullets["2"].SpawnObj()
                        newBullet.AngleFire(xPos - 10 ,yPos,15,270,"Player")
                        newBullet = play_bullets["2"].SpawnObj()
                        newBullet.AngleFire(xPos - 28,yPos,15,300,"Player")

            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_x:
                    if player_bomber_count > 0:
                        player_bomber_count -= 1
                        
                        for key in play_bullets:
                            play_bullets[key].AllDead()

                        if currentPlayer.id == "1":
                            # 총알 세팅
                            xPos = currentPlayer.xPos + currentPlayer.width/2
                            yPos = currentPlayer.yPos + currentPlayer.height/2
                            for i in range(0,36):
                                newBullet = play_bullets["9"].SpawnObj()
                                newBullet.ChangeSpeed(3)
                                newBullet.AngleFire(xPos,yPos,15,10 * i,"Player")
                                newBullet.ChangeRotation(270 - (10 * i))
                                
                        if currentPlayer.id == "2":
                            # 총알 세팅
                            for key in play_monsters:
                                for monster in play_monsters[key].pool:                         
                                    if monster.isAlive == True:
                                        if monster.Hit(5) == True:
                                            score += 100
                                        
                            for key in play_bosses:
                                for boss in play_bosses[key].pool:                         
                                    if boss.isAlive == True:
                                        if boss.Hit(5) == True:
                                            score += 10000
                        
        # 총알 움직임 제어
        for key in play_bullets:
            for bul in play_bullets[key].pool:
                bul.Move()
                
                # 적기 충돌 체크
                for key in play_monsters:
                    for monster in play_monsters[key].pool:
                        if bul.CollisionEnemy(monster) == True:
                            if monster.Hit(currentPlayer.power) == True:
                                score += 100
                                
                            game_etc_sounds["collision"].play()
                            bul.isAlive = False
                
                for key in play_bosses:
                    for boss in play_bosses[key].pool:
                        if bul.CollisionEnemy(boss) == True:
                            if boss.Hit(currentPlayer.power) == True:
                                score += 10000
                            game_etc_sounds["collision"].play()
                            bul.isAlive = False
                            
                # 아군 충돌 체크
                if bul.CollisionPlayer(currentPlayer) == True and debug == False:
                    player_life -= 1
                    
                    for key in play_bullets:
                        play_bullets[key].AllDead()
                    
                    currentPlayer.xPos = 250
                    currentPlayer.yPos = 550
                    
                    if player_life <= 0:
                        ChangeScene(2)            
                    
                

        for key in play_monsters:
            for mon in play_monsters[key].pool:
                mon.Move()
        
        StageHUD()      
    elif scene == 2:
        Outro(event)
                
    currentBG.Move()


def Render():
    global gamePad
    global textManager
    global currentBG,currentPlayer
    global scene, stage
    global play_monsters, play_bullets, play_bosses, play_effects

    DrawObject(currentBG.shape, currentBG.xPos,currentBG.yPos)
    DrawObject(currentBG.shape, currentBG.xPosSub,currentBG.yPosSub)

    if scene == 0:
        IntroRender()
    elif scene == 1:
        if stage == 0:
            Stage00Render()
        elif stage == 1:
            Stage01Render()
        elif stage == 2:
            Stage02Render()

        # 출력
        # 총알 출력
        for key in play_bullets:
            for bul in play_bullets[key].pool:
                if bul.isAlive == True:
                    DrawObject(bul.rotateShape, bul.xPos, bul.yPos)
        
        # 몬스터 출력
        for key in play_monsters:
            for mon in play_monsters[key].pool:
                if mon.isAlive == True:
                    DrawObject(mon.shape, mon.xPos, mon.yPos)
        
        for key in play_bosses:
            for boss in play_bosses[key].pool:
                if boss.isAlive == True:
                    DrawObject(boss.shape, boss.xPos, boss.yPos)
                    
                
        if currentPlayer.shieldAlive == True:
            pygame.draw.circle(gamePad,(255,255,255),(currentPlayer.xPos + 20,currentPlayer.yPos + 24),36)
        DrawObject(currentPlayer.shape, currentPlayer.xPos, currentPlayer.yPos)
        
        # HUD
        StageHUDRender()
    elif scene == 2:
        OutroRender()
    
        
    textManager.RenderText()
    pass

#############################################
# Playing Game

def initGame():
    global gamePad, clock
    global game_timer, stage_timer
    
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption("몬스터를 찾아서")
    
    # Manager세팅
    managerSetting()
    
    readGameResource()
    saveResourceData()
    makePooling()
    readSoundResource()
    
    clock = pygame.time.Clock()
    
    game_timer = pygame.time.get_ticks()
    stage_timer = pygame.time.get_ticks()
    
def runGame():
    global gamePad, clock, mode, debug
    
    InitPlay()
    
    onGame = False
    while not onGame:
        event = pygame.event.poll()
        
        if event.type in [pygame.QUIT]:
            onGame = True
            
        if event.type in [pygame.KEYDOWN]:
            if event.key == pygame.K_ESCAPE:
                onGame = True
                
            if event.key == pygame.K_F1:
                ChangeScene(0)
            if event.key == pygame.K_F2:
                ChangeScene(1)
                ChangeStage(0)
            if event.key == pygame.K_F3:
                ChangeScene(1)
                ChangeStage(1)
            if event.key == pygame.K_F4:
                ChangeScene(1)
                ChangeStage(2)
            if event.key == pygame.K_F5:
                ChangeScene(2)
                
            if event.key == pygame.K_F9:
                textManager.fade = True
            
            if event.key == pygame.K_F6:
                debug = False       
            if event.key == pygame.K_F7:
                debug = True   
        
            if event.key == pygame.K_F10:
                textManager.fade = False
        
        # 활성화
        Update(event)
        
        pygame.draw.rect(gamePad, (0,0,0), [0,0,padWidth,padHeight])
       
        # 출력
        Render()
        
        pygame.display.update()
        clock.tick(static_frame)
        
        
            
    pygame.quit()
    sys.exit()

initGame()
runGame()