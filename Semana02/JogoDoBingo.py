import random
from math import ceil
import time
class Jogador():
    def __init__(self, nome: str):
        self._nome = nome 
        self._cartela = {'disponiveis': [], 'marcados':[]}
    @property
    def get_nome(self) -> str:
        return self._nome

    def receber_cartela(self, numeros: list):
        self._cartela['disponiveis'] = numeros
    
    def marcar(self, numero):
        if numero in self._cartela['disponiveis'] and len(self._cartela['disponiveis']) > 0:
            self._cartela['disponiveis'].remove(numero)
            self._cartela['marcados'].append(numero)
            return True

    def faltantes(self):
        return self._cartela['disponiveis']

    def imprimir(self):
        print(f'-> {self._nome}: ')
        print('Números não marcados: ')
        for numeros in self._cartela['disponiveis']:
            print(f"{numeros}|", end='')

class Bingo:
    quantidade = 20
    numeros_jogo = {'disponiveis': list(), 'sorteados': list()}
    jogadores: dict[str, list[Jogador]] = {'no_jogo': [], 'vencedores': []}
    @classmethod
    def cria_numeros_jogos(cls):
        todos_numeros = list(range(cls.quantidade))
        random.shuffle(todos_numeros)
        cls.numeros_jogo['disponiveis'] = todos_numeros
    @classmethod
    def adiciona_jogadores(cls, lista: list[Jogador]):
        cls.jogadores['no_jogo'] = lista
        for jogador in lista:
            porcent = ceil((25/100)*(cls.quantidade))
            cartela = random.sample(cls.numeros_jogo['disponiveis'],porcent)
            jogador.receber_cartela(cartela)
    def __init__(self, lista_jogadores: list):
        self.cria_numeros_jogos()
        self.adiciona_jogadores(lista_jogadores)
    def sortear(self):
        numero_sorteado = self.numeros_jogo['disponiveis'].pop()
        print(f"Número sorteado -> {numero_sorteado}")
        [jogador.marcar(numero_sorteado) for jogador in self.jogadores['no_jogo']]
        self.numeros_jogo['sorteados'].append(numero_sorteado)
        self.verifica_bingo()
        pass
    def verifica_bingo(self):
        for jogador in self.jogadores['no_jogo']:
            if len(jogador.faltantes()) <= 0:
                print("== BINGO! BINGO! ==")
                print(f"{jogador.get_nome} fez BINGO!")
                self.jogadores['vencedores'].append(jogador.get_nome)
                self.jogadores['no_jogo'].remove(jogador)
                return True
        return False
    def imprime(self) -> str:
        print('\n' * 20)
        print("== Resumo do Bingo ==")
        print('-> Número já sorteados: ')
        print(f" {self.numeros_jogo['sorteados']}\n", end='')
        print("Jogadores no jogo: ")
        for jogador in self.jogadores['no_jogo']:
            print(f"  -> {jogador.get_nome}: ")
            print(f"{jogador.faltantes()}", end='\n')

    def menu(self):
        print("=======================")
        print("=====    Bingo    =====")
        print("=======================")
        print('1. Adicionar jogador.')
        print('2. Começar.')

        return int(input('Opção: '))

    def jogar(self, lista):
        on_game = False
        while True:
            escolha = self.menu()
            match escolha:
                case 1: 
                    while True:
                        print("\n== Adicionando o jogador ==")
                        nome = input("Nome: ")
                        novo_jogador = Jogador(nome)
                        self.jogadores['no_jogo'].append(novo_jogador)

                        resp = input("Adicionar outro jogador? (S/N): ")
                        if resp.lower() == 's':
                            continue
                        else: on_game = True; break
                case 2:
                    if len(self.jogadores['no_jogo']) <= 0:
                        print("Sem jogadores.")
                        continue

                    self.adiciona_jogadores(lista)
                    break
        while on_game:
            print("Sorteado",end='')
            for _ in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
            self.sortear()
            if not self.verifica_bingo():
                self.imprime()
                input("Pressione enter para prosseguir...")
                continue
            else:on_game = False; break
            

lista_jogadores = []
bingo = Bingo(lista_jogadores)
bingo.jogar(lista_jogadores)