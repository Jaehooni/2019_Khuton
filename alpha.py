import pygame as pg
import sys
import time
import random
import datetime
pg.init()
screen_width = 800
screen_height = 600
size = [screen_width, screen_height]
FPS = 60
white = (255,255,255)
black = (0,0,0)
screen = pg.display.set_mode(size) # 창크기 설정
pg.display.set_caption("가제 : 방구석 여ㅡ행")
clock = pg.time.Clock()
money = 0
money_Add = 100

class Player():
    def __init__(self):
        self.health = 1
        self.intelligence = 1
        self.charm = 1
        self.money = 10
        self.maxmoney = 200000
        self.happiness = 0
        self.stamina = 100
        self.day = 1
        self.bat = 0
player = Player()


currentscene = 10 #현재 secne 번호
class Image(pg.sprite.Sprite): #rect는 sprite객체만 가능해서 만듦
    def __init__(self,fileroute,size,rect): #size랑 rect는 튜플
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(fileroute) #객체의 이미지를 설정함
        if size != -1:
            self.image = (pg.transform.scale(self.image,size)).convert_alpha()
        self.Rect = self.image.get_rect(topleft=rect)

intro_background = Image('./Image/Intro_background.png',(850,650),(-30,-15))
#---0---
main_background = Image('./Image/main_background.png',-1,(0,0))
go_alba = Image('./Image/go_alba.png',-1,(18,38))
go_stat = Image('./Image/go_stat.png',-1,(18,150))
go_travel = Image('./Image/go_travel.png',-1,(18,262))
go_game = Image('./Image/go_game.png',-1,(18,364))

#---1---
ui = Image('./Image/a_ui2.png',-1,(0,444)) 
stamina_gauge = Image('./Image/stamina_gauge.png',-1,(625,541)) #width=158 height=25

alba1_1 = Image('./Image/alba1_1.png',-1,(95,50)) 
alba1_2 = Image('./Image/alba1_2.png',-1,(95,175)) 
alba1_3 = Image('./Image/alba1_3.png',-1,(95,300))
backmove = Image('./Image/backmove.png',-1,(3,168))
frontmove = Image('./Image/frontmove.png',-1,(747,168))
#---2---
alba2_1 = Image('./Image/alba2_1.png',-1,(95,50)) 
alba2_2 = Image('./Image/alba2_2.png',-1,(95,175)) 
alba2_3 = Image('./Image/alba2_3.png',-1,(95,300))
#---3---
alba3_1 = Image('./Image/alba3_1.png',-1,(95,50)) 
alba3_2 = Image('./Image/alba3_2.png',-1,(95,175)) 
alba3_3 = Image('./Image/alba3_3.png',-1,(95,300))
#---4---
int1 = Image('./Image/int1.png',-1,(95,50))
int2 = Image('./Image/int2.png',-1,(95,175)) 
int3 = Image('./Image/int3.png',-1,(95,300))
#---5---
heal1 = Image('./Image/heal1.png',-1,(95,50))
heal2 = Image('./Image/heal2.png',-1,(95,175)) 
heal3 = Image('./Image/heal3.png',-1,(95,300))
#---6---
charm1 = Image('./Image/charm1.png',-1,(95,50))
charm2 = Image('./Image/charm2.png',-1,(95,175)) 
charm3 = Image('./Image/charm3.png',-1,(95,300))
#---8---
game_start = Image('./Image/game_start.png',-1,(295,50))
bat10000 = Image('./Image/10000bat.png',-1,(303,160))
bat1000000 = Image('./Image/1000000bat.png',-1,(310,250))
bat_clear = Image('./Image/bat_clear.png',-1,(310,330))

effect_list = [0 for i in range(13)]

scenelist = [] 
for i in range(0,50):
    scenelist.append([])
scenelist[0].extend([main_background,go_alba,go_stat,go_travel,go_game])
scenelist[1].extend([alba1_1,alba1_2,alba1_3,backmove,frontmove])
scenelist[2].extend([alba2_1,alba2_2,alba2_3,backmove,frontmove])
scenelist[3].extend([alba3_1,alba3_2,alba3_3,backmove])
scenelist[4].extend([int1,int2,int3,backmove,frontmove])
scenelist[5].extend([heal1,heal2,heal3,backmove,frontmove])
scenelist[6].extend([charm1,charm2,charm3,backmove])
scenelist[8].extend([game_start,backmove,bat10000,bat1000000,bat_clear])
scenelist[10].extend([intro_background]) #인트로

def fade_in_and_out():
    fade = 255
    fade_image = pg.Surface((800,600), pg.SRCALPHA)
    pg.draw.rect(fade_image, (0,0,0,10), fade_image.get_rect())
    ui_blit()   
    while fade > 0: 
        screen.blit(fade_image,fade_image.get_rect())
        fade -=1
        pg.display.update()
        pg.time.wait(1) 

