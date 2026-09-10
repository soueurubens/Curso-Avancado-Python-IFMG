from pathlib import Path
import random

# Escolhendo uma palavra aleatoria 
file_path = Path(r'PythonAvançado\Semana03\palavras\palavras.txt')

with open(file_path, 'r', encoding='utf-8') as file: 
    palavras = [palavra.strip() for palavra in file.readlines()]
    rand_indx = random.randint(0, len(palavras))
    palavra_escolhida = palavras[rand_indx]
    print(f"A Palavra escolhida foi: {palavra_escolhida}")
