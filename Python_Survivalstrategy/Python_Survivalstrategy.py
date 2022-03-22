# -*- coding: utf-8 -*-
import pygame as pg
from pygame.locals import *
import sys

def main():
    pg.init() # 初期化
    disp_w, disp_h = 800, 450 #画面サイズ横と縦
    pg.display.set_mode((disp_w,disp_h),0,32)
    screen = pg.display.get_surface()
    #screen = pygame.display.set_mode((disp_w,disp_h)) # ウィンドウサイズの指定
    pg.display.set_caption("Pygame Test") # ウィンドウの上の方に出てくる文字の指定

    while(True):
        screen.fill((255,255,224,)) # 背景色の指定。RGB指定

        #描画処理
        pg.draw.rect(screen, (255,0,0),(20,70,100,100))

        pg.display.update() # 画面更新

        for event in pg.event.get(): # 終了処理
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pg.quit()
                    sys.exit()

if __name__ == "__main__":
    main()