def scene_change_blit(currentscene): 
    for sprite in scenelist[currentscene]:
        screen.blit(sprite.image,sprite.Rect)

def ui_blit(): #ui출력용,currentscene받아서 특정씬에는 안돌리게 하면됨
    screen.blit(ui.image,ui.Rect)
    screen.blit(stamina_gauge.image,stamina_gauge.Rect)

    realtime_Font = pg.font.Font(None, 25)
    text = realtime_Font.render(str(int(player.money)),True,(0,0,0))
    textrect = text.get_rect()
    textrect.topleft =(343,506)
    screen.blit(text,textrect)

    realtime_Font = pg.font.Font(None, 25)
    text = realtime_Font.render(str(player.day),True,(0,0,0))
    textrect = text.get_rect()
    textrect.topleft =(343,545)
    screen.blit(text,textrect)

    text = realtime_Font.render(str(player.health),True,(0,0,0))
    textrect = text.get_rect()
    textrect.topleft =(127,470)
    screen.blit(text,textrect)

    text = realtime_Font.render(str(player.intelligence),True,(0,0,0))
    textrect = text.get_rect()
    textrect.topleft =(127,518)
    screen.blit(text,textrect)

    text = realtime_Font.render(str(player.charm),True,(0,0,0))
    textrect = text.get_rect()
    textrect.topleft =(127,561)
    screen.blit(text,textrect)

    text = realtime_Font.render(str(player.maxmoney),True,(0,0,0))
    textrect = text.get_rect()
    textrect.topleft =(626,479)
    screen.blit(text,textrect)

def alba_lock(stat,min_stat):
    if stat >= min_stat:
        return True
    return False

def stamina_update(player,stamina_gauge): #스태미나 게이지 조절용
    if player.stamina <= 0:
        player.stamina = 0
    stamina_gauge.image = pg.transform.scale(stamina_gauge.image,(int(158*player.stamina/100),25))

passDay = False
def day_pass():
    global currentscene, passDay###변경점
    if player.stamina ==0:
        fade_in_and_out()###변경점 - fade 함수 위치를 바꿈
        currentscene = 0
        player.day += 1
        player.stamina = 100
        passDay = True
        pg.event.clear()

def money_clear():
    if player.money >= player.maxmoney:
        player.money = player.maxmoney       

def money_decline(player,decline): #돈없으면 업글못해
    if player.money < decline:
        return False
    else:
        player.money -= decline
        player.stamina -= 10
        return True
def processing_bar():#processing_bar
    lt = (100,480)
    wh = (600,25)
    percent = 0
    while percent<100:
        screen.fill((0,0,0))
        percent = percent%100+0.5
        r = pg.Rect((100,530), (wh[0]/100*percent, 25))
        pg.draw.rect(screen,(255,255,255),r)

    
        pg.display.update()
        pg.time.delay(1)
    pg.event.clear()

def day_event():
    global passDay

    if not passDay: return None

    pg.time.wait(3000)

    event_message = ""
    effect_message = ""
    lst = [0 for i in range(13)]
    event_num = random.randint(1, 200)

    if event_num == 1:
        event_message = "도둑이얏!!!!!!!!!!"
        effect_message = "현재 돈의 30% 강탈"
        lst[0]=1

    elif event_num == 200:
        event_message = "아니... 지금 몇시야?"
        effect_message = "하루 지나감"
        lst[1]=1

    elif 1 < event_num <= 26:
        event_message = "기운이 넘치는 날!"
        effect_message = "체력 수련 효과 2배"
        lst[2]=1

    elif 26 < event_num <= 51:
        event_message = "머리가 잘 돌아가는 날!"
        effect_message = "지능 수련 효과 2배"
        lst[3]=1

    elif 51 < event_num <= 76:
        event_message = "오늘은 화장이 잘 먹네~"
        effect_message = "매력 수련 효과 2배"
        lst[4]=1

    elif 76 < event_num <= 101:
        event_message = "운수 좋은 날!"
        effect_message = "오늘은 돈 획득량 1.25배"
        lst[5]=1

    elif 101 < event_num <= 121:
        event_message = "수련의 성과인가?!"
        effect_message = "현재 체력의 10%만큼 상승"
        lst[6]=1
        
    elif 121 < event_num <= 141:
        event_message = "공부의 성과인가?!"
        effect_message = "현재 지능의 10%만큼 상승"
        lst[7]=1
        
    elif 141 < event_num <= 161:
        event_message = "왜 이리 이뻐졌지?"
        effect_message = "현재 매력의 10%만큼 상승"
        lst[8]=1
        
    elif 161 < event_num <= 181:
        event_message = "하늘에서 돈이?!"
        effect_message = "현재 돈의 5%만큼 상승"
        lst[9]=1

    elif 181 < event_num <= 187:
        event_message = "노동자의 날"
        effect_message = "알바 못 함"
        lst[10]=1
        
    elif 187 < event_num <= 193:
        event_message = "요즘 성수긴가.. 자리가 없네.."
        effect_message = "여행 못 감"
        lst[11]=1
        
    elif 193 < event_num <= 199:
        event_message = "컨디션이 안 좋네..."
        effect_message = "소모 스테미나 1.6배 증가"
        lst[12]=1

    return (event_message, effect_message, lst)

