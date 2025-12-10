# Entrada do usuário
email = input("Digite um email valido: ").strip()

if "@" in email and not email.startswith("@") and not email.endswith("@") and " " not in email:
  if email.endswith("@gmail.com") or email.endswith("@outlook.com"):
    print("E-mail válido")
else:
  print("E-mail inválido")
# TODO: Verifique as regras do e-mail: