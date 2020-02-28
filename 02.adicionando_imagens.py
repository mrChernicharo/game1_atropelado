import os
import pygame
from pygame import image


BLACK = (0, 0, 0)

pygame.init()

x = 365
y = 300
velocidade = 10


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))



pygame.display.set_caption('Novo Jogo')

fundo = pygame.image.load(os.path.join('game1','fundo1.png'))
carro = pygame.image.load(os.path.join('game1','carrinho_amarelo3.png'))



#surface = pygame.Surface((100, 100))
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


    #screen.fill(BLACK)
    screen.blit(fundo,(0, 0))
    screen.blit(carro, (x,y))
   

    #pygame.draw.circle(screen, (0, 255, 0), (x, y), 30)
    pygame.display.update()
 

pygame.quit()

