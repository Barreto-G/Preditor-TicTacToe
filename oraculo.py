import arvore as ar
import numpy as np

# cada nodo da arvore deve conter um estado e uma sequencia de estados possivies
# tambem deve conter um peso para cada nodo, indicando a maior probabilidade de vitoria,
# de acordo com os ramos que levam a vitoria sem muitas ramificacoes
# tambem eh bom ter uma variavel que indica qual jogador esta jogando em cada estado

class Oraculo:
    def __init__(self):
        self.arvore = ar.Arvore()

    def checa_melhor_jogada(self, jogador):
        if jogador == 1:
            return

        valor_jogadas_possiveis = []
        for filho in self.arvore.raiz.filhos:
            valor_jogadas_possiveis.append(filho.valor)
        play_position = []
        if(max(valor_jogadas_possiveis) == 1):
            melhor_jogada = valor_jogadas_possiveis.index(1)
            play_position = self.arvore.raiz.filhos[melhor_jogada].jogada
        elif max(valor_jogadas_possiveis) == 0:
            melhor_jogada = valor_jogadas_possiveis.index(0)
            play_position = self.arvore.raiz.filhos[melhor_jogada].jogada
        print('Melhor jogada para o jogador 1: {}'.format(play_position))

    def atualiza_raiz(self, estado_atual):
        for filho in self.arvore.raiz.filhos:
            if checa_igualdade(estado_atual, filho.estado):
                self.arvore.raiz = filho
                return

def checa_igualdade(estado1, estado2):
    igualdades = (estado1 == estado2)
    if False not in igualdades:
        return True
    return False
