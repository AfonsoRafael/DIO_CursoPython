import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / 'usuarios.csv', 'w', encoding='utf-8', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['id','nome'])
        escritor.writerow(['1','Afonso'])
        escritor.writerow(['2','Ana'])
        escritor.writerow(['3','Jose'])
except IOError as exc:
    print("Erro ao criar o arquivo")


try:
    with open(ROOT_PATH / 'usuarios.csv', 'r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        for row in leitor:
            print(row)
except IOError as exc:
    print("Erro ao criar o arquivo")    

# Outra forma de ler o arquivo

try:
    with open(ROOT_PATH / 'usuarios.csv', 'r', encoding='utf-8', newline='')as arquivo:
        leitor = csv.DictReader(arquivo)
        for row in leitor:
            print(f"ID: {row['id']}")
            print(f"NOME: {row['nome']}")
except IOError as exc:
    print("Erro!")

# Boa pratica é usar as funçoes proprias do csv