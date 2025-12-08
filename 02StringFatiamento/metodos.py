# Principais metodos da classe str
frase = "      Curso em Video Python       "
print(frase.replace("Python", "Android"))  # Substitui "Python" por "Android"
print(frase.upper())  # Converte todos os caracteres para maiúsculas
print(frase.lower())  # Converte todos os caracteres para minúsculas
print(frase.capitalize())  # Coloca a primeira letra em maiúscula e o resto em minúsculas
print(frase.title())  # Coloca a primeira letra de cada palavra em maiúscula
print(frase.strip())  # Remove espaços em branco no início e no fim
print(frase.split())  # Divide a string em uma lista de palavras
print(frase.lstrip())  # Remove espaços em branco no início
print(frase.rstrip())  # Remove espaços em branco no fim
print(frase.center(40,"-"))  # Centraliza a string em um campo de largura 30
print(frase.count("o"))  # Conta quantas vezes "o" aparece na string
print(frase.find("Video"))  # Retorna o índice da primeira ocorrência de "Video
print("Curso" in frase)  # Verifica se "Curso" está na string
print(frase.index("em"))  # Retorna o índice da primeira ocorrência de "em"
print(frase.isalpha())  # Verifica se todos os caracteres são letras
print(".".join(frase))  # Junta os caracteres da string com "." entre eles