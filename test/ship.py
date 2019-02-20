import pygame

class Ship():

    def __init__(self, screen):
        """"Initialize the ship and set its starting position."""
        super(Ship, self).__init__()

        self.screen = screen

        #load the ship image and get its rect.
        self.image = pygame.image.load('images/player0.png')
        self.monster1 = pygame.image.load('images/tentacle0.png')
        self.monster2 = pygame.image.load('images/crab0.png')
        self.monster3 = pygame.image.load('images/octopus0.png')
        self.monster4 = pygame.image.load('images/mothership.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def create_main_menu(self):
        self.screen.blit(self.monster1, (400, 170))
        self.screen.blit(self.monster2, (400, 220))
        self.screen.blit(self.monster3, (400, 270))
        self.screen.blit(self.monster4, (400, 320))

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx