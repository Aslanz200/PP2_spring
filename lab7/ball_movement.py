import pygame
pygame.init()
screen = pygame.display.set_mode((600 , 600))

x = 300
y = 300
radius = 25
clock = pygame.time.Clock()

on = True
while on:
    screen.fill("White")
    pygame.draw.circle(screen , "Red" , (x , y) , radius)
    pygame.display.update()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                save = y
                y -= 20
                if y<radius:
                    y = save
            if event.key == pygame.K_DOWN:
                save = y
                y += 20
                if y>600-radius:
                    y = save
            if event.key == pygame.K_LEFT:
                save = x
                x -= 20
                if x<radius:
                    x = save
            if event.key == pygame.K_RIGHT:
                save = x
                x += 20
                if x>600-radius:
                    x = save
        clock.tick(60)
pygame.quit()