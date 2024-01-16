import pygame
import sys
import os

FPS = 50
size = WIDTH, HEIGHT = 1187, 660
SIZE = WIDTH, HEIGHT = 1187, 660

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


class Game:
    def screen_igra(self):
        if __name__ == '__main__':
            pygame.init()
            size = width, height = 1187, 660
            screen = pygame.display.set_mode(size)
            pygame.display.set_caption('Игра')

            kartinka = pygame.image.load('images/fon.png')
            kartinka = pygame.transform.scale(kartinka, (SIZE))

            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                screen.fill((255, 255, 255))
                screen.blit(kartinka, (0, 0))
                pygame.display.flip()
            pygame.quit()


class StartMenu:
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
    font = pygame.font.Font(None, 60)
    text = font.render('В поисках утерянного клада', 1, (0, 100, 0))
    screen.blit(text, (WIDTH / 2 - (520 / 2), 80))


# class FinishMenu:
#     def __init__(self, x, y, width, height, kartinka, text):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.kartinka = pygame.image.load(kartinka)
#         self.kartinka = pygame.transform.scale(self.kartinka, (width, height))
#         self.text = text
#
#     def text_on_knopki(self, screen):
#         font = pygame.font.Font(None, 38)
#         text = font.render(self.text, 1, (255, 255, 255))
#         knopka = pygame.Rect(self.x, self.y, self.width, self.height)
#         screen.blit(self.kartinka, knopka)
#         screen.blit(text, (self.x + (self.width - text.get_width()) // 2,
#                            self.y + (self.height - text.get_height()) // 2))
#
#     def clicking(self, event):
#         if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#             if (knopka_finish.proverka_clicking(pygame.mouse.get_pos()) or
#                     knopka_next_level.proverka_clicking(pygame.mouse.get_pos())):
#                 self.sound = pygame.mixer.Sound('sounds/sound_knopka.mp3')
#                 self.sound.play()
#
#     def proverka_clicking(self, pos):
#         return self.x < pos[0] < self.x + self.width and \
#             self.y < pos[1] < self.y + self.height
#
#
# def text_name_game(screen):
#     font = pygame.font.Font(None, 60)
#     font_coins = pygame.font.Font(None, 34)
#     text = font.render('Уровень пройден!', 1, (255, 255, 255))
#     collected_coins = font_coins.render('Вы собрали монет:', 1, (255, 255, 255))
#     screen.blit(text, (WIDTH / 2 - (350 / 2), 80))
#     screen.blit(collected_coins, (WIDTH / 2 - (200 / 2), 170))
#
#
# if __name__ == '__main__':
#     pygame.init()
#     size = width, height = 1187, 660
#     screen = pygame.display.set_mode(size)
#     pygame.display.set_caption('Меню выход')
#
#     foto_fona = pygame.image.load('images/fon_finish.png')
#     foto_fona = pygame.transform.scale(foto_fona, (size))
#
#     knopka_next_level = FinishMenu(WIDTH / 2 - (251 / 2), 250, 252, 80, 'images/Knopka_finish.png', 'Новый уровень')
#     knopka_finish = FinishMenu(WIDTH / 2 - (251 / 2), 360, 252, 80, 'images/Knopka_finish.png', 'Завершить игру')
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             knopka_finish.clicking(event)
#             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#                 if knopka_finish.proverka_clicking(pygame.mouse.get_pos()):
#                     zastavka()
#             knopka_next_level.clicking(event)
#         screen.fill((0, 0, 0))
#         screen.blit(foto_fona, (0, 0))
#
#         knopka_finish.text_on_knopki(screen)
#         knopka_next_level.text_on_knopki(screen)
#
#         text_name_game(screen)
#
#         pygame.display.flip()
#     pygame.quit()

class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)


camera = Camera()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Старт')

    knopka_start = StartMenu(WIDTH / 2 - (251 / 2), 150, 252, 120, 'images/Knopka.png', 'Начать игру')
    knopka_output = StartMenu(WIDTH / 2 - (251 / 2), 250, 252, 120, 'images/Knopka.png', 'Выйти из игры')
    knopka_levels = StartMenu(WIDTH / 2 - (251 / 2), 350, 252, 120, 'images/Knopka.png', 'Уровни')
    knopka_coin = StartMenu(WIDTH / 2 - (80 / 2), 470, 70, 50, 'images/coins.png', '')
    # knopka_finish = FinishMenu(WIDTH / 2 - (251 / 2), 350, 252, 120, 'images/Knopka.png', 'Завершить игру')

    game = Game()
    # finish_menu = FinishMenu()

    foto_fona = pygame.image.load('images/fon_menu.jpg')
    foto_fona = pygame.transform.scale(foto_fona, (size))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            knopka_start.clicking(event)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if knopka_start.proverka_clicking(pygame.mouse.get_pos()):
                    game.screen_igra()
        screen.fill((0, 0, 0))
        screen.blit(foto_fona, (0, 0))

        knopka_start.text_on_knopki(screen)
        knopka_output.text_on_knopki(screen)
        knopka_levels.text_on_knopki(screen)
        knopka_coin.text_on_knopki(screen)
        # knopka_finish.text_on_knopki(screen)

        text_name_game(screen)

        pygame.display.flip()
    pygame.quit()
