from pygame import *

class Objeto(sprite.Sprite):
    def __init__(self, imagem):
        super(sprite.Sprite, self).__init__()
        self.__velocidade = 20
        self.__imagem = image.load(imagem)
        self.__rect = self.__imagem.get_rect()

    def colocar(self, superfice):
        superfice.blit(self.__imagem, self.__rect)

    def mover(self, direcao):
        if direcao == "direita":
            self.__rect.right += self.__velocidade
            if self.__rect.right > 950:
                self.__rect.right = 950
        if direcao == "esquerda":
             self.__rect.left -= self.__velocidade
             if self.__rect.left <= 0:
                self.__rect.left = 0
        if direcao == "cima":
            self.__rect.top -= self.__velocidade
            if self.__rect.top <= 0:
                self.__rect.top = 0
        if direcao == "baixo":
            self.__rect.low += self.__velocidade
            if self.__rect.low > 700:
                self.__rect.low = 700

    def get_velocidade(self):
        return self.__velocidade

    def set_velocidade(self,amount):
        self.__velocidade = amount

    def get_imagem(self):
        return self.__imagem

    def set_imagem(self,amount):
        self.__imagem = amount

    def get_rect(self):
        return self.__rect

    def set_rect(self, amount):
        self.__rect = amount
