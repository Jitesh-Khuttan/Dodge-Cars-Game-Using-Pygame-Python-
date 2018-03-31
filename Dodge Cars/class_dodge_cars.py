import pygame,sys,os,time,random
from pygame.locals import *
class DodgeCars:

    def __init__(self,Display):
        self.Display = Display
        self.white = (255,255,255)
        self.red = (255,0,0)
        self.black = (0,0,0)
        self.width = 800
        self.height = 600
        self.GOImg = pygame.image.load('gameover.png')
        self.Pscore = []
    
       
    def Blit_Image(self,Image,x,y):
        self.Display.blit(Image,(x,y))

    def Opponent_Cars(self):
        self.Opp_Cars = [pygame.image.load("caropp1.png"),pygame.image.load("BLUECAR.png"),pygame.image.load("caropp3.png")]
        self.Opp_Car_HW = [(65,104),(64,106),(63,104)]
        self.Random_Number = random.randrange(0,3)
        self.Current_Car = self.Opp_Cars[self.Random_Number]
        self.Current_W,self.Current_H = self.Opp_Car_HW[self.Random_Number]
        return self.Current_Car, self.Current_W, self.Current_H

    def Opponent_Car_Coordinates(self,Road_r):
        self.OCar_Startx =  random.randrange(200,Road_r-64)
        self.OCar_Startylist = [-10,-20,-15,-12,-23]
        self.OCar_Starty = self.OCar_Startylist[random.randrange(0,4)]
        return self.OCar_Startx,self.OCar_Starty

    def Score(self,count):
        self.ScoreObj = pygame.font.Font("font.ttf",30)
        self.ScoreSurf = self.ScoreObj.render("Score:"+str(count),True,self.black)
        self.Display.blit(self.ScoreSurf,(0,0))

    def gameover(self,width,height):
        self.Display.blit(self.GOImg,(100,200))
        pygame.display.update()
        time.sleep(2)

    def Enter_Current_Score(self,c_score):
        Write = open("hiscore.txt",'a')
        Write.write('\n')
        Write.write(str(c_score))
        Write.close()

    def Previous_Score(self):
        Read = open("hiscore.txt",'r')
        self.score = Read.readlines()
        Read.close()
        self.score = [x.rstrip() for x in self.score]
        self.score = [int(x) for x in self.score]
        self.score.sort()
        DodgeCars.Show_Previous_Score(self,self.score[len(self.score)-1])

    def Show_Previous_Score(self,Pscore):
        self.DScoreObj = pygame.font.Font("font.ttf",20)
        self.DScoreSurf = self.DScoreObj.render("Previous High Score:"+str(Pscore),True,self.black)
        self.Display.blit(self.DScoreSurf,(0,575))

    def Display_Life(self,life):
        self.ScoreObj = pygame.font.Font("font.ttf",30)
        self.ScoreSurf = self.ScoreObj.render("Turns Left:"+str(life),True,self.black)
        self.Display.blit(self.ScoreSurf,(620,0))

    def lights(self,centerx,centery,radius,color):
        pygame.draw.circle(self.Display,color,(centerx,centery),radius)

    
        
        
                     
        

    
