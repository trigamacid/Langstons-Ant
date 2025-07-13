import pygame


class turtle:
     def __init__(self, x_pos, y_pos, direction, Hue):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.direction = direction 
        self.Hue = Hue
     def checkEdge(self):
         self.x_pos = self.x_pos % sX
         self.y_pos = self.y_pos % sY
     def forward(self, step):
          self.step = step   
          if self.direction == 0:
               self.x_pos += self.step
          if self.direction == 1:
               self.y_pos += self.step
          if self.direction == 2:
               self.x_pos -= self.step
          if self.direction == 3:
               self.y_pos -= self.step     
     def checkBlack(self):         
          if window.get_at((self.x_pos, self.y_pos)) == black:
            return True
     def checkWhite(self):         
          if window.get_at((self.x_pos, self.y_pos)) == white:
            return True
     def checkCustomColor(self, CustomColor):
          self.CustomColor = CustomColor        
          if window.get_at((self.x_pos, self.y_pos)) == self.CustomColor:
            return True
     def rotateClockwise(self):
         self.direction += 1
         if self.direction > 3:
             self.direction = 0     
     def rotateCounterClockwise(self):
         self.direction -= 1
         if self.direction < 0:
             self.direction = 3
     def turnAround(self):
         self.direction += 2
         if self.direction < 0:
             self.direction = 3
     def changeToBlack(self):
         window.set_at((self.x_pos, self.y_pos), black)
     def changeToWhite(self):
         window.set_at((self.x_pos, self.y_pos), white)
     def changeToCustomColor(self, CustomColor):
         self.CustomColor = CustomColor
         window.set_at((self.x_pos, self.y_pos), CustomColor)
     def rainbowCycle(self): 
         S = 1
         V = 1
         C = S * V
         X = C * (1 - abs(((self.Hue/60) % 2) - 1))
         m = V - C
         if 0 <= self.Hue and self.Hue <= 60:
            RGBx = (C, X, 0)
         if 60 <= self.Hue and self.Hue <= 120:
            RGBx = (X, C, 0)
         if 120 <= self.Hue and self.Hue <= 180:
            RGBx = (0, C, X)
         if 180 <= self.Hue and self.Hue <= 240:
            RGBx = (0, X, C)    
         if 240 <= self.Hue and self.Hue <= 300:
            RGBx = (X, 0, C)
         if 300 <= self.Hue and self.Hue <= 360:
            RGBx = (C, 0, X) 
         R = (RGBx[0] + m)*255
         G = (RGBx[1] + m)*255
         B = (RGBx[2] + m)*255
         window.set_at((self.x_pos, self.y_pos), (R, G, B))
         if self.Hue < 360:
             self.Hue += 1
         else:
             self.Hue = 0
     def langtsonsAnt(self):
         self.checkEdge()
         if self.checkBlack() == True:
            self.rotateCounterClockwise()
            self.changeToWhite()
            self.forward(1)          
         else:
            self.rotateClockwise()
            self.changeToBlack()
            self.forward(1)


         
       
pygame.init()
sX = 800
sY = 800
window = pygame.display.set_mode((sX, sY))
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255,255,255)
red = (255,0,0)
green = (0, 255, 0)

Ant = turtle(sX//2, sY//2, 0, 0)
Ant2 = turtle(sX//2 + 1, sY//2, 0, 0)
window.fill(black)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False

    for x in range(100):
        Ant.langtsonsAnt()
            #Red and Green custom ant
        # if Ant.checkCustomColor(green) == True:
        #     Ant.rotateCounterClockwise()
        #     Ant.changeToCustomColor(black)
        #     Ant.forward(1)          
        # if Ant.checkCustomColor(red) == True:
        #     Ant.rotateClockwise()
        #     Ant.changeToCustomColor(green)
        #     Ant.forward(1)
        # else:
        #     Ant.rotateClockwise()
        #     Ant.changeToCustomColor(red)
        #     Ant.forward(1)
            #Rainbow Custom Ant
        # Ant.checkEdge()   
        # if Ant.checkBlack() == True:
        #     Ant.rotateCounterClockwise()
        #     Ant.rainbowCycle()
        #     Ant.forward(1)
        #     Ant.rotateCounterClockwise()
        #     Ant.rainbowCycle()
        #     Ant.forward(1)
        #     Ant.forward(1)
        # else:
        #     Ant.rotateClockwise()
        #     Ant.changeToBlack()
        #     Ant.forward(1)
        #     Ant.forward(1)
            
    pygame.display.flip()
    clock.tick(60)
pygame.quit()