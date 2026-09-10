import csv 
from os.path import isfile
from pathlib import Path

def line():
    print('-'*50)

class Contato:
    # Campos contatos 
    campos = ['Nome', 'Telefone', 'Aniversario'];
    def __init__(self, valores):
        # Inicializa o dicionario de contatos
        self._dic = {}
        # Percorre a lista
        for cont, campo in enumerate(self.campos):
            self._dic[campo] = valores[cont]

    @classmethod
    def novo_contato(cls):
        line()
        print("== NOVO CONTATO ==")
        line()
        valores = []
        for campo in cls.campos:
            valor = input(f'{campo}: ').strip()
            if valor != '':
                valores.append(valor)
            else: valores.append('')

        # Verificando se o nome e número estão vazios
        if len(valores[0]) == 0 and len(valores[1]) == 0:
            print("Contato inválido, o nome é obrigatorio.")
            return None
        else: 
            return Contato(valores)



        

    def alterar(self):
        line()
        print("== ALTERAR CONTATO ==")
        line()
        # Percorre campos do dicionanario 
        for campo, valor in self._dic.items():
            # Mostra campo 
            print(f'{campo} -> {valor}', sep='')
            novo_valor = input("Novo valor: ").strip()  
            if novo_valor != '':
                self._dic[campo] = novo_valor
            
    @property
    def valores(self):
        lista_valores = []
        for campo in self.campos:
            lista_valores.append(self._dic[campo])
        return lista_valores

    
    def __str__(self):
        lista_csv = [campo + ': ' + self._dic[campo] for campo in self._dic]
        return '\n'.join(lista_csv)

    def __lt__(self, other):
        return tuple(self.valores) < tuple(other.valores)

class Arquivo:
    def __init__(self, nome_arquivo='Contatos.txt'):
        self._nome_arquivo = nome_arquivo
        self._lista_contatos = []

        self.cria_arquivo(nome_arquivo)

    def cria_arquivo(self, nome_arquivo:str):
        # Cria a pasta
        folder_path = Path(r'PythonAvançado\Semana03\ContatosFolder')
        folder_path.mkdir(exist_ok=True, parents=True)
        # Criando o arquivo
        file_name = nome_arquivo.strip().lower()
        file_path = folder_path / file_name
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('Nome,Telefone,Aniversario\n')
    def listar(self):
        if len(self._lista_contatos) == 0:
            print("Lista de contatos está vazia.")
        else:
            for cont, contato in enumerate(self._lista_contatos):
                print(f'Código: {cont}')
                print(str(contato))
                line()
    def buscar(self, codigo):
        if 0 <= codigo and codigo < len(self._lista_contatos):
            return self._lista_contatos[codigo]
        
    def adicionar_contato(self):
        contato = Contato.novo_contato()
        if contato is not None:
            self._lista_contatos.append(contato)

    def excluir(self, codigo):
        if 0 <= codigo and codigo < len(self._lista_contatos):
            self._lista_contatos.pop(codigo)

    def salvar(self):
        file_path = Path(r'PythonAvançado\Semana03\ContatosFolder\contatos.txt')
        # Abrindo o arquivo para salvar a lista de contatow
        with open(file_path, 'a', encoding='utf-8') as file:
            escritor = csv.writer(file)
            escritor.writerows(contato.valores for contato in self._lista_contatos)

arquivo = Arquivo()



