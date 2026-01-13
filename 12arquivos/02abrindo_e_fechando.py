# Abrindo e fechando arquivos em python
"""
para abrir usamos a função open()
quando terminamos de trabalhar no arquivo 
podemos fechar usando a função close()
"""

"""
Modos de leitura do arquivo
leitura(r),gravação(w),anexar(a)

O modo de abertura deve ser escolhido de acordo com a operação que sera realizada
"""

# para ler
file = open('exemplo.txt','r')

# fechando
file.close()

# para escrever
file = open('exemplo.txt','w')

# fechando
file.close()

# para anexar conteudo a um arquivo existente
file = open('exemplo.txt','a')

# fechando
file.close()