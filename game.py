import pygame
import sys

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
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.blit(self.background,(0,0))       
            self.screen.blit(self.slingshot1,(610,750))
            self.screen.blit(self.slingshot2,(1250,750))
            pygame.display.update()
            self.clock.tick(60)
AngryBirds().run()