import numpy as np
from copy import copy
class Nodo:
    def __init__(self, estado, p, raiz=False, jogada = []):
        self.estado = estado
        self.player = p
        self.filhos = []
        self.__raiz = raiz
        self.valor = 0
        self.jogada = jogada

        if not self.__estado_final() and self.checa_objetivo_final() == 0:
            self.cria_filhos(self.player)

    @property
    def raiz(self):
        return self.__raiz

    @raiz.setter
    def raiz(self, nova_raiz):
        self.__raiz = nova_raiz

    def __estado_final(self):
        for x in range(0, 3):
            for y in range(0, 3):
                if self.estado[x][y] == 0:
                    return False
        return True

    def cria_filhos(self, player_anterior):
        player = self.__inverte_jogador(player_anterior)
        referencia = self.estado
        for x in range(0, 3):
            for y in range(0, 3):
                if referencia[x][y] == 0:
                    aux = copy(referencia)
                    aux[x][y] = player_anterior
                    jogada = [copy(x), copy(y)]
                    novo_nodo = Nodo(aux, player,jogada=jogada)
                    self.filhos.append(novo_nodo)

    @staticmethod
    def __inverte_jogador(player):
        if player == 1:
            return 2
        elif player == 2:
            return 1

    def checa_objetivo_final(self):
        # Complete line?
        for i in range(3):
            s = set(self.estado[i, :])
            if len(s) == 1 and min(s) != 0:
                return s.pop()

        # Complete column?
        for i in range(3):
            s = set(self.estado[:, i])
            if len(s) == 1 and min(s) != 0:
                return s.pop()

        # Complete diagonal (main)?
        s = set([self.estado[i, i] for i in range(3)])
        if len(s) == 1 and min(s) != 0:
            return s.pop()

        # Complete diagonal (opposite)?
        s = set([self.estado[-i - 1, i] for i in range(3)])
        if len(s) == 1 and min(s) != 0:
            return s.pop()

        # nope, not an objective state
        return 0

    def minimax(self):
        if len(self.filhos) != 0:
            for filho in self.filhos:
                filho.minimax()

        if self.__estado_final() or self.checa_objetivo_final() != 0:
            aux = self.checa_objetivo_final()
            if aux == 1:
                self.valor = 1
            elif aux == 2:
                self.valor = -1
            return

        vetor_possibilidades = []
        for filho in self.filhos:
            vetor_possibilidades.append(filho.valor)
        if self.player == 1:
            self.valor = max(vetor_possibilidades)
            return
        else:
            self.valor = min(vetor_possibilidades)
            return


class Arvore:
    def __init__(self):
        estado_inicial = np.zeros((3,3))
        self.raiz = Nodo(estado_inicial,1)
        self.raiz.minimax()



#arv = Arvore()
#print('Estado inicial:\n {}, \njogador: {}\n'.format(arv.raiz.estado, arv.raiz.player))
#for filh in arv.raiz.filhos:
#    print('filho:\n {},\n jogada: {}\n'.format(filh.estado, filh.jogada))
#    print()