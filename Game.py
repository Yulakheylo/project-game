import pygame
import sys
import os

FPS = 50
size = WIDTH, HEIGHT = 1187, 660

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Игра')

clock = pygame.time.Clock()


# функция для загрузки изображений
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


# ОТРИСОВККА фона
background_image = pygame.image.load('images/fon.png')
background_image = pygame.transform.scale(background_image, size)


# функция для завершения программы
def terminate():
    pygame.quit()
    sys.exit()


# Заставка
def zastavka():
    img_game = pygame.image.load('images/zastavka.png')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        screen.blit(pygame.transform.scale(img_game, [1200, 670]), [0, 0])
        pygame.display.flip()


zastavka()


# загрузка уровней
def load_level(filename):
    filename = "levels/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


# Функция для генерации уровня на основе данных из файла
def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '1':
                Tile('zemla', x, y)
            elif level[y][x] == '#':
                Tile('kirpichik', x, y)
            elif level[y][x] == '@':
                Tile('water', x, y)
    return x, y


# Класс для отображения тайла
class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


# Загрузка изображений тайлов и игрока
tile_images = {
    'zemla': load_image('earth.png'),
    'kirpichik': load_image('kirpich.png'),
    'water': load_image('water.png')
}

# размеры тайла
tile_width = tile_height = 74

all_sprites = pygame.sprite.Group()  # Создание группы спрайтов
tiles_group = pygame.sprite.Group()  # Группа спрайтов для тайлов

level = load_level('level.txt')  # Загрузка уровня из файла
level_x, level_y = generate_level(level)  # Генерация уровня


# главный игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
    screen.blit(background_image, (0, 0))
    tiles_group.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
