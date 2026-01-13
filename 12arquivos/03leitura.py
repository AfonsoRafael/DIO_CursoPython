# podemos usar o read(), readline() e readlines() para ler o arquivo conforme necessidade

arquivo = open(r"C:\Users\Windows\Desktop\ciencia da computação\DIO\DIO_CursoPython\12arquivos\lorem.txt","r")
print(arquivo.read())
arquivo.close()

print("_____________________________________________________________________\n\n\n\n")

# o metodo readline le uma linha por vez


arquivo = open(r"C:\Users\Windows\Desktop\ciencia da computação\DIO\DIO_CursoPython\12arquivos\lorem.txt","r")
print(arquivo.readline())
arquivo.close()

print("_____________________________________________________________________\n\n\n\n")

# o metodo readlines retorna uma lista onde cada elemento é uma linha do arquivo

arquivo = open(r"C:\Users\Windows\Desktop\ciencia da computação\DIO\DIO_CursoPython\12arquivos\lorem.txt","r")
print(arquivo.readlines())
arquivo.close()

print("_____________________________________________________________________\n\n\n\n")

# o metodo readlines dica para iterar

arquivo = open(r"C:\Users\Windows\Desktop\ciencia da computação\DIO\DIO_CursoPython\12arquivos\lorem.txt","r")
while len(linha := arquivo.readlines()):
    print(linha)
arquivo.close()