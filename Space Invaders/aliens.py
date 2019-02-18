import pygame

class Aliens():

    def __init__(self, screen):
        super(Aliens, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.monster1 = pygame.image.load('images/tentacle0.png')
        self.monster2 = pygame.image.load('images/crab0.png')
        self.monster3 = pygame.image.load('images/octopus0.png')
        self.monster4 = pygame.image.load('images/mothership0.png')

    def create_main_menu(self):
        self.screen.blit(self.monster1, (400, 270))
        self.screen.blit(self.monster2, (400, 320))
        self.screen.blit(self.monster3, (400, 370))
        self.screen.blit(self.monster4, (400, 420))
