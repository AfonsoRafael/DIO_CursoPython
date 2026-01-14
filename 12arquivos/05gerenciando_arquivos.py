import os
import shutil
from pathlib import Path 

#ROOT_PATH = Path(__file__) # Para retornar o caminho do arquivo

#ROOT_PATH.parent # Retorna uma camada acima, ou seja a pasta em que esse arquivo esta

ROOT_PATH = Path(__file__).parent 

# Criando um novo diretorio
# os.mkdir(ROOT_PATH / "novo_diretorio")  # So executa uma vez, uma vez criado não cria de novo


# arquivo = open(ROOT_PATH / "novo.txt","w")
# arquivo.close()

# Renomeando um arquivo
# os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "novo_nome.txt")

# removendo um arquivo
#os.remove(ROOT_PATH / "novo_nome.txt")

# movendo para uma nova pasta
# shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo_diretorio" / "novo.txt")