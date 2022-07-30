import pygame

class Sapo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = [
                 pygame.image.load('classes/sprites/attack_1.png')
                ,pygame.image.load('classes/sprites/attack_2.png')
                ,pygame.image.load('classes/sprites/attack_3.png')
                ,pygame.image.load('classes/sprites/attack_4.png')
                ,pygame.image.load('classes/sprites/attack_5.png')
                ,pygame.image.load('classes/sprites/attack_6.png')
                ,pygame.image.load('classes/sprites/attack_7.png')
                ,pygame.image.load('classes/sprites/attack_8.png')
                ,pygame.image.load('classes/sprites/attack_9.png')
                ,pygame.image.load('classes/sprites/attack_10.png')
        ]

        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (128*3, 64*3))
        self.animado = False
        self.rect = self.image.get_rect()
        self.rect.topleft = 250, 150

    def atacar(self):
        self.animado = True

    def update(self):
        if self.animado:
            self.atual = self.atual + 0.025
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animado = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (128*3, 64*3))