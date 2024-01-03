import pygame
import sys
import os

FPS = 50
size = WIDTH, HEIGHT = 1187, 660

pygame.init()

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Игра')

clock = pygame.time.Clock()


class Game:
    def __init__(self):
        pass

    def screen_igra(self):
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
                    elif level[y][x] == '2':
                        Tile('water', x, y)
                    elif level[y][x] == '$':
                        Tile('kolona', x, y)
                    elif level[y][x] == '3':
                        Tile('oblako', x, y)
                    elif level[y][x] == '^':
                        Tile('bugor', x, y)
                    elif level[y][x] == '*':
                        Tile('life', x, y)
                    elif level[y][x] == 'm':
                        Tile('money', x, y)
            return x, y

        # Класс для отображения тайла
        class Tile(pygame.sprite.Sprite):
            def __init__(self, tile_type, pos_x, pos_y):
                super().__init__(tiles_group, all_sprites)
                self.image = tile_images[tile_type]
                self.rect = self.image.get_rect().move(
                    tile_width * pos_x, tile_height * pos_y)

        # Загрузка изображений тайлов и игрока

        # Загрузка изображений тайлов и игрока
        tile_images = {
            'zemla': load_image('earth.png'),
            'kirpichik': load_image('kirpich.png'),
            'water': load_image('water.png'),
            'kolona': load_image('kolona.png'),
            'oblako': load_image('oblachko.png'),
            'bugor': load_image('bugor.png'),
            'life': load_image('life.png'),
            'money': load_image('money.png')
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


# кнопка
class Knopka:
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
                self.sound = pygame.mixer.Sound('sounds/звук_кнопки.mp3')
                self.sound.play()

    def proverka_clicking(self, pos):
        return self.x < pos[0] < self.x + self.width and \
            self.y < pos[1] < self.y + self.height


def text_name_game(screen):
    font = pygame.font.Font(None, 38)
    text = font.render('В поисках утерянного клада', 1, (255, 255, 255))
    screen.blit(text, (400, 80))


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Старт')

    knopka_start = Knopka(WIDTH / 2 - (251 / 2), 150, 252, 120, 'images/Кнопка.png', 'Начать игру')
    knopka_output = Knopka(WIDTH / 2 - (251 / 2), 250, 252, 120, 'images/Кнопка.png', 'Выйти из игры')
    knopka_levels = Knopka(WIDTH / 2 - (251 / 2), 350, 252, 120, 'images/Кнопка.png', 'Уровни')
    knopka_coin = Knopka(560, 470, 70, 50, 'images/coins.png', '')

    game = Game()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            knopka_start.clicking(event)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if knopka_start.proverka_clicking(pygame.mouse.get_pos()):
                    game.screen_igra()
        screen.fill(pygame.Color('#B73229'))
        knopka_start.text_on_knopki(screen)
        knopka_output.text_on_knopki(screen)
        knopka_levels.text_on_knopki(screen)
        knopka_coin.text_on_knopki(screen)

        text_name_game(screen)

        pygame.display.flip()
    pygame.quit()
