import pygame
pygame.init()

screen = pygame.display.set_mode((600, 200))
pygame.display.set_caption("Music player")
screen.fill((255, 255, 255))


playicon = pygame.image.load("lab7/music_photos/playicon.png")
playicon = pygame.transform.scale(playicon, (50, 50))

stopicon = pygame.image.load("lab7/music_photos/pausebutton.png")
stopicon = pygame.transform.scale(stopicon, (50, 50))

nexticon = pygame.image.load("lab7/music_photos/nextbutton.png")
nexticon = pygame.transform.scale(nexticon, (50, 50))

backicon = pygame.image.load("lab7/music_photos/nextbutton copy.jpg")
backicon = pygame.transform.scale(backicon, (50, 50))


play_rect = playicon.get_rect(topleft=(225, 75))
stop_rect = stopicon.get_rect(topleft=(325, 75))
next_rect = nexticon.get_rect(topleft=(425, 75))
back_rect = backicon.get_rect(topleft=(120, 75))

music_list = [
    "lab7/musics/Arctic Monkeys - I Wanna Be Yours.mp3",
    "lab7/musics/FRANK OCEAN - PINK  WHITE  ( s l o w e d      r e v e r b ).mp3",
    "lab7/musics/Sade - Smooth Operator (Lyrics).mp3"
]

index = 0
on = True
a = False

while on:
    screen.fill((255, 255, 255))
    screen.blit(playicon, play_rect.topleft)
    screen.blit(stopicon, stop_rect.topleft)
    screen.blit(nexticon, next_rect.topleft)
    screen.blit(backicon, back_rect.topleft)
    pygame.display.update()

    if a:
        pygame.mixer.music.load(music_list[index])
        pygame.mixer.music.play()
        a = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False

        if event.type == pygame.MOUSEBUTTONDOWN:  
            if play_rect.collidepoint(event.pos):
                a = True

            if stop_rect.collidepoint(event.pos):
                pygame.mixer.music.stop() 

            if next_rect.collidepoint(event.pos):
                index += 1
                if index == 3:
                    index = 0
                pygame.mixer.music.stop()
                a = True

            if back_rect.collidepoint(event.pos): 
                index -= 1
                if index < 0:
                    index = 2
                pygame.mixer.music.stop()
                a = True

pygame.quit()
