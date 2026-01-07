# Geradores são tipos especiais de iteradores que permitem a criação de sequências de valores sob demanda, economizando memória.
# São definidos usando funções que utilizam a palavra-chave 'yield' para produzir uma série de valores ao longo do tempo, em vez de retornar um único valor.

# Características principais dos geradores:
# Uma vez que um gerador é criado, ele pode ser iterado apenas uma vez. Após a iteração completa, ele não pode ser reiniciado ou reutilizado.
# O estado do gerador é mantido entre as chamadas, permitindo que ele continue de onde parou na próxima iteração.
# A execução de um gerador é pausada quando ele encontra a palavra-chave 'yield' e retomada na próxima chamada.

def meu_gerador(numeros=list[int]):
    for numero in numeros:
        yield numero * 2

# Usando o gerador
for valor in meu_gerador(1,2,3,4,5):
    print(valor)

# Em termos gerais, usar geradores quando o codigo for simples e direto, sem a necessidade de decoradores ou outras funcionalidades complexas.
# Iteradores sao ideais para trabalhar com grandes conjuntos de dados ou fluxos de dados infinitos, onde a economia de memoria e a eficiencia sao cruciais.