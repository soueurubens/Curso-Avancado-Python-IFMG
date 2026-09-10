from os.path import isfile
from pathlib import Path

def linha():
    print('-'*50)

class Campeonato: 
    def __init__(self):
        self.__jogos_path = Path(r'PythonAvançado\Semana03\Campeonato\jogos')
        self.__times_path = Path(r'PythonAvançado\Semana03\Campeonato\times')

        self._dic_times = {}
        self._list_jogos = []


    def incluir_time(self):
        linha()
        print("== ADICIONAR UM TIME ==")
        linha()

        time = input("Nome do time: ").title().strip()
        if time == '':
            return
        if time in self._dic_times.keys():
            print("Time já existente!");
            return
        self._dic_times[time] = 0
        self.salva_time()
        print(f'{time} adicionando com sucesso!\n')
        

    def incluir_jogo(self):
        linha()
        print("== ADICIONAR UM JOGO ==")
        linha()

        time_casa = input("Time de casa: ").title().strip()
        qtd_gols_casa = input("Quantidade de gols: ")
        time_visitante = input("Time vistante: ").title().strip()
        qtd_gols_vistante = input("Quantidade de gols: ")

        if time_casa not in self._dic_times and time_visitante not in self._dic_times:
            print("Jogo inválido.")     
            return
        
        self._list_jogos.append({(time_casa, time_visitante):(qtd_gols_casa,qtd_gols_vistante)})
        self.salva_jogos()
        print("Jogo registrado com sucesso!\n")


    def salva_time(self):
        file_path = self.__times_path / 'times.txt'
        with open(file_path, 'w', encoding='utf-8') as file:
            for time, pontos in self._dic_times.items():
                file.write(f'{time}: {pontos}\n')

    def salva_jogos(self):
            file_path = self.__jogos_path / 'jogos.csv'
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write('time_casa,time_visitante,gols_casa,gols_visitante\n')
                for jogo in self._list_jogos:
                    for (casa, visitante), (gols_casa, gols_visitante) in jogo.items():
                        file.write(f'{casa},{visitante},{gols_casa},{gols_visitante}\n')

    def soma_pontos(self):
        file_jogos = Path(r'PythonAvançado\Semana03\Campeonato\jogos\jogos.csv')
        with open(file_jogos, 'r', encoding='utf-8') as file:
            file.readline()
            for linha in file:
                # Pegando os dados
                linha_data = linha.split(',')
                time_casa = linha_data[0]
                time_vis = linha_data[1]
                gols_casa = linha_data[2]
                gols_vis = linha_data[3]

                # Empate
                if gols_casa == gols_vis:
                    if time_casa in self._dic_times and time_vis in self._dic_times:
                        self._dic_times[time_casa] += 1
                        self._dic_times[time_vis] += 1

                # Vitoria diferença
                if gols_vis != gols_casa:
                    if gols_vis > gols_casa: self._dic_times[time_vis] += 3;
                    else: self._dic_times[time_casa] += 3
            print(self._dic_times)


                













