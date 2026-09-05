# Jogo da forca Multiplayer 
import time
class Palavra:
    @staticmethod
    def verifica_palavra(palavra):
        for char in palavra:
            if char.isdigit():
                return False
        return True

    @staticmethod
    def pega_sublinhado(palavra):
        sublinhado = list("_" * len(palavra))
        return sublinhado

    def __init__(self, palavra: str, dica: str = ''):
        if not self.verifica_palavra(palavra):
            raise ValueError("Palavra inválida.")

        self._palavra = palavra.strip().lower()
        self._dica = dica

        self._sublinhado = self.pega_sublinhado(self._palavra)


    def tem_letra(self, letra: str):
        letra = letra.strip().lower()
        indices = []
        for ind, letras in enumerate(self._palavra):
            if letra == letras:
                indices.append(ind)

        # Adicionando as letras 
        for ind in indices:
            self._sublinhado[ind] = letra
            
        return len(indices) > 0
    

    def tela(self):
        if self._dica != '': print(f"Dica: {self._dica}.")
        else: print(f"Dica: Sem dicas.")

        for linha in self._sublinhado:
            print(f"{linha} ", end='')

    def completada(self):
        if self._sublinhado == list(self._palavra):
            return True
        return False

class Forca:
    def __init__(self, palavra: Palavra):
        self._palavra = palavra
        self._digitadas = list()
        self._erros = 0

    def eh_letra_valida(self, letra):
        if len(letra) != 1 or letra.isdigit():
            print("Letra inválida.")
            return False
        if letra in self._digitadas:
            print("Letra já ultilizada.")
            return False
        return True
        


    def mostrar(self):
        print("\n"*100)
        print(f"Erros: {self._erros}")
        print(f"Palavras digitadas: {self._digitadas}")
        self._palavra.tela()

    def jogar(self):
        entrada = ''
        while True:
            print("="*10)
            print('Forca Game')
            print("="*10)

            self.mostrar()
            entrada = input("\nDigite uma letra: ")
            if self.eh_letra_valida(entrada):
                if self._palavra.tem_letra(entrada):
                    if self._palavra.completada():
                        break
                else: self._erros += 1;
            else:
                time.sleep(1)
            self._digitadas.append(entrada)
        print("\n"*10)
        print("="*10)
        print("FIM DE JOGO!")
        print(f"A palavra era: {self._palavra._palavra}")
        print(f"QTDE. ERROS  --------- {self._erros}")
        print(f"Palavras digitadas  ------------ {self._digitadas}")

def main():
    try:
        print("Jogador 1")
        entrada = input("Digite a palavra > ")
        dica = input("Digite uma dica > ")
        palavra = Palavra(entrada, dica)

        jogo = Forca(palavra)
        jogo.jogar()
    except Exception as e:
        print(e)


main()