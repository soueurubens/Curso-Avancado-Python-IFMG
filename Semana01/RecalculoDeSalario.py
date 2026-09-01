def pega_salario():
    while True:
        try:
            salario = float(input("Salario Atual > R$ "))
            if salario <= 0:
                print("Salario não pode ser negativo!")
                continue
            return salario
        except:
            print("Informe o valor novamente!")

def pega_funcioanario():
    nome_entrada = input("Nome do Funcionario >")
    if nome_entrada == '':
        return None
    salario = pega_salario()
    return (nome_entrada, salario)


def pega_total(lista_funcionarios):
    total = 0
    for funcionario in lista_funcionarios:
        total += funcionario[1]
    return total


def aumenta_salario(lista_funcionarios):
    for count, funcionario in enumerate(lista_funcionarios):
        nome, salario = funcionario

        if salario >= 5000.0:
            salario += (salario * (5/100))
        elif salario > 2000:
            salario += (salario * (15/100))
        else:salario += (salario * (20/100))

        lista_funcionarios[count] = (nome, salario)
    return lista_funcionarios

def main():
    lista_funcionarios = []
    total_antigo = 0
    total_novo = 0
    
    while True:
        funcionario = pega_funcioanario()
        if not funcionario:
            break
        lista_funcionarios.append(funcionario)
    total_antigo = pega_total(lista_funcionarios)
    lista_funcionarios = aumenta_salario(lista_funcionarios)
    total_novo = pega_total(lista_funcionarios)

    
    print(f"Diferença Total: {total_novo - total_antigo}")
    print("== Funcionarios com salariaos abaixo de R$2000.0 == ")
    for nome, salario in lista_funcionarios:
        if salario < 2000:
            print(f"Nome: {nome} - Salario Atual {salario}")



main()
