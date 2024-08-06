import pygame


class PygameApp:
    def __init__(self, width, height, title, logger):
        self.width = width
        self.height = height
        self.title = title
        self.logger = logger

        # Inicializar Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
        self.quit()

    def handle_events(self):
        for event in pygame.event.get():
            # logger event
            #self.logger.info(event)
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass  # Lógica de actualización del juego aquí

    def draw(self):
        self.screen.fill((0, 0, 0))  # Dibuja en la pantalla aquí

    def quit(self):
        pygame.quit()