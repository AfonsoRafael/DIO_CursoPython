import functools
# Decoradores com argumentos
print("-----------------------------------------------")
print("Exemplo 4: Decoradores com argumentos")
def decorador_com_args(func):
    @functools.wraps(func) # TODO:Mantem o nome e docstring da funcao original, importante para debug e documentacao
    def envelope_com_args(*args, **kwargs):
        print("Antes da execucao da funcao decorada com argumentos.")
        resultado = func(*args, **kwargs) # Chama a funcao original com seus argumentos
        print("Depois da execucao da funcao decorada com argumentos.")
        return resultado
    return envelope_com_args
@decorador_com_args
def minha_funcao_com_args(nome, idade):
    print(f"Oi {nome}, voce tem {idade} anos!")
    return idade * 2 # Retorna o dobro da idade, precisa ser capturado no decorador para ser retornado corretamente
retorno = minha_funcao_com_args("Ana", 30)
print(f"Retorno da funcao decorada com argumentos: {retorno}") 
minha_funcao_com_args("Bruno", 25)
print("-----------------------------------------------")

print(minha_funcao_com_args.__name__)  # Verifica se o nome da funcao foi preservado

