import pygame
import sys
import random

class AngryBirds:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((1920,1080))
        self.clock=pygame.time.Clock()
        self.background=pygame.image.load('assets/background/background.png')
        self.background=pygame.transform.scale(self.background,(1920,1080))
        self.slingshot1=pygame.image.load('assets/background/slingshot1.png')
        self.slingshot1=pygame.transform.scale(self.slingshot1,(60,108))
        self.slingshot2=pygame.image.load('assets/background/slingshot2.png')
        self.slingshot2=pygame.transform.scale(self.slingshot2,(60,108))
        self.red=pygame.image.load('assets/birds/Red/Red_atlaunch.png')
        self.red=pygame.transform.scale(self.red,(20,20))
        self.ready1=True
        self.ready2=True
        self.launchPos1=pygame.Rect(609,739,50,50)
        self.launchPos2=pygame.Rect(1261,739,50,50)
        self.birdx1=634
        self.birdy1=764
        self.birdx2=1286
        self.birdy2=764
        self.indrag=False
        self.inflight=False
        self.initialVelocity=0
        self.sinx=0
        self.cosx=0
        self.vx=0
        self.vy=0
    def run1(self):
        while self.ready1:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif (event.type==pygame.MOUSEBUTTONDOWN):
                    if(self.launchPos1.collidepoint(pygame.mouse.get_pos())):
                        self.indrag=True
                elif (event.type==pygame.MOUSEBUTTONUP and self.indrag==True):
                    self.indrag=False
                    self.inflight=True
                    self.distance1=(((self.birdx1-634)**2)+((self.birdy1-764)**2))**0.5
                    self.sinx=(self.birdy1-764)/self.distance1
                    self.cosx=(634-self.birdx1)/self.distance1
                    self.initialVelocity=self.distance1*2/3
                    self.vx=self.initialVelocity*self.cosx
                    self.vy=self.initialVelocity*self.sinx
            self.screen.blit(self.background,(0,0))      
            self.screen.blit(self.slingshot1,(610,750))
            self.screen.blit(self.slingshot2,(1250,750))
            pygame.draw.circle(self.screen,(48,25,7),(642,766),4)
            pygame.draw.circle(self.screen,(48,25,7),(1278,766),4)
            pygame.draw.circle(self.screen,(48,25,7),(623,771),5)
            pygame.draw.circle(self.screen,(48,25,7),(1297,771),5)
            if(self.indrag==True):  
                self.birdx1,self.birdy1=pygame.mouse.get_pos()
                self.distance1=(((self.birdx1-634)**2)+((self.birdy1-764)**2))**0.5
                if self.distance1>200:
                    self.birdx1=634+(200*(self.birdx1-634)/self.distance1)
                    self.birdy1=764+(200*(self.birdy1-764)/self.distance1)
                pygame.draw.line(self.screen,(48,25,7),(642,766),(self.birdx1,self.birdy1),4)
                pygame.draw.line(self.screen,(48,25,7),(623,771),(self.birdx1-5,self.birdy1+5),4)
            elif (self.inflight==True):
                self.birdx1=self.birdx1+self.vx/5
                self.birdy1=self.birdy1-self.vy/5
                self.vy=self.vy-2
                if(self.birdy1>858 and (self.birdy1+self.vy/5)<858):
                    self.vy=self.vy*(-0.75)
            self.screen.blit(self.red,(self.birdx1-10,self.birdy1-10))
            pygame.display.update()
            self.clock.tick(60)
    def run2(self):
        while self.ready2:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif (event.type==pygame.MOUSEBUTTONDOWN):
                    if(self.launchPos2.collidepoint(pygame.mouse.get_pos())):
                        self.indrag=True
                elif (event.type==pygame.MOUSEBUTTONUP and self.indrag==True):
                    self.indrag=False
                    self.inflight=True
                    self.distance2=(((self.birdx2-1286)**2)+((self.birdy2-764)**2))**0.5
                    self.sinx=(self.birdy2-764)/self.distance2
                    self.cosx=(1286-self.birdx2)/self.distance2
                    self.initialVelocity=self.distance2*2/3
                    self.vx=self.initialVelocity*self.cosx
                    self.vy=self.initialVelocity*self.sinx
            self.screen.blit(self.background,(0,0))      
            self.screen.blit(self.slingshot1,(610,750))
            self.screen.blit(self.slingshot2,(1250,750))
            pygame.draw.circle(self.screen,(48,25,7),(642,766),4)
            pygame.draw.circle(self.screen,(48,25,7),(1278,766),4)
            pygame.draw.circle(self.screen,(48,25,7),(623,771),5)
            pygame.draw.circle(self.screen,(48,25,7),(1297,771),5)
            if(self.indrag==True):  
                self.birdx2,self.birdy2=pygame.mouse.get_pos()
                self.distance2=(((self.birdx2-1286)**2)+((self.birdy2-764)**2))**0.5
                if self.distance2>200:
                    self.birdx2=1286+(200*(self.birdx2-1286)/self.distance2)
                    self.birdy2=764+(200*(self.birdy2-764)/self.distance2)
                pygame.draw.line(self.screen,(48,25,7),(1278,766),(self.birdx2,self.birdy2),4)
                pygame.draw.line(self.screen,(48,25,7),(1297,771),(self.birdx2-5,self.birdy2+5),4)
            elif (self.inflight==True):
                self.birdx2=self.birdx2+self.vx/5
                self.birdy2=self.birdy2-self.vy/5
                self.vy=self.vy-2
                if(self.birdy2>858 and (self.birdy2+self.vy/5)<858):
                    self.vy=self.vy*(-0.75)
            self.screen.blit(self.red,(self.birdx2-10,self.birdy2-10))
            pygame.display.update()
            self.clock.tick(60)        
AngryBirds().run1()