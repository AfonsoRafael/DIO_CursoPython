"""
 Média de Notas
Peça ao usuário para inserir notas até que ele digite -1. Em seguida, calcule e mostre a média das notas digitadas.

"""
print("""---Media de notas---
      Digite -1 para mostrar a media das notas""")
escolha = 1
nota = 0
notaF = 0
Qnotas = 0
while escolha !="-1":
    nota = float(input("Digite a nota: "))
    notaF += nota
    Qnotas +=1
    escolha = input("Deseja continuar? sair -1:  ")
media = notaF/Qnotas
print(f"A media das notas e: {media}")