from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Sempre pode ocorrer erros, por isso é excencial que seja feito o tratamento dele

# FileNotFoundError é usado quando um arquivo que esta sendo aberto não pode ser encontrado

try:
    arquivo = open("nao_existe.txt")
except FileNotFoundError as exc: # Esse exc captura detalhes do erro
    print("Arquivo nao encontrado")
    print(exc)

# PermissionError é quando tenta abrir um arquivo e não tem permissão necessaria para ler ou gravar

# IOError é um erro geral de entrada e saida, como problemas de permissao, de armazenamento entre outros

# UnicodeDecodeError é quando tenta decodificar os dados e usa uma codificação inadequada(lendo o arquivo)

# UnicodeEncodeError é quando tenta codificar o arquivo e ao gravar gera erro(gravando o arquivo)

# IsADirectoryError é lançado quanto tenta abrir um diretorio em vez de arquivo

try:
    arquivo = open(ROOT_PATH / "novo_diretorio")
except IsADirectoryError as exc: # Boa pratica especificar 
    print(f"Nao foi possivel abrir esse arquivo: {exc}")
except Exception: # Erro generico
    print("Algum erro ocorreu")