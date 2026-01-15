from pathlib import Path

ROOT_PATH  = Path(__file__).parent

try:
    with open(ROOT_PATH / 'lorem.txt','r') as arquivo: # with faz com que o arquivo se feche automaticamente apos o uso
        print(arquivo.read())
except IOError as exc: # Importante envolver com esse erro pois ele garante o erro possivel
    print(f"Arquivo nao abriu: {exc}")

# importante colocar a codificação tambem
try:                                        # Valor da codificacao
    with open(ROOT_PATH / "teste.txt", "r" , encoding="ascii") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Arquivo nao abriu: \n{exc}")
except UnicodeDecodeError as exc:
    print(f"Esse arquivo possui valor diferente da condificacao: \n{exc}")

try:                                        # Valor da codificacao
    with open(ROOT_PATH / "teste.txt", "r" , encoding="utf-8") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Arquivo nao abriu: \n{exc}")
except UnicodeDecodeError as exc:
    print("Esse arquivo possui valor diferente da condificacao: \n{exc}")