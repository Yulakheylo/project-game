import pygame

SIZE = WIDTH, HEIGHT = 600, 600


class Game:
    def __init__(self):
        pass

    def screen_igra(self):
        if __name__ == '__main__':
            pygame.init()
            size = width, height = 1000, 600
            screen = pygame.display.set_mode(size)
            pygame.display.set_caption('Игра')

            kartinka = pygame.image.load('images/fon.png')
            kartinka = pygame.transform.scale(kartinka, (size))

            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                screen.fill((255, 255, 255))
                screen.blit(kartinka, (0, 0))
                pygame.display.flip()
            pygame.quit()


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
    screen.blit(text, (120, 80))


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Старт')

    knopka_start = Knopka(WIDTH / 2 - (251 / 2), 150, 252, 120, 'images/Кнопка.png', 'Начать игру')
    knopka_output = Knopka(WIDTH / 2 - (251 / 2), 250, 252, 120, 'images/Кнопка.png', 'Выйти из игры')
    knopka_levels = Knopka(WIDTH / 2 - (251 / 2), 350, 252, 120, 'images/Кнопка.png', 'Уровни')
    knopka_coin = Knopka(270, 470, 70, 50, 'images/coins.png', '')

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