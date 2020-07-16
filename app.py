import pygame
from pygame import display
from pygame import mixer


pygame.init()

# Screen
size_x, size_y = 800, 600
bg_color = (5,35,45)
white = (255, 255, 255)
screen = pygame.display.set_mode((size_x, size_y))

pygame.display.set_caption("Pruebameste")
screen.fill(bg_color)


font = pygame.font.Font('lefontdiu.ttf', 32)
text = font.render("Reproduciendo: music_test.mp3", True, white)
text_rect = text.get_rect()
text_rect.center = (size_x // 2, size_y // 2)

screen.blit(text, text_rect)

# Reproduce la song
mixer.music.load("music_test.mp3")
mixer.music.play(0)

pygame.display.flip()

run = True
while run:
    # mixer.music.get_busy()
    # # pygame.event.poll()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False


pygame.quit()