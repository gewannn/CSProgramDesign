import os
import math
#我下了pygame这几行就注释吧try:
    #import pygame
#except:
    #os.system("pip install pygame -i https://pypi.tuna.tsinghua.edu.cn/simple")
import pygame
from pygame.locals import *

class Brush():
    def __init__(self,screen):
        self.screen = screen
        self.color = (0,0,0)
        self.size = 1
        self.drawing = False
        self.last_pos = None

    def start_draw(self,pos):
        self.drawing = True
        self.last_pos = None

    def end_draw(self):
        self.drawing = False

    def draw(self,pos):
        if self.drawing:
            for p in self.get_points(pos):
                pygame.draw.circle(self.screen,self.color,p,self.size)
            self.last_pos = pos

    def get_points(self,pos):
        if self.last_pos is None:
            return []
        points = [ (self.last_pos[0],self.last_pos[1]) ]
        len_x = pos[0] - self.last_pos[0]
        len_y = pos[1] - self.last_pos[1]
        length = math.sqrt(len_x ** 2 + len_y ** 2)
        step_x = len_x / length
        step_y = len_y / length
        for _ in range (int(length)):
            points.append((points[-1][0] + step_x,points[-1][1] + step_y))
        points = map(lambda x:(int(0.5+x[0]),int(0.5+x[1])),points)
        return list(set(points))

class Painter():
    def __init__(self):
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("DrawPad")
        self.clock = pygame.time.Clock()
        self.brush = Brush(self.screen)

    def run(self):
        self.screen.fill((255,255,255))
        while True:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    return
                elif event.type ==KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.screen.fill((255,255,255))
                elif event.type == MOUSEBUTTONDOWN:
                    self.brush.start_draw(event.pos)
                elif event.type == MOUSEMOTION:
                    self.brush.draw(event.pos)
                elif event.type == MOUSEBUTTONUP:
                    self.brush.end_draw()
            pygame.display.update()

if __name__ == "__main__":
    app = Painter()
    app.run()