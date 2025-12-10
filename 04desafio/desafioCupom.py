# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}
print("""
----------------------------------------
Sistema de Cupons de Desconto
Cupons disponíveis:
      - DESCONTO10: 10% de desconto
      - DESCONTO20: 20% de desconto
      - SEM_DESCONTO: Sem desconto
----------------------------------------""")
# Entrada do usuário
preco = float(input("Digite o preco: ").strip())
cupom = input("Digite o cupom de Desconto: ").strip()

cupom = cupom.upper()
if cupom == "DESCONTO10":
  preco = preco-(preco * descontos["DESCONTO10"])
  print(f"{preco:.2f}")
elif cupom == "DESCONTO20":
  preco = preco-(preco*descontos["DESCONTO20"])
  print(f"{preco:.2f}")
elif cupom == "SEM_DESCONTO":
  preco = preco-(preco*descontos["SEM_DESCONTO"])
  print(f"{preco:.2f}")
else:
  print("Sem cupom")
# TODO: Aplique o desconto se o cupom for válido: