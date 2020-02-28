import os
import pygame
from pygame import image
from random import randint


BLACK = (0, 0, 0)
WHITE = (255,255,255)

pygame.init()

x = 365
y = 100
velocidade = 10

#coordenadas dos bots 
pos_x = 480
pos_x_b = 260
pos_x_c = 375

pos_y = 700
pos_y_b = 700
pos_y_c = 700
velocidade_bots = 12

timer = 0
tempo_segundo = 0

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

fonte = pygame.font.SysFont('arial black', 30 ) #procurar fonte no sistema sysFont('fonte', tamanho)
texto = fonte.render(' Tempo | 0 ' , True, (255,255,255), (0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (65, 50)


pygame.display.set_caption('Novo Jogo')

fundo = pygame.image.load(os.path.join('game1','fundo1.png'))
carro = pygame.image.load(os.path.join('game1','carrinho_amarelo3.png'))

#carregando outros carrinhos

policia = pygame.image.load(os.path.join('game1','carrinho_police.png'))
ambulancia = pygame.image.load(os.path.join('game1','ambulancia.png'))
pickup = pygame.image.load(os.path.join('game1','carrinho_pickup.png'))


clock = pygame.time.Clock()

running = True

while running:

    pygame.time.delay(20) # o fluxo retorna aqui a cada 20 milisegundos
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

    comandos = pygame.key.get_pressed()
    if (comandos[pygame.K_UP] | comandos[pygame.K_w]) and y >= -70 :
        y -= velocidade
    if comandos[pygame.K_DOWN] | comandos[pygame.K_s] and y <= 530 :
        y += velocidade
    if comandos[pygame.K_RIGHT] | comandos[pygame.K_d] and x <= 500:
        x += velocidade
    if comandos[pygame.K_LEFT] | comandos[pygame.K_a] and x >= 230:
        x -= velocidade        


    pos_y -= velocidade_bots         #policia
    pos_y_b -= velocidade_bots - 1   #ambulancia
    pos_y_c -= velocidade_bots + 3   #pickup   
       

    if (pos_y <= -820):
        pos_y = randint(700, 1400)
    if (pos_y_b <= -820):
        pos_y_b = randint(700, 1000) 
    if (pos_y_c <= -820):
        pos_y_c = randint(700, 2200)        

    # logo, o timer sobe 1 a cada 20 milisec.
    # assim, 20 x 50 = 1000 milisec.
    # quando o timer for 50, entraremos no else, 
    if (timer < 50):  
        timer += 1 
    else:
        tempo_segundo += 1
        texto = fonte.render(' Tempo | ' + str(tempo_segundo) +' ', True, (255,255,255), (0,0,0))
        timer = 0

    screen.blit(fundo,(0, 0))
    screen.blit(carro, (x,y))
    screen.blit(policia, (pos_x, pos_y))
    screen.blit(ambulancia, (pos_x_b , pos_y_b + 400))
    screen.blit(pickup, (pos_x_c , pos_y_c + 240))
    screen.blit(texto, pos_texto)

    print(timer)
    pygame.display.update()
 

pygame.quit()

