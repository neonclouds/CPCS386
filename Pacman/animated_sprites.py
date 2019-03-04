import pygame
import sys, os



class AnimatedSprite(pygame.sprite.Sprite):

    def __init__(self, position):
        """
        Animated sprite object.

        Args:
            position: x, y coordinate on the screen to place the AnimatedSprite.
            images: Images to use in the animation.
        """
        super(AnimatedSprite, self).__init__()

        size = (34, 34)

        self.images = [pygame.image.load('images/p0.png'),
                  pygame.image.load('images/p1.png'),
                  pygame.image.load('images/p2.png'),
                  pygame.image.load('images/p3.png'),
                  pygame.image.load('images/p4.png'),
                  pygame.image.load('images/p5.png'),
                  pygame.image.load('images/p6.png'),
                  pygame.image.load('images/p7.png'),
                  pygame.image.load('images/p8.png'),
                  pygame.image.load('images/p9.png'),
                  pygame.image.load('images/p10.png'),
                  pygame.image.load('images/p11.png'),
                  pygame.image.load('images/p12.png'),
                  pygame.image.load('images/p13.png')]

        self.rect = pygame.Rect(position, size)
        self.images_right = self.images
        self.images_left = [pygame.transform.flip(image, True, False) for image in self.images]  # Flipping every image.
        self.index = 0
        self.image = self.images[self.index]  # 'image' is the current image of the animation.

        self.velocity = pygame.math.Vector2(0, 0)

        self.animation_time = 0.1
        self.current_time = 0

        self.animation_frames = 6
        self.current_frame = 0