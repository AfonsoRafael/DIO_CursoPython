# Para escrever no arquivo usamos o write() e o writelines()

arquivo = open(r"C:\Users\Windows\Desktop\ciencia da computação\DIO\DIO_CursoPython\12arquivos\teste.txt","w")
arquivo.write("Escrevendo dados em um novo arquivo") # escreve uma linha
arquivo.writelines(["\n","Escrevendo","\n","um","\n","novo","\n","texto"]) # itera sobre uma lista de linhas
arquivo.close()