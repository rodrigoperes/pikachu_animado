import pygame

class Pikachu(pygame.sprite.Sprite):
    def __init__(self, nome, sexo, nivel):
        pygame.sprite.Sprite.__init__(self)
        self.nome = nome
        self.sexo = sexo
        self.nivel = nivel
        self.x = 100
        self.y = 100
        self.velocidade = 1
        self.correndo = False
        self.orientacao = 'direita'
        self.sprites = [
                 pygame.image.load('classes/sprites/sprite_pikachu00.png')
        ]
        self.sprites_ataque = [
                 pygame.image.load('classes/sprites/sprite_pikachu01.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu02.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu03.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu04.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu05.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu06.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu07.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu08.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu09.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu10.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu11.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu12.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu13.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu14.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu15.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu16.png')
        ]
        self.sprites_ataque_esq = [
                 pygame.image.load('classes/sprites/sprite_pikachu_esq01.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu_esq02.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu_esq03.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu_esq04.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu_esq05.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu_esq06.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu_esq07.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu_esq08.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu_esq09.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu_esq10.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu_esq11.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu_esq12.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu_esq13.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu_esq14.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu_esq15.png')
                ,pygame.image.load('classes/sprites/sprite_pikachu_esq16.png')
        ]
        self.sprites_corrida = [
             pygame.image.load('classes/sprites/sprite_pikachu17.png')
            ,pygame.image.load('classes/sprites/sprite_pikachu18.png')
            ,pygame.image.load('classes/sprites/sprite_pikachu19.png')
            ,pygame.image.load('classes/sprites/sprite_pikachu20.png')
            ,pygame.image.load('classes/sprites/sprite_pikachu21.png')
        ]
        self.sprites_corrida_esq = [
             pygame.image.load('classes/sprites/sprite_pikachu_esq17.png')
            ,pygame.image.load('classes/sprites/sprite_pikachu_esq18.png')
            ,pygame.image.load('classes/sprites/sprite_pikachu_esq19.png')
            ,pygame.image.load('classes/sprites/sprite_pikachu_esq20.png')
            ,pygame.image.load('classes/sprites/sprite_pikachu_esq21.png')
        ]
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (178*3, 71*3))
        self.animado = False
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y

    def mudar_direcao(self, orientacao):
        if self.animado == False:
            self.orientacao = orientacao
            if self.orientacao == 'direita':
                self.sprites = [pygame.image.load('classes/sprites/sprite_pikachu00.png')]
            elif self.orientacao == 'esquerda':
                self.sprites =  [pygame.image.load('classes/sprites/sprite_pikachu_esq00.png')]
            self.atual = 0
            self.image = self.sprites[self.atual]
            self.image = pygame.transform.scale(self.image, (178*3, 71*3))

    def choque_do_trovao(self):
        self.animado = True
        if self.orientacao == 'direita':
            self.sprites = [self.image] + self.sprites_ataque
        elif self.orientacao == 'esquerda':
            self.sprites = [self.image] + self.sprites_ataque_esq

    def correr(self):
        self.animado = True
        self.correndo = True
        if self.orientacao == 'direita':
            self.sprites = self.sprites_corrida
        elif self.orientacao == 'esquerda':
            self.sprites = self.sprites_corrida_esq

    def parar(self):
        self.animado = False
        self.correndo = False
        if self.orientacao == 'direita':
            self.sprites = [pygame.image.load('classes/sprites/sprite_pikachu00.png')]
        elif self.orientacao == 'esquerda':
            self.sprites =  [pygame.image.load('classes/sprites/sprite_pikachu_esq00.png')]
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (178*3, 71*3))


    def update(self):
        if self.animado:
            self.atual = self.atual + 0.025
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animado = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (178*3, 71*3))
            if self.correndo:
                self.animado = True
                if self.orientacao == 'direita':
                    self.x = self.x + self.velocidade
                elif self.orientacao == 'esquerda':
                    self.x = self.x - self.velocidade
                self.rect.topleft = self.x, self.y

    def falar(self):
        print("Pika Pika!")