import pygame
import sys
import os
import camera

# Инициализация Pygame
pygame.init()

# Определение некоторых констант для игры
WIDTH = 1187
HEIGHT = 660
FPS = 60
GRAVITY = 0.8
PLAYER_SPEED = 5
JUMP_HEIGHT = -17
size = WIDTH, HEIGHT

# Создание игрового окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("игрухки")


# функция для завершения программы
def terminate():
    pygame.quit()
    sys.exit()


def igra():
    level_int = 1
    level = []

    # Определение цветов
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

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

    # Загрузка изображений жизни, уровня, количества монеток в углах экрана
    live_image = pygame.image.load("images/lives.png")
    coin_image = pygame.image.load("images/money_cr.png")
    level1_image = pygame.image.load("images/level1.png")
    level2_image = pygame.image.load("images/level2.png")
    level3_image = pygame.image.load("images/level3.png")

    # функция для завершения программы
    def terminate():
        pygame.quit()
        sys.exit()

    def WASTED():
        img_game = pygame.image.load('images/WASTED.png')
        pygame.mixer.stop()
        wasted_sound = pygame.mixer.Sound('sounds/sound_wasted.mp3')
        wasted_sound.play(0)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    men()
            screen.blit(pygame.transform.scale(img_game, [1200, 670]), [0, 0])
            pygame.display.flip()

    def WIN():
        img_game = pygame.image.load('images/win.png')
        pygame.mixer.stop()
        win_sound = pygame.mixer.Sound('sounds/sound_win.mp3')
        win_sound.play(0)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    men()
            screen.blit(pygame.transform.scale(img_game, [1200, 670]), [0, 0])
            pygame.display.flip()

    # Загрузка изображений игрока
    player_images_right = [
        load_image("pl.png", -1).convert_alpha(),
        load_image("pl.png", -1).convert_alpha(),
        load_image("pl.png", -1).convert_alpha(),
        load_image("pl.png", -1).convert_alpha(),
        load_image("pl2.png", -1).convert_alpha(),
        load_image("pl2.png", -1).convert_alpha(),
        load_image("pl2.png", -1).convert_alpha(),
        load_image("pl2.png", -1).convert_alpha(),
        load_image("pl3.png", -1).convert_alpha(),
        load_image("pl3.png", -1).convert_alpha(),
        load_image("pl3.png", -1).convert_alpha(),
        load_image("pl3.png", -1).convert_alpha(),
        load_image("pl4.png", -1).convert_alpha(),
        load_image("pl4.png", -1).convert_alpha(),
        load_image("pl4.png", -1).convert_alpha(),
        load_image("pl4.png", -1).convert_alpha()
    ]

    player_images_left = [
        pygame.transform.flip(load_image("pl.png", -1).convert_alpha(), True, False),
        pygame.transform.flip(load_image("pl.png", -1).convert_alpha(), True, False),
        pygame.transform.flip(load_image("pl.png", -1).convert_alpha(), True, False),
        pygame.transform.flip(load_image("pl.png", -1).convert_alpha(), True, False),
        pygame.transform.flip(load_image("pl2.png", -1).convert_alpha(), True, False),
        pygame.transform.flip(load_image("pl2.png", -1).convert_alpha(), True, False),
        pygame.transform.flip(load_image("pl2.png", -1).convert_alpha(), True, False),
        pygame.transform.flip(load_image("pl2.png", -1).convert_alpha(), True, False),
        pygame.transform.flip(load_image("pl3.png", -1).convert_alpha(), True, False),
        pygame.transform.flip(load_image("pl3.png", -1).convert_alpha(), True, False),
        pygame.transform.flip(load_image("pl3.png", -1).convert_alpha(), True, False),
        pygame.transform.flip(load_image("pl3.png", -1).convert_alpha(), True, False),
        pygame.transform.flip(load_image("pl4.png", -1).convert_alpha(), True, False),
        pygame.transform.flip(load_image("pl4.png", -1).convert_alpha(), True, False),
        pygame.transform.flip(load_image("pl4.png", -1).convert_alpha(), True, False),
        pygame.transform.flip(load_image("pl4.png", -1).convert_alpha(), True, False)

    ]

    # Загрузка изображений монеток и блоков
    coin_image = load_image("money_cr.png", -1).convert_alpha()
    pov_earth_image = load_image("pov_earth.png", -1).convert_alpha()
    earth_image = load_image("earth.png", -1).convert_alpha()
    pov_water_image = load_image("pov_water.png", -1).convert_alpha()
    water_image = load_image("water.png", -1).convert_alpha()
    block_image = load_image("kirpich.png", -1).convert_alpha()
    life_image = load_image("life.png", -1).convert_alpha()
    exit_image = load_image("exit_level.png", -1).convert_alpha()
    klad_image = load_image("klad.png", -1).convert_alpha()

    # Создание класса для представления блоков на уровне
    class Tile(pygame.sprite.Sprite):
        def __init__(self, x, y, tile_type):
            super().__init__()
            if tile_type == "coin":
                self.image = coin_image
            elif tile_type == "life":
                self.image = life_image
            elif tile_type == "pov_earth":
                self.image = pov_earth_image
            elif tile_type == "earth":
                self.image = earth_image
            elif tile_type == "pov_water":
                self.image = pov_water_image
            elif tile_type == "water":
                self.image = water_image
            elif tile_type == "block":
                self.image = block_image
            elif tile_type == 'exit_level':
                self.image = exit_image
            elif tile_type == 'klad':
                self.image = klad_image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    # Создание класса для игрока
    class Player(pygame.sprite.Sprite):
        def __init__(self, tiles, money, life, water, exit_level, klad):
            super().__init__()
            self.images_right = player_images_right
            self.images_left = player_images_left
            self.current_image = 0
            self.image = self.images_right[self.current_image]
            self.rect = self.image.get_rect()
            self.rect.x = 100
            self.rect.y = 0
            self.vel_y = 0
            self.vel_x = 0
            self.tiles = tiles
            self.money = money
            self.life = life
            self.water = water
            self.exit_level = exit_level
            self.klad = klad
            self.score = 0
            self.lives = 3
            self.levels = 1
            self.exit_hit = False
            # self.money_sound = False

        def update(self):
            self.vel_y += GRAVITY

            # Проверка столкновения с блоками
            self.rect.y += self.vel_y

            block_collisions = pygame.sprite.spritecollide(self, self.tiles, False)
            for block in block_collisions:
                if self.vel_y > 0:
                    self.rect.bottom = block.rect.top
                    self.vel_y = 0
                elif self.vel_y < 0:
                    self.rect.top = block.rect.bottom
                    self.vel_y = 0

            self.rect.x += self.vel_x

            block_collisions = pygame.sprite.spritecollide(self, self.tiles, False)
            for block in block_collisions:
                if self.vel_x > 0:
                    self.rect.right = block.rect.left
                    self.vel_x = 0
                elif self.vel_x < 0:
                    self.rect.left = block.rect.right
                    self.vel_x = 0

            # Обработка движения влево и вправо
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.vel_x = -PLAYER_SPEED
                self.image = self.images_left[self.current_image]
            elif keys[pygame.K_RIGHT]:
                self.vel_x = PLAYER_SPEED
                self.image = self.images_right[self.current_image]
            else:
                self.vel_x = 0

            # Обработка прыжка
            if keys[pygame.K_SPACE] and self.vel_y == 0:
                self.vel_y = JUMP_HEIGHT
                keys = pygame.key.get_pressed()
                jump_sound = pygame.mixer.Sound('sounds/jump.mp3')
                jump_sound.play(0)

            # столкновение со стеной
            if player.rect.left == 0 and keys[pygame.K_LEFT]:
                self.vel_x = 0

            # Анимация движения игрока
            self.animate()

        def animate(self):
            # Анимация движения игрока
            if self.vel_y != 0:
                self.current_image = 9
            else:
                self.current_image += 1
                if self.current_image >= len(self.images_right):
                    self.current_image = 0
            if self.image in self.images_left:
                self.image = self.images_left[self.current_image]

            if self.image in self.images_right:
                self.image = self.images_right[self.current_image]

            if self.vel_x == 0:
                self.current_image = 1

        def collect_coin(self):
            # Обработка столкновения с монеткой
            coins_collected = pygame.sprite.spritecollide(self, self.money, True)
            for coin in coins_collected:
                if coin.image == coin_image:
                    self.score += 1
                    money_sound = pygame.mixer.Sound('sounds/sound_money.mp3')
                    money_sound.play(0)

        def collect_life(self):
            # Обработка столкновения с жизнью
            life_collected = pygame.sprite.spritecollide(self, self.life, True)
            for life in life_collected:
                if life.image == life_image:
                    self.lives += 1
                    life_sound = pygame.mixer.Sound('sounds/sound_life.mp3')
                    life_sound.play(0)

        def collect_exit_level(self):
            # Обработка столкновения с выходом
            exit_level_collected = pygame.sprite.spritecollide(self, self.exit_level, True)
            for exit_level in exit_level_collected:
                if exit_level.image == exit_image:
                    self.levels += 1
                    self.exit_hit = True
                    self.rect.x = 100
                    self.rect.y = 0
                    level_sound = pygame.mixer.Sound('sounds/sound_level.mp3')
                    level_sound.play(0)
            # Обработка столкновения с сокровищами
            win_collected = pygame.sprite.spritecollide(self, self.klad, False)
            for k in win_collected:
                if self.vel_y > 0:
                    self.rect.bottom = k.rect.top
                    self.vel_y = 0
                    self.rect.x = 100
                    self.rect.y = 0
                    WIN()
                elif self.vel_y < 0:
                    self.rect.top = k.rect.bottom
                    WIN()
            for block in win_collected:
                if self.vel_x > 0:
                    self.rect.right = block.rect.left
                    WIN()
                elif self.vel_x < 0:
                    self.rect.left = block.rect.right
                    WIN()

        def lose_life(self):
            # Потеря жизни
            if player.rect.y > HEIGHT:
                self.lives -= 1
                self.rect.x -= 300
                self.rect.y = 0
            water_collected = pygame.sprite.spritecollide(self, self.water, False)
            for block in water_collected:
                if self.vel_y > 0:
                    self.rect.bottom = block.rect.top
                    self.vel_y = 0
                    self.rect.x = 100
                    self.rect.y = 0
                    self.lives -= 1
                elif self.vel_y < 0:
                    self.rect.top = block.rect.bottom
                    self.vel_y = 0
                    self.rect.x = 100
                    self.rect.y = 0
                    self.lives -= 1

        def camera(self):
            if self.rect.x > 350:
                # изменяем ракурс камеры
                camera.update(player)
                # обновляем положение всех спрайтов
                for sprite in all_sprites:
                    camera.apply(sprite)

    # Создание групп спрайтов для удобного обновления и отображения
    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    tile_money = pygame.sprite.Group()
    tile_life = pygame.sprite.Group()
    tile_water = pygame.sprite.Group()
    exit_group = pygame.sprite.Group()
    klad_group = pygame.sprite.Group()

    def level1():
        with open('levels\level1.txt', 'r') as file:
            # Чтение каждой строки файла и добавление ее в массив strings
            for line in file:
                # Добавление строки в массив strings (удаление символа новой строки '\n')
                level.append(line.rstrip())
        zilk()

    def level2():
        with open('levels\level2.txt', 'r') as file:
            # Чтение каждой строки файла и добавление ее в массив strings
            for line in file:
                # Добавление строки в массив strings (удаление символа новой строки '\n')
                level.append(line.rstrip())
        zilk()

    def level3():
        with open('levels\level3.txt', 'r') as file:
            # Чтение каждой строки файла и добавление ее в массив strings
            for line in file:
                # Добавление строки в массив strings (удаление символа новой строки '\n')
                level.append(line.rstrip())
        zilk()

    def zilk():
        x = y = 0
        for row in level:
            for col in row:
                if col == "b":  # Блок
                    tile = Tile(x, y, "block")
                    all_sprites.add(tile)
                    tiles_group.add(tile)
                elif col == "c":  # Монетка
                    tile = Tile(x, y, "coin")
                    all_sprites.add(tile)
                    tile_money.add(tile)
                elif col == "j":  # Жизнь
                    tile = Tile(x, y, "life")
                    all_sprites.add(tile)
                    tile_life.add(tile)
                elif col == "p":  # Поверхность земли
                    tile = Tile(x, y, "pov_earth")
                    all_sprites.add(tile)
                    tiles_group.add(tile)
                elif col == "w":  # Поверхность воды
                    tile = Tile(x, y, "pov_water")
                    all_sprites.add(tile)
                    tile_water.add(tile)
                elif col == "e":  # Земля под поверхностью земли
                    tile = Tile(x, y, "earth")
                    all_sprites.add(tile)
                    tiles_group.add(tile)
                elif col == "v":  # Вода под поверхностью воды
                    tile = Tile(x, y, "water")
                    all_sprites.add(tile)
                    tile_water.add(tile)
                elif col == "x":  #
                    tile = Tile(x, y, "exit_level")
                    all_sprites.add(tile)
                    exit_group.add(tile)
                elif col == "k":  #
                    tile = Tile(x, y, "klad")
                    all_sprites.add(tile)
                    klad_group.add(tile)
                x += 72
            y += 73
            x = 0

    # Создание игрока
    player = Player(tiles_group, tile_money, tile_life, tile_water, exit_group, klad_group)
    all_sprites.add(player)

    class Camera:
        # зададим начальный сдвиг камеры
        def __init__(self):
            self.dx = 0
            self.rect = player.image.get_rect()

        # сдвинуть объект obj на смещение камеры
        def apply(self, obj):
            obj.rect.x += self.dx

        # позиционировать камеру на объекте target
        def update(self, target):
            self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 3)

    camera = Camera()

    # Цикл игры
    running = True
    clock = pygame.time.Clock()

    if level_int == 1:
        level1()

    bg_sound = pygame.mixer.Sound('sounds/fon.mp3')
    bg_sound.play(-1)

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.camera()

        if player.exit_hit:
            # Если это последний уровень, то игра завершается с победой
            if level_int == 4:
                WIN()
                # print("Молодец! Возьми с полки пирожок")
            else:
                # Иначе переходим на следующий уровень
                level_int += 1
                level = []
                if level_int == 2:
                    level2()  # ненадолго проиграл
                    player.exit_hit = False
                    # Отрисовка игрового окна
                    background_image = pygame.image.load('images/fon2.png')
                    background_image = pygame.transform.scale(background_image, size)
                elif level_int == 3:
                    level3()  # ненадолго проиграл
                    player.exit_hit = False
                    background_image = pygame.image.load('images/fon3.png')
                    background_image = pygame.transform.scale(background_image, size)

        # Обновление игрока
        player.update()

        # Проверка, не упал ли игрок или закончились ли у него жизни
        if player.lives <= 0:
            WASTED()
            running = False

        # Отрисовка игрового окна
        screen.blit(background_image, (0, 0))
        all_sprites.draw(screen)
        exit_group.draw(screen)
        # Обработка столкновения игрока с монеткой
        player.collect_coin()
        player.collect_life()
        player.lose_life()
        player.collect_exit_level()

        # Отрисовка счета и жизней игрока
        score_text = f"{player.score}x"
        lives_text = f"{player.lives}x"
        score_label = pygame.font.SysFont(None, 100).render(score_text, True, WHITE)
        lives_label = pygame.font.SysFont(None, 100).render(lives_text, True, WHITE)
        exit_group.draw(screen)
        screen.blit(score_label, (10, 15))
        screen.blit(lives_label, (WIDTH - lives_label.get_width() - 90, 15))

        # Отображение изображения на экране
        screen.blit(live_image, (1100, 10))
        if level_int == 1:
            screen.blit(level1_image, (10, 100))
        elif level_int == 2:
            screen.blit(level2_image, (10, 100))
        elif level_int == 3:
            screen.blit(level3_image, (10, 100))
        screen.blit(coin_image, (150, 10))
        pygame.display.flip()

    pygame.quit()

