import pygame
from pygame.locals import *
from sys import exit
from classes.Pikachu import Pikachu

pygame.init()

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sprites')

todas_as_sprites = pygame.sprite.Group()
pikachu = Pikachu('Pikachu', 'M', 50)
todas_as_sprites.add(pikachu)

# Loop Principal do Jogo
while True:
    tela.fill('black')
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if pikachu.orientacao == 'direita':
                    pikachu.mudar_direcao('esquerda')
                pikachu.correr()
            if event.key == K_SPACE:
                pikachu.choque_do_trovao()
            if event.key == K_RIGHT:
                if pikachu.orientacao == 'esquerda':
                    pikachu.mudar_direcao('direita')
                pikachu.correr()
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                pikachu.parar()



    todas_as_sprites.update()
    todas_as_sprites.draw(tela)
    
    pygame.display.flip()