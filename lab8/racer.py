import pygame , time , sys
from random import randint
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((400 , 600))
bgimage = pygame.image.load("lab8/racer_elements/AnimatedStreet.png")

FPS = pygame.time.Clock()


font = pygame.font.SysFont("Verdana" , 60)
game_over = font.render("Game over" , True , "Black")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/racer_elements/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (randint(30, 330) , 0)

    def move(self):
        self.rect.move_ip(0 , 9)
        if self.rect.top > 600 :
            self.rect.top = -60
            self.rect.center = (randint(30, 330) , 0)
    def draw(self , screen):
        screen.blit(self.image , self.rect)



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/racer_elements/Player.png")   #my car png
        self.rect = self.image.get_rect()  #drawing rectangle aroung my png so i can allocate its postion
        self.rect.center = (200 , 550)  #starting position
    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.top>0:   #top off-screen limit
            if pressed_keys[K_UP]:
                self.rect.move_ip(0 , -3)

        if self.rect.bottom<600:   #bottom off-screen limit
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0 , 3)

        if self.rect.left > 0:    #left off-screen limit
          if pressed_keys[K_LEFT]:
              self.rect.move_ip(-3, 0)

        if self.rect.right < 400:   #right off-screen limit
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(3, 0)
    def draw(self , screen):
        screen.blit(self.image , self.rect)

pygame.mixer.music.load("lab8/racer_elements/background.wav") 
pygame.mixer.music.play(-1)

on = True
P1 = Player()
E1 = Enemy()
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
while on:
    
    screen.blit(bgimage , (0 , 0))

    P1.update()
    E1.move()

    P1.draw(screen)
    E1.draw(screen)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False

    if pygame.sprite.spritecollideany(P1 , enemies):
        pygame.mixer.music.stop()
        pygame.mixer.Sound("lab8/racer_elements/crash.wav").play()
        time.sleep(2)
        screen.fill("Red")
        screen.blit(game_over , (30 , 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    FPS.tick(60)

pygame.quit()
