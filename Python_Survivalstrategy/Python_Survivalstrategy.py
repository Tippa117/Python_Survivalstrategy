# -*- coding: utf-8 -*-
import pygame as pg
from pygame.locals import *
import sys

#class Creature:
#    """
#    """
#    def __init__(self):
#        self.born_x = 20
#        self.born_y = 20
#        self,born_size_x = 50
#        self.born_size_y = 50
    
#    def create(self):
#        pg.Rect(self.born_x, self.born_y, self.born_size_x, self.born_size_y)

def main():
    pg.init() # ������
    disp_w, disp_h = 800, 450 # ��ʃT�C�Y���Əc
    pg.display.set_mode((disp_w,disp_h),0,32)
    screen = pg.display.get_surface()
    # screen = pygame.display.set_mode((disp_w,disp_h)) # �E�B���h�E�T�C�Y�̎w��
    pg.display.set_caption("Pygame Test") # �E�B���h�E�̏�̕��ɏo�Ă��镶���̎w��
    # ��ʍX�V���x
    FPS = 30 
    fpsClock = pg.time.Clock()

    # �������I�u�W�F�N�g����
    #creature1 = Creature()
    creature1 = pg.Rect(20,20,50,50)

    x = 50
    dx = 10

    while(True):
        screen.fill((255,255,224,)) # �w�i�F�̎w��BRGB�w��

        #�`�揈��
        pg.draw.rect(screen, (255,0,0),creature1)
        pg.display.update() # ��ʍX�V
        fpsClock.tick(FPS)

        if creature1.x >= (disp_w-50) or creature1.x <= 0:
            dx = -dx
        
        creature1.x += dx
        
        for event in pg.event.get(): # �I������
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pg.quit()
                    sys.exit()

if __name__ == "__main__":
    main()