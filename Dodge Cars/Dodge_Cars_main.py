import pygame,sys,time,random
from pygame.locals import *
from class_dodge_cars import *
pygame.init()

width=800 #wIDTH OF THE SCREEN
height=600 #HEIGHT OF THE SCREEEN
FPS=40 #FRAME RATE
white = (255,255,255)
l_red = (255,0,0)
red = (150,0,0)
l_green = (0,255,0)
green = (0,150,0)
yellow = (255,229,10)
l_yellow =(212,255,10)
black = (0,0,0)
roadcolor = (47,47,47)

Display = pygame.display.set_mode((width,height)) #DISPLAY SURFACE OBJECT
pygame.display.set_caption("The Car Racing") #CAPTION
clock=pygame.time.Clock() #TIME OBJECT
CarImg = pygame.image.load("car.png") #LOADING CAR IMAGE
RoadImg1 = pygame.image.load("road1.jpg") #LOADING ROAD IMAGE
TreeImg1 = pygame.image.load("longtree1.jpg") #LOADING TREE IMAGE
TreeImg2 = pygame.image.load("longtree2.jpg")
Bugatti = pygame.image.load("Bugatti.png")
GameIcon = pygame.image.load("GameIcon.png")
pygame.display.set_icon(GameIcon)
life = 2 #LIFE OF THE GAMER
Previous_Score = DodgeCars(Display)
Previous_Score.Previous_Score()
EndGame = False
GamePaused = False

Just_In = DodgeCars(Display)
def Entry_Screen():
    
    Entry = True
    Display.fill(white)
    while Entry:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        Color_Tuple = (red,yellow,green)
        Color = Color_Tuple[random.randint(0,2)]
        display_message("Dodge Cars",70,400,100,Color)
        display_message("Made By: Jitesh Khuttan",20,650,20,black)
        Just_In.Blit_Image(Bugatti,175,200)
        Interactive(250,450,20,green,l_green,"Start!")
        Interactive(400,450,20,yellow,l_yellow,"Ready!")
        Interactive(550,450,20,red,l_red,"Quit!")
        
        pygame.display.update()
        clock.tick(30)
mousex,mousey = 0,0
clickx,clixky = 0,0
MouseClicked = False
def Interactive(centerx,centery,radius,icolor,acolor,message):
    global mousex,mousey
    global clickx,clicky
    global MouseClicked 
    for event in pygame.event.get():
        if event.type == MOUSEMOTION:
            mousex,mousey = event.pos
        elif event.type == MOUSEBUTTONDOWN:
            clickx,clicky = event.pos
            MouseClicked = True
        elif event.type == MOUSEBUTTONUP:
            clickx,clicky = event.pos
            MouseClicked = True
            
    #print (mousex,mousey)
    left_x = centerx - radius
    left_y = centery - radius
    width_c = height_c = 2*radius #Width And Height of rect bounding circle
    if mousex > left_x and mousex < (left_x + width_c) and mousey > left_y and mousey < (left_y + height_c):
        Just_In.lights(centerx,centery,radius,acolor)
        display_message(message,20,centerx,centery+50,black)
        if clickx > 230 and clickx < (230 + 40) and clicky > 430 and clicky < (430 + 40) and MouseClicked == True:
            MouseClicked = False
            global life
            global GamePaused
            if life == -1:
                life = 2
                Enter_Game()
                main()
            elif GamePaused == True:
                GamePaused = False
                pygame.mixer.music.unpause()
            else:
                Enter_Game()
                main()
        elif clickx > 530 and clickx < (530 + 40) and clicky > 430 and clicky < (430 + 40) and MouseClicked == True:
            pygame.quit()
            sys.exit()
    else:
        Just_In.lights(centerx,centery,radius,icolor)
        display_message(message,20,centerx,centery+50,black)

def crash(OCar_Startx,OCar_Starty,count):
    Enter_Current_Score = DodgeCars(Display)
    SoundObj = pygame.mixer.Sound('shot.wav')
    SoundObj.play()
    explosion(OCar_Startx,OCar_Starty)
    Enter_Current_Score.Enter_Current_Score(count)
    #display_message("EXPLODED",100,width/2,height/2,black)
    life_count()
    time.sleep(2)
    main()

def explosion(OCar_Startx,OCar_Starty):
    ExpImg = pygame.image.load('explosion.gif')
    Display.blit(ExpImg,(OCar_Startx,OCar_Starty))
    pygame.display.update()

