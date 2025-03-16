import pygame , datetime
import time
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Micky Mouse Clock")
screen.fill((255, 255, 255))

bg_image = pygame.image.load("lab7/photos/clock.png")
sec_hand = pygame.image.load("lab7/photos/sec_hand.png")
min_hand = pygame.image.load("lab7/photos/min_hand.png")


second = int(datetime.datetime.now().strftime("%S"))
minute = int(datetime.datetime.now().strftime("%M"))


sec_angle = second * -6
min_angle = minute * -6
clock = pygame.time.Clock()


on = True
while on:
    screen.blit(bg_image , (0, 0))
    
    rot_sec_hand = pygame.transform.rotate(sec_hand , sec_angle+60)
    rot_min_hand = pygame.transform.rotate(min_hand , min_angle-60)

    sec_hand1 = rot_sec_hand.get_rect(center=(400 , 300))
    min_hand1 = rot_min_hand.get_rect(center=(400 , 300))

    screen.blit(rot_sec_hand , sec_hand1.topleft)
    screen.blit(rot_min_hand , min_hand1.topleft)

    sec_angle -= 6
    if sec_angle % 360 == 0:
        min_angle -= 6

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False
            pygame.quit()
    clock.tick(1)