def day_event_message(message):
    global passDay
    
    passDay = False
    sb = Image("./Image/speech_bubble.png",-1,(270,220))

    screen.blit(sb.image, sb.Rect)

    l = len(message)

    font = pg.font.Font("./Font/bmjua.ttf", 25-(l//10)*(l%10))
    text = font.render(message, True, (0,0,0))
    text_rect = text.get_rect()
    text_rect.center = (372, 272)

    screen.blit(text, text_rect)
    pg.display.update()

    pg.time.wait(2000)
    pg.event.clear()

#게임변수
def game():
    cup_image = pg.image.load("./Image/yabawi.png")
    bmjuaFont = pg.font.Font("./Font/bmjua.ttf", 30)
    posX = 315
    posY = 180
    distance = 250
    reward = random.randint(2,11)
    reward_text = bmjuaFont.render(str(reward)+"배", True, black)
    reward_pos = random.randint(-1,1)
    def open_cup(pos):
        reward_rect = reward_text.get_rect()
        reward_rect.center = (posX+reward_pos*distance+85, posY+170)
        i = -5
        while i < 300:
            i+=1
            if 100 < i < 200 :
                continue
            screen.fill(white)
            ui_blit()
            screen.blit(reward_text, reward_rect)
            dh = 150 - abs(150-i)
            screen.blit(cup_image, (posX-distance, posY-(pos==-1)*dh))
            screen.blit(cup_image, (posX, posY-(pos==0)*dh))
            screen.blit(cup_image, (posX+distance, posY-(pos==1)*dh))

            pg.display.update()
            pg.time.wait(1)
    open_cup(reward_pos)
    pg.time.wait(100)

    cup = list(range(3))
    for i in range(3):
        distance = 250
        while distance > -255:
            screen.fill(white)
            ui_blit()
            dw = 50-abs(distance)/5
            dh = int(posY-dw/2)
            con_cup_image = pg.transform.scale(cup_image,(int(171+0.85*dw), int(207+dw))).convert_alpha()
            screen.blit(con_cup_image, (posX-distance, dh))
            screen.blit(con_cup_image, (posX, dh))
            screen.blit(con_cup_image, (posX+distance, dh))
            pg.display.update()
            distance-=5
            pg.time.wait(1)

    distance = 250
    cup[0] = screen.blit(cup_image, (posX-distance, posY))
    cup[1] = screen.blit(cup_image, (posX, posY))
    cup[2] = screen.blit(cup_image, (posX+distance, posY))
    pg.event.clear()
    clicked = False
    clicked_pos = 0
    reward_pos = random.randint(-1,1)
    while not clicked:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                pos = pg.mouse.get_pos()

                for i in range(3):
                    if cup[i].collidepoint(pos):
                        clicked = True
                        clicked_pos = i-1
    open_cup(clicked_pos)
    pg.time.wait(100)

    if clicked_pos != reward_pos:
        open_cup(reward_pos)
    else:
        re_motion = [pg.image.load("./Image/reward1.png"), pg.image.load("./Image/reward2.png")]
        for i in range(2):
            re_motion[i] = pg.transform.scale(re_motion[i], (400,400))
        re_motion_pos = [(210,15),(210,30)]
        for i in range(6):
            screen.fill(white)
            ui_blit()
            screen.blit(re_motion[i%2], re_motion_pos[i%2])
            screen.blit(reward_text, (379,207))
            pg.display.update()
            pg.time.wait(500)
        player.money += reward * player.bat
betting_scene = False

while True:
    screen.fill(white)

    stamina_update(player,stamina_gauge)

    scene_change_blit(currentscene)

    ui_blit()

    temp = day_event()
    if temp != None:
        event_message, effect_message, effect_list = temp
        day_event_message(event_message)

    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            pos = pg.mouse.get_pos()
            if currentscene == 10:
                if intro_background.Rect.collidepoint(pos):
                    currentscene = 0
            elif currentscene == 0:
                if go_alba.Rect.collidepoint(pos):
                    currentscene = 1
                elif go_stat.Rect.collidepoint(pos):
                    currentscene = 4
                elif go_travel.Rect.collidepoint(pos):
                    currentscene = 19
                elif go_game.Rect.collidepoint(pos):
                    currentscene = 8
            elif currentscene == 1:
                if alba1_1.Rect.collidepoint(pos):
                    player.money += 5000 + 5000*0.25*effect_list[5]
                    player.stamina -= 10
                elif alba1_2.Rect.collidepoint(pos) and alba_lock(player.intelligence,10):
                    player.money += 100000 
                    player.stamina -= 10 
                elif alba1_3.Rect.collidepoint(pos) :
                    player.money += 2000000 * alba_lock(player.intelligence,50)
                    player.stamina -= 10 * alba_lock(player.intelligence,50)
                elif backmove.Rect.collidepoint(pos):
                    currentscene = 0
                elif frontmove.Rect.collidepoint(pos):
                    currentscene = 2
            elif currentscene == 2:
                if alba2_1.Rect.collidepoint(pos):
                    player.money += 10000
                    player.stamina -= 10
                elif alba2_2.Rect.collidepoint(pos):
                    player.money += 200000 * alba_lock(player.health,10)
                    player.stamina -= 10 * alba_lock(player.health,10)
                elif alba2_3.Rect.collidepoint(pos):
                    player.money += 10000000 * alba_lock(player.health,100)
                    player.stamina -= 10 * alba_lock(player.health,100)
                elif backmove.Rect.collidepoint(pos):
                    currentscene = 1
                elif frontmove.Rect.collidepoint(pos):
                    currentscene = 3
            elif currentscene == 3:
                if alba3_1.Rect.collidepoint(pos):
                    player.money += 5000
                    player.stamina -= 10
                elif alba3_2.Rect.collidepoint(pos):
                    player.money += 100000 * alba_lock(player.charm,10)
                    player.stamina -= 10 * alba_lock(player.charm,10)
                elif alba3_3.Rect.collidepoint(pos):
                    player.money += 2000000 * alba_lock(player.charm,50)
                    player.stamina -= 10 * alba_lock(player.charm,50)
                elif backmove.Rect.collidepoint(pos):
                    currentscene = 2
            elif currentscene == 4:
                if int1.Rect.collidepoint(pos):
                    player.intelligence += 1 * money_decline(player,30000)
                elif int2.Rect.collidepoint(pos):
                    player.intelligence += 5 * money_decline(player,1000000)
                elif int3.Rect.collidepoint(pos):
                    player.intelligence += 50 * money_decline(player,10000000)
                elif backmove.Rect.collidepoint(pos):
                    currentscene = 0   
                elif frontmove.Rect.collidepoint(pos):
                    currentscene = 5 
            elif currentscene == 5:
                if heal1.Rect.collidepoint(pos):
                    player.health += 1 * money_decline(player,50000)
                elif heal2.Rect.collidepoint(pos):
                    player.health += 5 * money_decline(player,2500000)
                elif heal3.Rect.collidepoint(pos):
                    player.health += 10 * money_decline(player,50000000)
                elif backmove.Rect.collidepoint(pos):
                    currentscene = 4   
                elif frontmove.Rect.collidepoint(pos):
                    currentscene = 6 
            elif currentscene == 6:
                if int1.Rect.collidepoint(pos):
                    player.charm += 1 * money_decline(player,30000)
                elif int2.Rect.collidepoint(pos):
                    player.charm += 5 * money_decline(player,1000000)
                elif int3.Rect.collidepoint(pos):
                    player.charm += 50 * money_decline(player,10000000)
                elif backmove.Rect.collidepoint(pos):
                    currentscene = 5   
            elif currentscene == 8:
                betting_scene = True
                if game_start.Rect.collidepoint(pos):
                    if not(player.money < player.bat) and not(player.bat==0):
                        player.money -= player.bat
                        game()       
                elif backmove.Rect.collidepoint(pos):
                    currentscene = 0
                    betting_scene = False
                elif bat10000.Rect.collidepoint(pos):
                    player.bat += 10000
                elif bat1000000.Rect.collidepoint(pos):
                    player.bat += 1000000
                elif bat_clear.Rect.collidepoint(pos):
                    player.bat = 0
                
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    money_clear() #최대보유량 넘으면 자름
    day_pass() #

    #test용
    realtime_Font = pg.font.Font(None, 25)
    text = realtime_Font.render('cursor = '+str(pg.mouse.get_pos()),True,(0,0,0))
    textrect = text.get_rect()
    textrect.topleft =(0,0)
    screen.blit(text,textrect)

    text = realtime_Font.render('scene = '+str(currentscene),True,(0,0,0))
    textrect = text.get_rect()
    textrect.topleft =(700,0)
    screen.blit(text,textrect)

    if betting_scene:
        realtime_Font = pg.font.Font(None, 25)
        text = realtime_Font.render('betting = '+str(player.bat),True,(0,0,0))
        textrect = text.get_rect()
        textrect.topleft =(555,255)
        screen.blit(text,textrect)

    pg.display.update()
    clock.tick(FPS)