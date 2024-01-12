import pygame
import sys
import os

FPS = 50
size = WIDTH, HEIGHT = 1187, 660
SIZE = WIDTH, HEIGHT = 1187, 660

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('В поисках утерянного клада')

clock = pygame.time.Clock()


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


def screen_igra():
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
                    Tile('earth.png', x, y)
                elif level[y][x] == '2':
                    Tile('pov_earth.png', x, y)
                elif level[y][x] == '#':
                    Tile('kirpich.png', x, y)
                elif level[y][x] == '.':
                    Tile('water.png', x, y)
                elif level[y][x] == ',':
                    Tile('pov_water.png', x, y)
                elif level[y][x] == '$':
                    Tile('kolona.png', x, y)
                elif level[y][x] == '3':
                    Tile('oblachko.png', x, y)
                elif level[y][x] == '^':
                    Tile('bugor.png', x, y)
                elif level[y][x] == '*':
                    Tile('life.png', x, y)
                elif level[y][x] == 'm':
                    Tile('money_cr.png', x, y)
                elif level[y][x] == '@':
                    new_player = Player(x, y)

        return new_player, x, y

    # Класс для отображения тайла
    class Tile(pygame.sprite.Sprite):
        def __init__(self, tile_type, pos_x, pos_y):
            super().__init__(tiles_group, all_sprites)
            self.image = load_image(tile_type, -1)
            self.rect = self.image.get_rect().move(
                tile_width * pos_x, tile_height * pos_y)

    # класс для отображения игрока
    class Player(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y):
            super().__init__(player_group, all_sprites)
            self.image = player_image
            self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y + 2)
            self.pos = pos_x, pos_y
            self.direction = ''  # начальное направление движения
            self.moving = False  # флаг движения
            self.movement_x = 0  # смещение по x
            self.movement_y = 0  # смещение пo y

        def move(self, x, y):
            self.pos = x, y
            self.rect = self.image.get_rect().move(tile_width * x, tile_height * y + 2)

        def update(self):  # функция для обновления координат игрока
            if self.moving:
                if self.direction == 'left' and self.rect.x > 0:  # движение влево
                    self.rect.left -= 10
                if self.direction == 'right' and self.rect.x < level_x:  # движение вправо
                    self.rect.left += 10
                if self.direction == 'up' and self.rect.y > 0:  # движение вверх
                    self.rect.top -= 10
                if self.direction == 'down' and self.rect.y < level_y:  # движение вниз
                    self.rect.top += 10


    # загрузка изображения игрока
    player_image = load_image('pl.png', -1)

    # размеры тайла
    tile_width = tile_height = 74

    all_sprites = pygame.sprite.Group()  # Создание группы спрайтов
    tiles_group = pygame.sprite.Group()  # Группа спрайтов для тайлов
    player_group = pygame.sprite.Group()  # Группа спрайтов для игрока

    level = load_level('level.txt')  # Загрузка уровня из файла
    player, level_x, level_y = generate_level(level)  # Генерация уровня
    level_x = WIDTH / tile_width
    level_y = HEIGHT / tile_height

    # создание объекта игрока
    pos_x, pos_y = 100, 100
    player = Player(pos_x, pos_y)

    # главный игровой цикл
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

        keys = pygame.key.get_pressed()

        # обработка движения
        if not player.moving:
            if keys[pygame.K_LEFT]:
                player.moving = True
                player.direction = 'left'
            elif keys[pygame.K_RIGHT]:
                player.moving = True
                player.direction = 'right'
            elif keys[pygame.K_UP]:
                player.moving = True
                player.direction = 'up'
            elif keys[pygame.K_DOWN]:
                player.moving = True
                player.direction = 'down'
        else:
            if not any([keys[pygame.K_LEFT], keys[pygame.K_RIGHT], keys[pygame.K_UP], keys[pygame.K_DOWN]]):
                player.moving = False

        screen.blit(background_image, (0, 0))
        tiles_group.draw(screen)  # отрисовака тайлов
        player_group.update()  # обновление координат игрока
        player_group.draw(screen)  # отрисовка игрока
        pygame.display.flip()
        clock.tick(FPS)


class Menu:
    def __init__(self, x, y, width, height, kartinka, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.kartinka = pygame.image.load(kartinka)
        self.kartinka = pygame.transform.scale(self.kartinka, (width, height))
        self.text = text

    def text_on_knopki(self, screen):
        font = pygame.font.Font(None, 38)
        text = font.render(self.text, 1, (255, 255, 255))
        knopka = pygame.Rect(self.x, self.y, self.width, self.height)
        screen.blit(self.kartinka, knopka)
        screen.blit(text, (self.x + (self.width - text.get_width()) // 2,
                           self.y + (self.height - text.get_height()) // 2))

    def clicking(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if (knopka_start.proverka_clicking(pygame.mouse.get_pos()) or
                    knopka_output.proverka_clicking(pygame.mouse.get_pos()) or
                    knopka_levels.proverka_clicking(pygame.mouse.get_pos()) or
                    knopka_coin.proverka_clicking(pygame.mouse.get_pos())):
                self.sound = pygame.mixer.Sound('sounds/sound_knopka.mp3')
                self.sound.play()

    def proverka_clicking(self, pos):
        return self.x < pos[0] < self.x + self.width and \
            self.y < pos[1] < self.y + self.height


def text_name_game(screen):
    font = pygame.font.Font(None, 38)
    text = font.render('В поисках утерянного клада', 1, (0, 100, 0))
    screen.blit(text, (WIDTH / 2 - (350 / 2), 80))


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Старт')

    knopka_start = Menu(WIDTH / 2 - (251 / 2), 150, 252, 120, 'images/Knopka.png', 'Начать игру')
    knopka_output = Menu(WIDTH / 2 - (251 / 2), 250, 252, 120, 'images/Knopka.png', 'Выйти из игры')
    knopka_levels = Menu(WIDTH / 2 - (251 / 2), 350, 252, 120, 'images/Knopka.png', 'Уровни')
    knopka_coin = Menu(WIDTH / 2 - (80 / 2), 470, 70, 50, 'images/coins.png', '')

    foto_fona = pygame.image.load('images/fon_menu.jpg')
    foto_fona = pygame.transform.scale(foto_fona, (1800, 660))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            knopka_start.clicking(event)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if knopka_start.proverka_clicking(pygame.mouse.get_pos()):
                    screen_igra()

        screen.fill((0, 0, 0))
        screen.blit(foto_fona, (0, 0))

        knopka_start.text_on_knopki(screen)
        knopka_output.text_on_knopki(screen)
        knopka_levels.text_on_knopki(screen)
        knopka_coin.text_on_knopki(screen)

        text_name_game(screen)

        pygame.display.flip()
    pygame.quit()
