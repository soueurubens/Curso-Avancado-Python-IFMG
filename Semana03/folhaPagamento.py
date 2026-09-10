import json 
from pathlib import Path
from os.path import isfile


class Funcionario:
    def conserta_tempo_servico(self, tempo): 
        if not isinstance(tempo, str):
            return tempo
        return int(tempo[0])

    def __init__(self, cpf, nome, tempo_servico,dependentes,salario):
        self._cpf = cpf
        self._nome = nome
        self._salario = salario
        self._tempo_servico = self.conserta_tempo_servico(tempo_servico)
        self._dependentes = dependentes


    def __str__(self):
        return f'[{self._cpf}] - {self._nome} - Salario Atual: R${self.salario:,.2f}\nNa empresa há:{self.tempo_servico} anos'
    

    def to_dict(self):
        return {
            "cpf": self._cpf,
            "nome": self._nome,
            "tempo_servico": self._tempo_servico,
            "dependentes": self._dependentes,
            "salario": self._salario
        }

    @property
    def cpf(self):
        return self._cpf
    @property
    def salario(self):
        return self._salario
    @property
    def tempo_servico(self):
        return self._tempo_servico
    @property
    def quantidade_dependentes(self):
        return len(self._dependentes)

    @salario.setter
    def salario(self, novo_salario):
        self._salario = novo_salario

    
class Folha:
    def __init__(self):
        self._file_path = Path(r'PythonAvançado\Semana03\funcionarios.json')
        self._funcionarios = []
        self._folha_lista = []

        self.adiciona_funcionario_lista()

    def incluir_funcionario(self):
        print(" == INCLUINDO FUNCIONARIO == ")
        cpf = input("Digite o cpf: ");
        if not self.buscar_funcionario(cpf):
            print("Funcionario já existente.")
            return

        deps = []
        nome = input("Digite o nome: ").title().strip()
        salario = float(input("Digite o salario: "))
        tempo_servico = input("Digite o tempo de serviço (anos): ").strip()
        resp = input("Possui dependetes? (S/N)").strip().lower();
        if resp == 's':
            quantidade = int(input("Quantidade: "))
            for i in range(quantidade):
                nome_dep = input(f"Digite o nome do {i+1}° dependente: ").strip().title()
                deps.append(nome_dep)

        if nome != '':
            func = Funcionario(cpf, nome, tempo_servico, deps, salario)
            self.salva_funcionario(func)
            self._funcionarios.append(func)
            print("Funcionario adicionado com sucesso!")

    def listar(self):
        print("== Lista Funcionarios ==")
        for func in self._funcionarios:
            print(func)
            print('-'*50)

    def excluir(self, cpf_desejado):
        posicao = self.buscar_funcionario(cpf_desejado)

        if posicao == -1:
            return

        with open(self._file_path, 'r', encoding='utf-8') as file: 
            data = json.load(file)

        data.pop(posicao)
        self._funcionarios.pop(posicao)

        with open(self._file_path, 'w', encoding='utf-8') as file: 
            json.dump(data, file, ensure_ascii=False, indent=4)
        return True


    def salva_funcionario(self, funcionario):
        with open(self._file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        data.append(funcionario.to_dict())
        with open(self._file_path, 'w', encoding='utf-8') as file: 
            json.dump(data, file, ensure_ascii=False, indent=4)
        
    def adiciona_funcionario_lista(self):
        if isfile(self._file_path):
            with open(self._file_path, 'r', encoding='utf-8') as file: 
                data = json.load(file)
                self._funcionarios.extend([Funcionario(**funcionario) for funcionario in data])
            print(self._funcionarios)

    def buscar_funcionario(self, cpf_desejado):
        for cont, func in enumerate(self._funcionarios):
            if cpf_desejado == func.cpf:
                print("Encontrado!")
                print(f"Posição na lista: {cont}")
                return cont
        return -1

    def calcula_salario(self):
        if not self._funcionarios:
            return False
        self._folha_lista = self._funcionarios.copy()
        for func in self._folha_lista:
            novo_salario = func.salario + ((func.salario * 0.01) * func.tempo_servico) + (150.0 * func.quantidade_dependentes)
            func.salario = novo_salario

