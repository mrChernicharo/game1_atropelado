import os
import pygame



BLACK = (0, 0, 0)

pygame.init()

x = 365
y = 300
velocidade = 10

#coordenadas dos bots 
pos_x = 480
pos_x_b = 260
pos_x_c = 375

pos_y = 700
pos_y_b = 700
pos_y_c = 700
velocidade_bots = 10

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))



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

    #velocidades diferentes pra cada carro
    pos_y -= velocidade_bots   
    pos_y_b -= velocidade_bots - 2   
    pos_y_c -= velocidade_bots + 3
       

    #caso o carro saia pelo topo da tela, faça-o reaparecer embaixo
    if (pos_y <= -820):
        pos_y = 800
    if (pos_y_b <= -820):
        pos_y_b = 800    
    if (pos_y_c <= -820):
        pos_y_c = 800         

    screen.blit(fundo,(0, 0))
    screen.blit(carro, (x,y))

    #desenhando os outros carrinhos
    
    screen.blit(policia, (pos_x, pos_y))
    screen.blit(ambulancia, (pos_x_b , pos_y_b + 400))
    screen.blit(pickup, (pos_x_c , pos_y_c + 240))


    pygame.display.update()
 

pygame.quit()

