# -*- coding: shift-jis -*-
# モジュールインポート
import pygame

# pygame初期化
pygame.init()

## 初期設定
# ウィンドウのサイズ
WIDTH = 500
HEIGHT = 500
# アニメーション更新速度
FPS = 30

def quit():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.event.clear()
      return True
  return False

def clear(screen):
  screen.fill((100, 100, 100))

def update(fps):
  pygame.display.update()
  pygame.time.Clock().tick(fps)

import math

def ngon(screen, color = (255, 255, 255), gx = 100, gy = 100, gr = 100, n = 5, rot =0):
  points = [(gr*math.cos(th) + gx, gr*math.sin(th) + gy) for th in [i*2*math.pi /n - math.pi/2 + rot for i in range(n)]]
  pygame.draw.polygon(screen, color = color, points = points, width = 1)

## 人工生物基盤
import random

XMIN, XMAX = -1.5, 1.5
YMIN, YMAX = -1.5, 1.5

class Entity:

  def __init__(self, hue=0, sat=0, brightness=1, radius=0.1):
      self.hue = hue # [0, 1]色相
      self.sat = sat # [0, 1]彩度saturation
      self.brightness = brightness # [0, 1]明度
      self._color = pygame.Color(0)
      self._updateColor()
      self.x = random.uniform(-1, 1)
      self.y = random.uniform(-1, 1)
      self.radius = radius
      self.alive = True
  
  def draw(self, screen, color, gx, gy, gr):
    ngon(screen, color, gx, gy, gr, 4)

  def _updateColor(self):
    self._color.hsva = 360*self.hue, 100*self.sat, 100*self.brightness, 100

  def update(self, screen):
    if self.alive:
      self._updateColor()
      # Processing の map関数が便利なので実装をコピー
      def map(value, istart, istop, ostart, ostop):
        return ostart + (ostop - ostart)*((value - istart)/(istop - istart))
        gx = map(self.x, XMIN, XMAX, 0, WIDTH)
        gy = map(self.y, YMIN, YMAX, HEIGHT, 0)
        gr = map(self.radius, 0, XMAX, 0, WIDTH/2)
        self.draw(screen, self._color, gx, gy, gr)
  
  def collideWith(self, other) -> bool:
    dx = self.x - other.x
    dy = self.y - other.y
    rr = self.radius + other.radius
    return dx*dx + dy*dy < rr*rr

## 基盤テスト用
class C(Entity):

  def __init__(self, hue, omega):
    super().__init__(hue=hue, sat=1)
    self._theta = 0
    self.omega = omega

  def update(self, screen):
    self.x = math.cos(self._theta)
    self.y = math.sin(self._theta)
    self._theta += self.omega
    super().update(screen)

class B(Entity):

  def __init__(self, hue, omega):
    super().__init__(hue=hue, sat=1)
    self._theta = 0
    self.omega = omega

  def update(self, screen):
    self.radius = 1.0*math.fabs(math.cos(self._theta))
    self._theta += self.omega
    super().update(screen)

cs = [C(hue=0, omega=0.1), C(hue=0.2, omega=0.2)]
bs = [B(hue=0.4, omega=0.1)]
entities = cs + bs

screen = pygame.display.set_mode((WIDTH, HEIGHT))

while not quit():
  clear(screen)
  for e in entities:
    e.update(screen)
  update(FPS)

pygame.display.quit()

print("人工生命基盤テスト done")

#if __name__ == "__main__":
#    main()