def START():
    img_game = pygame.image.load('images/start.png')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        screen.blit(pygame.transform.scale(img_game, [1200, 670]), [0, 0])
        pygame.display.flip()

def men():
    # классс стартового меню
    class StartMenu:
        # функция для создания кнопки потом передадим x, y, width, height, kartinka, text - это параметры
        # для кнопок
        def __init__(self, x, y, width, height, kartinka, text):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.kartinka = pygame.image.load(kartinka)
            self.kartinka = pygame.transform.scale(self.kartinka, (width, height))
            self.text = text

        # функция для создания надписей посередине кнопок
        def text_on_knopki(self, screen):
            font = pygame.font.Font(None, 38)
            text = font.render(self.text, 1, (255, 255, 255))
            knopka = pygame.Rect(self.x, self.y, self.width, self.height)
            screen.blit(self.kartinka, knopka)
            screen.blit(text, (self.x + (self.width - text.get_width()) // 2,
                               self.y + (self.height - text.get_height()) // 2))

        # функция для создания звука при нажатии на кнопки меню

        def clicking(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if (knopka_start.proverka_clicking(pygame.mouse.get_pos()) or
                        knopka_output.proverka_clicking(pygame.mouse.get_pos()) or
                        knopka_levels.proverka_clicking(pygame.mouse.get_pos()) or
                        knopka_coin.proverka_clicking(pygame.mouse.get_pos()) or
                        knopka_strelka.proverka_clicking(pygame.mouse.get_pos())):
                    self.sound = pygame.mixer.Sound('sounds/sound_knopka.mp3')
                    self.sound.play()

        # функция для проверки нажатия на кнопки проверяем по координатам
        # попали ли мы по кнопке

        def proverka_clicking(self, pos):
            return self.x < pos[0] < self.x + self.width and \
                self.y < pos[1] < self.y + self.height

    # функция для создания шрифта размера и цвета надписей на кнопках
    def text_name_game(screen):
        font = pygame.font.Font(None, 60)
        text = font.render('В поисках утерянного клада', 1, (0, 100, 0))
        screen.blit(text, (WIDTH / 2 - (520 / 2), 80))

    def count_coins():
        # функция для создания эклана игры
        pygame.init()
        size = width, height = 1187, 660
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Собранные монеты')

        kartinka = pygame.image.load('images/yellow_fon.jpg')
        kartinka = pygame.transform.scale(kartinka, (size))

        font_count_coins = pygame.font.Font(None, 42)
        count_coins_text = font_count_coins.render(f'Лучший результат:36монет', 1, (0, 0, 0))
        # knopka_strelka = StartMenu(WIDTH / 2 - (600 / 2), 450, 100, 70, 'images/strelka.png', '')
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                knopka_strelka.clicking(event)
            screen.fill((255, 255, 255))
            screen.blit(kartinka, (0, 0))
            # knopka_strelka.text_on_knopki(screen)
            screen.blit(count_coins_text, (450, 170))
            pygame.display.flip()

        pygame.quit()

    def yrowni():
        pygame.init()
        size = width, height = 1187, 660
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Уровни')
        font_count_coins = pygame.font.Font(None, 70)

        count_coins_text = font_count_coins.render('Первый уровень', 1, (0, 0, 0))
        count1_coins_text = font_count_coins.render('Второй уровень', 1, (0, 0, 0))
        count2_coins_text = font_count_coins.render('Третий уровень', 1, (0, 0, 0))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            screen.blit(foto_fona, (0, 0))
            screen.blit(count_coins_text, (320, 170))
            screen.blit(count1_coins_text, (320, 270))
            screen.blit(count2_coins_text, (320, 370))
            pygame.display.flip()

        pygame.quit()

    if __name__ == "__main__":
        pygame.init()
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Старт')

        # передаём пораметры для создания кнопок (класс Menu функция __init__)
        knopka_start = StartMenu(WIDTH / 2 - (251 / 2), 150, 252, 120, 'images/Knopka.png', 'Начать игру')
        knopka_output = StartMenu(WIDTH / 2 - (251 / 2), 250, 252, 120, 'images/Knopka.png', 'Выйти из игры')
        knopka_levels = StartMenu(WIDTH / 2 - (251 / 2), 350, 252, 120, 'images/Knopka.png', 'Уровни')
        knopka_coin = StartMenu(WIDTH / 2 - (80 / 2), 470, 70, 50, 'images/coins.png', '')
        knopka_strelka = StartMenu(WIDTH / 2 - (150 / 2), 450, 100, 70, 'images/strelka.png', '')

        foto_fona = pygame.image.load('images/fon_menu.png')
        foto_fona = pygame.transform.scale(foto_fona, (size))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                knopka_start.clicking(event)  # чтобы кнопка кликалась со звуком
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if knopka_start.proverka_clicking(pygame.mouse.get_pos()):
                        START()
                        igra()
                    if knopka_output.proverka_clicking(pygame.mouse.get_pos()):
                        terminate()
                    if knopka_coin.proverka_clicking(pygame.mouse.get_pos()):
                        count_coins()
                    if knopka_levels.proverka_clicking(pygame.mouse.get_pos()):
                        yrowni()
            screen.fill((0, 0, 0))
            screen.blit(foto_fona, (0, 0))

            knopka_start.text_on_knopki(screen)  # отображаем кнопки на экране
            knopka_output.text_on_knopki(screen)
            knopka_levels.text_on_knopki(screen)
            knopka_coin.text_on_knopki(screen)

            text_name_game(screen)

            pygame.display.flip()
        pygame.quit()


# Заставка
def zastavka():
    img_game = pygame.image.load('images/zastavka.png')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                men()
        screen.blit(pygame.transform.scale(img_game, [1200, 670]), [0, 0])
        pygame.display.flip()


zastavka()


def yellow():
    img_game = pygame.image.load('images/yellow_fon.jpg')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                men()
        screen.blit(pygame.transform.scale(img_game, [1200, 670]), [0, 0])
        pygame.display.flip()


yellow()

