from nave import Nave


class Jogador(Nave):
    def __init__(self,imagem):
        super().__init__(imagem)

    def mover(self,direcao):
        if direcao == "direita" or direcao == "esquerda":
            super().mover(direcao)
