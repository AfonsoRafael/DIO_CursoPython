contatos = {
    "afonso@gmail": {"nome": "Afonso", "telefone": "1234-5678"},
    "bruna@gmail": {"nome": "Bruna", "telefone": "8765-4321"},
    "carla@gmail": {"nome": "Carla", "telefone": "5678-1234"}
}
contatos2 = {
    "afonso@gmail": {"nome": "Afonso", "telefone": "1234-5678"},
    "bruna@gmail": {"nome": "Bruna", "telefone": "8765-4321"},
    "carla@gmail": {"nome": "Carla", "telefone": "5678-1234"}
}
print("_____________Metodos de Dicionários_____________\n")

print("_____________Metodo CLEAR_____________\n")
# clear() - Remove todos os itens do dicionário
contatos2.clear()
print("Contatos2 apos clear():", contatos2)


print("_____________Metodo COPY_____________\n")
# copy() - Retorna uma cópia rasa do dicionário
contatos_copia = contatos.copy()
print("Copia dos contatos:", contatos_copia)

print("_____________Metodo FROMKEYS_____________\n")
# fromkeys() - Cria um novo dicionário com chaves de um iterável e valores padrão
chaves = ["email1@gmail", "email2@gmail", "email3@gmail"]
novo_dicionario = dict.fromkeys(chaves, "valor padrao")
print("Novo dicionario criado com fromkeys():", novo_dicionario)

print("_____________Metodo GET_____________\n")
# get() - Retorna o valor para a chave especificada, ou um valor padrão se a chave não existir
telefone_afonso = contatos.get("afonso@gmail", {}).get("telefone", "Nao encontrado")
print("Telefone do Afonso usando get():", telefone_afonso)
telefone_desconhecido = contatos.get("desconhecido@gmail", {}).get("telefone", "Nao encontrado")
print("Telefone desconhecido usando get():", telefone_desconhecido)

print("_____________Metodo ITENS_____________\n")
# items() - Retorna uma visão dos pares chave-valor no dicionário
itens = contatos.items()
print("Itens do dicionario contatos:", itens)
for chave, valor in itens:
    print(f"Chave: {chave}, Valor: {valor}") 

print("_____________Metodo KEYS_____________\n")
# keys() - Retorna uma visão das chaves no dicionário
chaves_contatos = contatos.keys()
print("Chaves do dicionario contatos:", chaves_contatos)

print("_____________Metodo POP_____________\n")
# pop() - Remove o item com a chave especificada e retorna seu valor
telefone_bruna = contatos.pop("bruna@gmail", {}).get("telefone", "Nao encontrado")
print("Telefone da Bruna removido usando pop():", telefone_bruna)
print("Contatos apos remover Bruna:", contatos)
print("_____________Metodo POPITEM_____________\n")
# popitem() - Remove e retorna um par chave-valor arbitrário do dicionário
chave_removida, valor_removido = contatos.popitem()
print("Item removido usando popitem():", chave_removida, valor_removido)
print("Contatos apos popitem():", contatos)

print("_____________Metodo SETDEFAULT_____________\n")
# setdefault() - Retorna o valor da chave especificada. Se a chave não existir, insere a chave com o valor padrão fornecido
telefone_carla = contatos.setdefault("carla@gmail", {}).get("telefone", "Nao encontrado")
print("Telefone da Carla usando setdefault():", telefone_carla)
telefone_novo = contatos.setdefault("david@gmail", {"nome": "David", "telefone": "0000-0000"}).get("telefone")
print("Telefone do David usando setdefault():", telefone_novo)
print("Contatos apos setdefault():", contatos)

print("_____________Metodo UPDATE_____________\n")
# update() - Atualiza o dicionário com os pares chave-valor de outro dicionário ou de um iterável de pares chave-valor
contatos_update = { "eva@gmail": {"nome": "Eva", "telefone": "1111-2222"} }
contatos.update(contatos_update)
print("Contatos apos update():", contatos)

print("_____________Metodo VALUES_____________\n")
# values() - Retorna uma visão dos valores no dicionário
valores_contatos = contatos.values()
print("Valores do dicionario contatos:", valores_contatos)
for valor in valores_contatos:
    print("Valor:", valor)


print("_____________Metodo IN_____________\n")
# in - Verifica se uma chave existe no dicionário
existe_afonso = "afonso@gmail" in contatos
print("Afonso existe em contatos?", existe_afonso)
existe_bruna = "bruna@gmail" in contatos
print("Bruna existe em contatos?", existe_bruna)


print("_____________Metodo DEL_____________\n")
# del - Remove o item com a chave especificada
del contatos["afonso@gmail"]
print("Contatos apos deletar Afonso:", contatos)
