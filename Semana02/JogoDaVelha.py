from random import random
class Tabuleiro():
    def __init__(self):
        self._posicoes = [
            [' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' ']
        ]

    def jogada(self, posicao: str, simbolo:str):
        try:
            posicao = posicao.strip()
            linha = int(posicao[0]) - 1
            letra = posicao[1].upper()
            coluna = ord(letra) - ord('A')
            if self._posicoes[linha][coluna] == ' ':
                self._posicoes[linha][coluna] = simbolo
                return True
        except:
            pass
        return False

    def todas_linhas(self):
        todas = []
        # Pegando as linhas horizontais
        for linha in self._posicoes:
            todas.append(tuple(linha))
        # Pegando as colunas 
        for cont in range(3):
            colunas = [self._posicoes[0][cont],
                       self._posicoes[1][cont],
                       self._posicoes[2][cont]]
            todas.append(tuple(colunas))

        # Pegando as diagonais
        diagonal = []
        transversal = [] 
        for cont in range(3):
            diagonal.append(self._posicoes[cont][cont])
            transversal.append(self._posicoes[2-cont][cont])
        todas.append(tuple(diagonal))
        todas.append(tuple(transversal))
        return todas 


    def tem_jogada(self):
        for linha in self._posicoes:
            if ' ' in linha:
                return True
        return False

    def imprime(self):
        print("\n   A    B   C ")
        print("  ┌───┬───┬───┐")
        for count, linha in enumerate(self._posicoes):
            print(f"{count + 1} │ " + " │ ".join(linha) + " │")
            if count < len(self._posicoes) - 1:
                print("  ├───┼───┼───┤")
        print("  └───┴───┴───┘")


class Velha: 
    def __init__(self):
        self._tabuleiro = Tabuleiro()
        if random() > 0.5:
            self._jogador = 'X'
        else: self._jogador = 'O'

    def jogar(self):
        while self._tabuleiro.tem_jogada():
            self.pega_jogada()
            if self.eh_vencedor(self._jogador):
                print("Fim de jogo!")
                print(f"{self._jogador} venceu!")
                return
            self.troca_jogador()


    def troca_jogador(self):
        if self._jogador == 'X':
            self._jogador = 'O'
        else: self._jogador = 'X'
    def pega_jogada(self):
        while True:
            self.imprime()
            print(f"Vez do Jogador {self._jogador}.")
            posicao = input("Digite a posição(Ex: 2B): ")
            if self._tabuleiro.jogada(posicao, self._jogador):
                break
    def eh_vencedor(self, jogador):
        linhas = self._tabuleiro.todas_linhas()
        if tuple([jogador, jogador, jogador]) in linhas:
            return True
        return False
    def imprime(self):
        print("\n"*50)
        print("== Jogo da Velha ==")
        self._tabuleiro.imprime()

jogo = Velha()
jogo.jogar()