def display_message(text,size,x,y,color):
    TextObj = pygame.font.Font("font.ttf",size)
    TextSurf = TextObj.render(text,True,color)
    RectSurf = TextSurf.get_rect()
    RectSurf.center=(x,y)
    Display.blit(TextSurf, RectSurf)
    pygame.display.update()

def life_count():
    global life
    life -= 1
    if life == -1:
        GameOver = DodgeCars(Display)
        GameOver.gameover(width,height)
        while True:
            Restart_Page()

def Restart_Page():
    Interactive(250,450,20,green,l_green,"Restart!")
    Interactive(550,450,20,red,l_red,"Quit!")
    pygame.display.update()
    clock.tick(15)
    
def Pause():
    global GamePaused
    pygame.mixer.music.pause()
    GamePaused = True
    while GamePaused:
        display_message("PAUSED",100,width/2,height/2,black)
        Interactive(250,450,20,green,l_green,"Continue!")
        Interactive(550,450,20,red,l_red,"Quit!")
        pygame.display.update()
        clock.tick(30)

def Enter_Game():
    Display.fill(roadcolor)
    Roadx = 200
    Roady = -580
    Treex1 = 0
    Treey1 = 0
    Treex2 = 605
    Treey2 = 0
    Start_Number = DodgeCars(Display)
    At_Start_Time = 3
    while At_Start_Time >=0:
        Start_Number.Blit_Image(RoadImg1,Roadx,Roady) #CALLING FUNCTION TO BLIT ROAD IMAGE
        Start_Number.Blit_Image(TreeImg1,Treex1,Treey1) #CALLING FUNCTION TO BLIT TREE IMAGE
        Start_Number.Blit_Image(TreeImg2,Treex2,Treey2) #CALLING FUNCTION TO BLIT TREE IMAGE
        if At_Start_Time == 0:
            display_message("GO!",150,width/2,height/2,black)
        else:
            display_message(str(At_Start_Time),150,width/2,height/2,black)
        At_Start_Time -= 1
        pygame.display.update()
        clock.tick(1)
    
    

        
