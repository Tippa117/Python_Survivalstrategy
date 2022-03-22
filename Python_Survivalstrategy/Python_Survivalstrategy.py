# -*- coding: utf-8 -*-
import pygame as pg
from pygame.locals import *
import sys

def main():
    pg.init() # ������
    disp_w, disp_h = 800, 450 #��ʃT�C�Y���Əc
    pg.display.set_mode((disp_w,disp_h),0,32)
    screen = pg.display.get_surface()
    #screen = pygame.display.set_mode((disp_w,disp_h)) # �E�B���h�E�T�C�Y�̎w��
    pg.display.set_caption("Pygame Test") # �E�B���h�E�̏�̕��ɏo�Ă��镶���̎w��

    while(True):
        screen.fill((255,255,224,)) # �w�i�F�̎w��BRGB�w��

        #�`�揈��
        pg.draw.rect(screen, (255,0,0),(20,70,100,100))

        pg.display.update() # ��ʍX�V

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