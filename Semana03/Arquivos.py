from pathlib import Path
# Caminho base 
folder_path = Path(r'PythonAvançado\Semana03\files')
folder_path.mkdir(exist_ok=True, parents=True)

contatos_file = folder_path/'contatos.txt'
# Adicionando dados
while True:
    contato = input("Contato: ").strip()
    if contato == '':
        break
    with open(contatos_file, 'a', encoding='utf-8') as file: 
        file.write(contato + '\n')

# Diferença entre read(), readline(), readlines()
with open(contatos_file, 'r', encoding='utf-8') as file:
    print("\n ========  READ ======== ")
    print(file.read())

    file.seek(0) 
    print("\n ========  READLINE ======== ")
    print(file.readline())

    file.seek(0) 
    print("\n ========  READLINES ======== ")
    print(file.readlines())



