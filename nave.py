from objeto import Objeto
from pygame import mixer


class Nave(Objeto):
    def __init__(self,imagem):
        super().__init__(imagem)
        self.__pontos_de_vida = 100
        self.__disparos = []
        self.__efeito = mixer.Sound("audios\\tiroinimigo.ogg")

    def disparar(self):
        minhaBala = Objeto('imagens\\balaouro.png')
        rect = self.get_rect()
        minhaBala.get_rect().centerx = rect.centerx
        minhaBala.get_rect().centery = rect.centery
        self.__disparos.append(minhaBala)
        self.__efeito.play()

    def perde_vida(self):
        self.__pontos_de_vida -= 10

    def remove_disparo(self,disparo):
        self.__disparos.remove(disparo)

    def get_pontos_de_vida(self):
        return self.__pontos_de_vida

    def set_pontos_de_vida(self,amount):
        self.__pontos_de_vida = amount

    def get_disparos(self):
        return self.__disparos

    def set_disparos(self,amount):
        self.__disparos = amount

    def get_efeito(self):
        return self.__efeito

    def set_efeito(self, amount):
        self.__efeito = amount
