"""
 Pirâmide de Números
Peça um número N e imprima uma pirâmide de números como no exemplo para N=5:

text
1
22
333
4444
55555

"""
print("---Piramide de numeros---")
n= int(input("Digite um numero para formar a piramide: "))

for i in range(1,n+1):
    print(f"{i}"*i)