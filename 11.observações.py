"""

Reparei que o carregamento das imagens só é bem sucedido quando abro o diretório 'game' aqui no VSCode
Se eu abrir direto 'game1', ou então um diretório superior como por exemplo o VSCode/ ou Unigranrio/,
o método pygame.image.load() simplesmente não funciona

outra coisa importante para o carregamento correto de imagens foi o uso do os.path.join()
pelo que entendi, esse método forma o path, adicionando o nome diretório junto ao nome da imagem
assim:
        carro = pygame.image.load(os.path.join('game1','carrinho_amarelo3.png'))

gera o caminho 'game1/carrinho_amarelo3.png'


"""