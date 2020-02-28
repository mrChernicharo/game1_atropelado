import pygame
import random


BLACK = (0, 0, 0)

pygame.init()
x = 400
y = 300
velocidade = 10

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Novo Jogo')

surface = pygame.Surface((100, 100))
clock = pygame.time.Clock()

running = True

while running:

    pygame.time.delay(25)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP] | comandos[pygame.K_w]:
        y -= velocidade
    if comandos[pygame.K_DOWN] | comandos[pygame.K_s]:
        y += velocidade
    if comandos[pygame.K_RIGHT] | comandos[pygame.K_d]:
        x += velocidade
    if comandos[pygame.K_LEFT] | comandos[pygame.K_a]:
        x -= velocidade        

    screen.fill(BLACK)
    pygame.draw.circle(screen, (0, 255, 0), (x, y), 30)
    pygame.display.update()
 

pygame.quit()

"""
se a linha comandos = pygame.key.get_pressed() e todos os seus ifs etivesse indentada dentro do for event...
isso impediria o movimento caso segurássemos a tecla. tirando ela do for, aí sim o movimento é contínuo
"""
 
 
