def set_numero_candidato():
    while True:
        numero = input("Número > ")
        if numero.isdigit() and len(numero) == 2:
            return numero
        else: print("ERRO: Valor incorreto. Ex: 'XX'."); continue;
def set_nome_candidato():
    nome = input("Nome > ").strip().title()
    return nome
def add_candidatos(dic_candidatos: dict):
    while True:
        nome = set_nome_candidato()
        numero = set_numero_candidato()
        dic_candidatos[numero] = nome
        res = ""
        while True:
            res = input("Adicionar novamente? [s/n] > ")
            if res.lower() not in ['s','n']:
                print("Valor invalido! Digite 's' ou 'n'.")
                continue
            break
        if res.lower() == "n":
            print("== Candidatos Adicionados com Sucesso! == \n")
            break
def pega_votos(candidatos_dict, votos_dict):
    print("== Iniciando o sistema de votação! == ")
    while True:
        print("Digite '.' para sair. ")
        voto = input("Digite o número do candidato: ")
        if voto.strip() == '.':
            print("\n ** Obrigado pelo seu voto! **\n")
            break
        # Adicionando o voto no dicionanario de votos
        if voto in candidatos_dict:
            if voto not in votos_dict:
                votos_dict[voto] = 1
            else: votos_dict[voto] += 1
        else: 
            if voto.strip() == '':
                if "EmBranco" not in votos_dict:
                    votos_dict["EmBranco"] = 1
                else: votos_dict["EmBranco"] += 1
                pass
            else:
                if "Nulos" not in votos_dict:
                    votos_dict["Nulos"] = 1
                else: votos_dict["Nulos"] += 1

def exibe_votos(votos_dict, candidatos_dict):
    total_votos = sum(votos_dict.values())
    for chave in votos_dict:
        if chave.isdigit():
            porcent = round((votos_dict[chave] / total_votos) * 100, 2)
            print(f"{candidatos_dict[chave]} - Votos: {votos_dict[chave]} - Porcentagem: {porcent}%")
            

    for chave in votos_dict:
        if not chave.isdigit():
            porcent = round((votos_dict[chave] / total_votos) * 100, 2)
            print(f"{chave} - Qtd: {votos_dict[chave]} - Porcentagem: {porcent}%")
def exibe_candidatos(dict_candidatos):
    print("# Candidatos #")
    for numero in dict_candidatos:
        print(f"[{numero}] - {dict_candidatos[numero]}")

def main():
    candidatos = {}
    votos = {}

    add_candidatos(candidatos)
    exibe_candidatos(candidatos)
    pega_votos(candidatos, votos)
    exibe_votos(votos, candidatos)



main()



