"""
 Validação de Senha
Crie um programa que peça uma senha ao usuário e só permita continuar quando a senha correta for digitada (defina uma senha fixa). Dê no máximo 3 tentativas."""

senha = "vasco"
chance = 3
c = False

while chance>0 and c == False:
    d = input("Digite a senha: ").strip()
    if senha == d:
        print("Parabens, a senha esta correta")
        c = True
    else:
        print("Tente novamente")
        chance -=1

if c ==False:
    print("Voce excedeu o limite de tentativas")