'''------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
#pygame.mixer.music.load('gamemusic.mp3')
#pygame.mixer.music.play(-1,0.0)
def main():
    Obj1 = DodgeCars(Display)
    Obj2 = DodgeCars(Display)
    OBJECTS = (Obj1,Obj2) #TUPLE OF OBJECTS
    Life = DodgeCars(Display)#OBJECT TO DISPLAY LIFE
    Carx = width*0.4 #X-COORDINATE OF CAR
    Cary = height*0.8 #Y-COORDINATE OF CAR
    Car_Width=64 #WIDTH OF CAR
    Car_Height = 104 #Heigth Of The Car
    Previous_Score = DodgeCars(Display)
    Road_Count = 1

        
    x_change=0 #CHANGE IN POSTION OF CAR MOVING RIGHT OR LEFT
    y_change=0
    '''thing_w = 50
    thing_h = 50
    thing_startx =  random.randrange(200,Road_r-thing_w)
    thing_starty = -500
    color = black
    thing_speed=7'''
    Road_r = 600 #RightEnd
    Current_Car1,OCar_w1,OCar_h1 = OBJECTS[0].Opponent_Cars()
    OCar_Startx1,OCar_Starty1 = OBJECTS[0].Opponent_Car_Coordinates(Road_r)
    OCar_Speed1 = 7
    OCar_Speed2 =7
    OCar_Speed3 = 9
    OCARSPEEDS = [OCar_Speed1,OCar_Speed2,OCar_Speed3] #INITIALISING SPEED OF THE CARS
    Add_Speed1 = OCARSPEEDS[0]
    Add_Speed2 = OCARSPEEDS[1]
    Add_Speed3 = OCARSPEEDS[2]
    
    OCARSPEED_UP = 15 #SPEED WHEN UPPER ARROW KEY IS PRESSED
    Second_Car_First_Time = 1
    '''COORDINATES FOR SETTING THE IMAGE OF ROAD AND SIDE TREES'''
    Roadx = 200
    Roady = -580
    Treex1 = 0
    Treey1 = -580
    Treex2 = 605
    Treey2 = -580
    MoveRoad = 5
    MoveTree1 = 5
    MoveTree2 = 5
    TempTreeSpeed1 = 5
    TempTreeSpeed2 = 5
    TempRoadSpeed = 5
    count = 0 #SCORE
    Up_Press_Count = 1
    
    global GamePaused
    if GamePaused == False:
        while not EndGame:
            Display.fill(roadcolor)
            Roady += MoveRoad
            Treey1 += MoveTree1
            Treey2 += MoveTree2
            if Roady > 10:
                Roady = -580
            if Treey1 > 10:
                Treey1 = -580
                Treey2 = -580
            OBJECTS[0].Blit_Image(RoadImg1,Roadx,Roady) #CALLING FUNCTION TO BLIT ROAD IMAGE
            OBJECTS[0].Blit_Image(TreeImg1,Treex1,Treey1) #CALLING FUNCTION TO BLIT TREE IMAGE
            OBJECTS[0].Blit_Image(TreeImg2,Treex2,Treey2) #CALLING FUNCTION TO BLIT TREE IMAGE

            for event in pygame.event.get(): #RETURNING THE LIST OF THE OCCURED EVENTS
                if event.type==pygame.QUIT: #CHECKING FOR QUIT
                    pygame.quit()
                    sys.exit()
                if event.type == KEYUP: #WHAT TO DO WHEN KEY IS RELEASED
                    if event.key == K_ESCAPE: #IF KEY RELEASED WAS ESCAPE KEY
                        pygame.quit()
                        sys.exit()
                    elif event.key == K_p:
                        Pause()
                        
                if event.type == pygame.KEYDOWN: #WHAT TO DO IF KEY WAS PRESSED DOWN
                    
                    if event.key == pygame.K_LEFT: #IF KEY WAS LEFT ARROW KEY
                        x_change= -6
                        
                    elif event.key == pygame.K_RIGHT: #IF KEY WAS RIGHT ARROW KEY
                        x_change = 6
                        
                    elif event.key == pygame.K_UP:
                        if Up_Press_Count == 1:
                            Cary += -15
                        Up_Press_Count += 1
                        MoveRoad = 10
                        MoveTree1 = 10
                        MoveTree2 = 10
                        Add_Speed1 = 14
                        if count >= 10:
                            Add_Speed2 = 17
##                        if count >= 20:
##                            Add_Speed3 += 3
                        
                    elif event.key == pygame.K_DOWN:
                        y_change = 5

    
                elif event.type == pygame.KEYUP: #WHEN KEY IS RELEASED
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN:
                        x_change=0
                        y_change=0
                    elif event.key == pygame.K_UP:
                        if Up_Press_Count > 1:
                            Cary += 15
                            Up_Press_Count = 1
                        Add_Speed1 = OCARSPEEDS[0]
                        MoveRoad = TempRoadSpeed
                        MoveTree1 = TempTreeSpeed1 
                        MoveTree2 = TempTreeSpeed2
                        if count >= 10:
                            Add_Speed2 = OCARSPEEDS[1]
##                        if count >= 20:
##                            Add_Speed3 = OCARSPEEDS[2]
            Carx += x_change #CHANGING COORDINATE OF THE CAR
            #Cary+=y_change
            OCar_Starty1 += Add_Speed1 #MOVING THE OPPONENT CAR ALONG Y-AXIS
            OBJECTS[0].Blit_Image(CarImg,Carx,Cary) #BLITING IMAGE OF CAR TO CHANGED COORDINATE
            OBJECTS[0].Blit_Image(Current_Car1,OCar_Startx1,OCar_Starty1) #BLITING THE IMAGE OF OPPONENT CAR TO NEW COORDNATE
            if count >= 10:
                OCar_Starty2 += Add_Speed2
                OBJECTS[0].Blit_Image(Current_Car2,OCar_Startx2,OCar_Starty2)
##            elif count > 20:
##                OCar_Starty3 += Add_Speed3
##                OBJECTS[0].Blit_Image(Current_Car3,OCar_Startx3,OCar_Starty3)
            
            OBJECTS[0].Score(count) #Displaying Score
            Previous_Score.Previous_Score() #DISPLAYING PREVIOUS SCORE
            Life.Display_Life(life) #DISPLAYING LIFE OF THE PLAYER
            
            if Carx < 200 or Carx > (width-Car_Width-200) or (Cary + Car_Height)> height or Cary < 0: #TESTING: IF CAR TOUCHED THE SIDES OF THE ROAD
                crash(Carx,Cary,count) #CALLING CRASH()
            
            if OCar_Starty1 > height: #IF OPPONENT CAR CROSSES THE BOTTOM SCREEN
                if count > 10:
                    Current_Car1,OCar_w1,OCar_h1 = OBJECTS[0].Opponent_Cars()
                    OCar_Startx1,OCar_Starty1 = OBJECTS[0].Opponent_Car_Coordinates(Road_r)
                    while (OCar_Startx1 > OCar_Startx2 and OCar_Startx1 < OCar_Startx2 + OCar_w2): 
                        Current_Car1,OCar_w1,OCar_h1 = OBJECTS[0].Opponent_Cars()
                        OCar_Startx1,OCar_Starty1 = OBJECTS[0].Opponent_Car_Coordinates(Road_r)
                else:
                    Current_Car1,OCar_w1,OCar_h1 = OBJECTS[0].Opponent_Cars()
                    OCar_Startx1,OCar_Starty1 = OBJECTS[0].Opponent_Car_Coordinates(Road_r)
                count += 1
##                Add_Speed1 += 0.5
                OCARSPEEDS[0] += 0.005
                TempRoadSpeed += 0.004
                MoveRoad += 0.004
                MoveTree1 += 0.004
                MoveTree2 += 0.004
                TempTreeSpeed1 += 0.004
                TempTreeSpeed2 += 0.004
                if count == 10:
                    Current_Car2,OCar_w2,OCar_h2 = OBJECTS[0].Opponent_Cars()
                    OCar_Startx2,OCar_Starty2 = OBJECTS[0].Opponent_Car_Coordinates(Road_r)
                    
            if count > 10:
                if OCar_Starty2 > height:
                    Current_Car2,OCar_w2,OCar_h2 = OBJECTS[0].Opponent_Cars()
                    OCar_Startx2,OCar_Starty2 = OBJECTS[0].Opponent_Car_Coordinates(Road_r)
                    while(OCar_Startx2 > OCar_Startx1 and OCar_Startx2 < OCar_Startx1 + OCar_w1):
                        OCar_Startx2,OCar_Starty2 = OBJECTS[0].Opponent_Car_Coordinates(Road_r)
##                  Add_Speed2 += 0.5
                    if Second_Car_First_Time == 1:
                        OCARSPEEDS[1] += 0.015
                        Second_Car_First_Time += 1
                    OCARSPEEDS[1] += 0.006
                    count += 1
##                if count == 20:
##                    Current_Car3,OCar_w3,OCar_h3 = OBJECTS[0].Opponent_Cars()
##                    OCar_Startx3,OCar_Starty3 = OBJECTS[0].Opponent_Car_Coordinates(Road_r)
##
##            if count > 20:
##                if OCar_Starty3 > height:
##                    Current_Car3,OCar_w3,OCar_h3 = OBJECTS[0].Opponent_Cars()
##                    OCar_Startx3,OCar_Starty3 = OBJECTS[0].Opponent_Car_Coordinates(Road_r)
##                    Add_Speed3 += 0.5
##                    OCARSPEEDS[2] += 0.5
##                    count += 1


                
            if Cary < OCar_Starty1 + OCar_h1 and (Cary+Car_Height) > OCar_Starty1: #IF Y-COORDINATES CROSS OVER
                if (Carx > OCar_Startx1 and Carx < OCar_Startx1 +OCar_w1) or (Carx + Car_Width > OCar_Startx1 and Carx + Car_Width < OCar_Startx1 + OCar_w1):
                    crash(Carx,Cary-20,count)
            if count > 10 and count <= 20:
                if Cary < OCar_Starty2 + OCar_h2 and (Cary+Car_Height) > OCar_Starty2: #IF Y-COORDINATES CROSS OVER
                    if (Carx > OCar_Startx2 and Carx < OCar_Startx2 +OCar_w2) or (Carx + Car_Width > OCar_Startx2 and Carx + Car_Width < OCar_Startx2 + OCar_w2):
                        crash(Carx,Cary-20,count)
##            if count > 20:
##                if Cary < OCar_Starty3 + OCar_h3 and (Cary+Car_Height) > OCar_Starty3: #IF Y-COORDINATES CROSS OVER
##                    if (Carx > OCar_Startx3 and Carx < OCar_Startx3 +OCar_w3) or (Carx + Car_Width > OCar_Startx3 and Carx + Car_Width < OCar_Startx3 + OCar_w3):
##                        crash(Carx,Cary-20,count)
                
            
            
            pygame.display.update()
            clock.tick(FPS)
Entry_Screen()
pygame.quit()
sys.exit()

    

                
