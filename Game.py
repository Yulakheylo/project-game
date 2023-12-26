import pygame
import sys
import os

FPS = 50
size = WIDTH, HEIGHT = 1200, 670

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Игра')

clock = pygame.time.Clock()

#функция для загрузки изображений
def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

#ОТРИСОВККА фона
background_image = pygame.image.load('images/fon.png')

#функция для завершения программы
def terminate():
    pygame.quit()
    sys.exit()

#главный игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
    screen.blit(background_image, (-100, -160))
    pygame.display.flip()
    clock.tick(FPS)



