from pygame import *
from jogador import Jogador
from objeto import Objeto
from inimigo import Inimigo


def colocaInimigos():
    for linha in range(6):
        for coluna in range(14):
            inimigos.append(Inimigo('imagens\\inimigo3.png'))
            inimigos[(linha*14) + coluna].get_rect().x = coluna * 67
            inimigos[(linha*14) + coluna].get_rect().y = linha * 70

size = (950, 700)
init()
tela = display.set_mode(size)
display.set_caption("Space Invaders")
fecha_tela = True

try:
    jogador = Jogador('imagens\\nave2.png')
    print('teste')
    inimigos = []
    colocaInimigos()
    imagemfundo = Objeto('imagens\\fundo2.jpeg')
    print('teste3')
except:
    print("Falha ao carregar recursos.")
else:
    jogando = True
    relogio = time.Clock()
    jogador.get_rect().centerx = 475
    jogador.get_rect().centery = 640

    while fecha_tela:
        relogio.tick(50)  # velocidade que a bala vai
        for evento in event.get():
            if evento.type == QUIT:
                fecha_tela = False
            if evento.type == KEYDOWN:  # pega alguem evento do teclado
                if evento.key == K_LEFT:
                    jogador.mover('esquerda')
                elif evento.key == K_RIGHT:
                    jogador.mover('direita')
                elif evento.key == K_SPACE:
                    jogador.disparar()
                elif evento.key == K_ESCAPE:
                    fecha_tela = False

        imagemfundo.colocar(tela)
        for bala in jogador.get_disparos():
            bala.colocar(tela)
            bala.mover('cima')
            for inimigo in inimigos:
                if bala.get_rect().colliderect(inimigo.get_rect()):
                    jogador.remove_disparo(bala)
                    inimigo.destruir()
                    inimigos.remove(inimigo)
                    break
            if bala.get_rect().y <= 0:
                jogador.remove_disparo(bala)
            if inimigos == []:
                colocaInimigos()
        jogador.colocar(tela)  # chama a funçao pra botar as coisas na tela
        for inimigo in inimigos:
            inimigo.colocar(tela)
        display.update()

quit()
