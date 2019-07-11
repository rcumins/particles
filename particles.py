import pygame, os, random
from pygame.locals import *

r = random
os.environ["SDL_VIDEO_WINDOW_POS"] = "0,0"

class Box(pygame.sprite.Sprite):
    def __init__(self, size=(32,32), pos=(100,100), colour=(r.randint(0,255),r.randint(0,255),r.randint(0,255)),acc=1,top=32):
        pygame.sprite.Sprite.__init__(self)
        self.screen = pygame.display.get_surface().get_rect()
        self.rect = pygame.Rect(pos,size)
        self.image = pygame.Surface(size)
        self.image.fill(colour)
        self.acc = acc
        self.top = top
        self.velocity = [0,0]
        self.gravity = 0.980665
        self.friction = 0.80999

    def update(self,velocity):
        self.key_input()
        self.rect = self.rect.move(velocity)

        if self.rect.x < 0 and self.velocity[0] < 0:
            self.rect.x = 0
            self.velocity[0] = (self.velocity[0]*0.8)
            self.velocity[0] *= -1

        if self.rect.right > self.screen.width and self.velocity[0] > 0:
            self.rect.x = (self.screen.width-self.rect.width)
            self.velocity[0] = (self.velocity[0]*0.8)
            self.velocity[0] *= -1

        if self.rect.y < 0  and self.velocity[1] < 0:
            self.rect.y = 0
            self.velocity[1] = (self.velocity[1]*0.8)
            self.velocity[1] *= -1

        if self.rect.bottom > self.screen.bottom:
            self.rect.y = self.screen.bottom - self.rect.height
            self.velocity[1] = (self.velocity[1]*0.8)
            self.velocity[1] *= -1

        
        if self.rect.bottom >= (self.screen.bottom):
            self.rect.y = self.screen.height - (self.rect.height*3)
            if self.velocity[1] > -3:
                self.velocity[1] = 0;
            self.velocity[0] *= self.friction
            
        self.velocity[1] += self.gravity
                            
    def key_input(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.accelerate("up")
        if keystate[pygame.K_DOWN]:
            self.accelerate("down")
        if keystate[pygame.K_LEFT]:
            self.accelerate("left")
        if keystate[pygame.K_RIGHT]:
            self.accelerate("right")
        if keystate[pygame.K_q]:
            pygame.quit()

    def accelerate(self,direction):
        start_acc = 0
        if direction == "down":
            self.velocity[1] += self.acc
            if self.velocity[1] > self.top:
                self.velocity[1] = self.top

        elif direction == "up":
            self.velocity[1] -= (self.acc*4)
            if self.velocity[1] < -self.top:
                self.velocity[1] = -self.top

        if direction == "left":
            self.velocity[0] -= self.acc
            if self.velocity[0] > -3:
                start_acc = 4
                self.velocity[0] -= start_acc
            if self.velocity[0] < -self.top:
                self.velocity[0] = -self.top

        elif direction == "right":
            self.velocity[0] += self.acc
            if self.velocity[0] < 3:
                start_acc = 4
                self.velocity[0] += start_acc
            if self.velocity[0] > self.top:
                self.velocity[0] = self.top

pygame.init()
res = (1024,768)
pos = (0,0)
screen = pygame.display.set_mode(res,FULLSCREEN)#NOFRAME, 
bg_rect = pygame.Rect(pos,res)
bg_image = pygame.Surface(res)
bg_image.fill((0,0,0))

p = []
p1 = []
p2 = []
p3 = []
for x in range(0,400):
    box = Box((r.randint(2,4),r.randint(2,4)),(r.randint(1,r.randint(1,res[0])),r.randint(1,r.randint(1,res[1]))),(r.randint(0,25),r.randint(0,25),r.randint(120,255)),r.randint(1,10),r.randint(20,32))
    box.image.set_alpha(100)
    p.append(box)
    p1.append(box)
    box = Box((r.randint(4,6),r.randint(4,6)),(r.randint(1,r.randint(1,res[0])),r.randint(1,r.randint(1,res[1]))),(r.randint(0,25),r.randint(0,25),r.randint(120,255)),r.randint(1,8),r.randint(20,32))
    p.append(box)
    p2.append(box)
    box = Box((r.randint(4,8),r.randint(4,8)),(r.randint(1,r.randint(1,res[0])),r.randint(1,r.randint(1,res[1]))),(r.randint(0,25),r.randint(0,25),r.randint(120,255)),r.randint(1,4),r.randint(20,32))
    box.image.set_alpha(80)
    p.append(box)
    p3.append(box)
screen.blit(bg_image,bg_rect)
for box in p:
    box.velocity = [r.randint(-32,32),r.randint(-32,32)]
    screen.blit(box.image,box.rect)

pygame.display.update()

clock = pygame.time.Clock()
started = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.QUIT:
                pygame.quit()
                if event.key == K_ESCAPE:
                    pygame.quit()
                    
    keystate = pygame.key.get_pressed()
    
    if keystate[pygame.K_SPACE]:
        for box in p:
            box.velocity = [0,0]
            box.rect.x = r.randint(1,res[0]-1)
            box.rect.y = r.randint(1,res[1]-1)
    
    if keystate[pygame.K_r]:
        for box in p:
            colour = (r.randint(120,255),r.randint(0,25),r.randint(0,25))
            box.image.fill(colour)
            
    if keystate[pygame.K_g]:
        for box in p:
            colour = (r.randint(0,25),r.randint(120,255),r.randint(0,25))
            box.image.fill(colour)

    if keystate[pygame.K_b]:
        for box in p:
            colour = (r.randint(0,25),r.randint(0,25),r.randint(120,225))
            box.image.fill(colour)
            
    if keystate[pygame.K_c]:
        for box in p:
            red = (r.randint(120,225),r.randint(0,25),r.randint(0,25))
            green = (r.randint(0,25),r.randint(120,225),r.randint(0,25))
            blue = (r.randint(0,25),r.randint(0,25),r.randint(120,225))
            colour = r.choice([red,green,blue])
            box.image.fill(colour)

    if keystate[pygame.K_x]:
        for box in p:
            box.velocity = [r.randint(-32,32),r.randint(-32,32)]

    if keystate[pygame.K_s]:
        for box in p:
            box.velocity = [0,0]

    if keystate[pygame.K_z]:
        for box in p:
            box.gravity = 0

    if keystate[pygame.K_a]:
        for box in p:
            box.gravity = 0.580665
    
    if keystate[pygame.K_f]:
        colour = (r.randint(0,255),r.randint(0,255),r.randint(0,255))
        for box in p:
            box.image.fill(colour)
            box.image.set_alpha(r.choice((80,120,81,121,255)))

         
    if keystate[pygame.K_l]:
        bg_image.fill((0,0,0))
      
    if keystate[pygame.K_k]:
        colour = (r.randint(0,100),r.randint(0,100),r.randint(0,100))
        bg_image.fill(colour)
      
    screen.blit(bg_image,bg_rect)
    for box in p:
        box.update(box.velocity)
        screen.blit(box.image,box.rect)
    pygame.display.flip()
    clock.tick(30)
    #print clock.get_fps()
