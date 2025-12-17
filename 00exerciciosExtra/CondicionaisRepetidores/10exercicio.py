# Verifique se um número fornecido pelo usuário é primo ou não.

print("---Verificacao de numero primo---")
n = int(input("Digite um numero e verifique se e primo: ").strip())
primo = True
for i in range(2,n):
    if n%i == 0:
        primo = False 

if primo == True :
    print(f"O numero {n} e primo!")
else:
    print(f"O numero {n} nao e primo")