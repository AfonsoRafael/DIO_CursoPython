# Metodos de Classe
# Metodos de classe sao aqueles que sao declarados com o decorador @classmethod. Eles recebem como primeiro parametro a propria classe (geralmente nomeada como cls) em vez de uma instancia da classe (self). Metodos de classe sao usados para definir comportamentos que estao relacionados à classe como um todo, em vez de a instancias individuais.
#Metodos de classe sao frequentemente usados para criar metodos de fabrica, que sao metodos que retornam instancias da classe com base em diferentes conjuntos de parametros.
# Metodos Staticos
# Metodos estaticos sao declarados com o decorador @staticmethod. Eles nao recebem automaticamente nem a instancia (self) nem a classe (cls) como primeiro parametro. Metodos estaticos sao usados para definir funcoes que estao relacionadas à classe, mas nao dependem do estado da instancia ou da classe. Eles funcionam como funcoes comuns, mas sao agrupados dentro da classe para melhor organizacao e encapsulamento.


# Diferenca entre metodos de classe e metodos estaticos:
# Metodos de classe recebem a classe como primeiro parametro e podem acessar e modificar o estado da classe. Metodos estaticos nao recebem automaticamente nem a instancia nem a classe como parametro e nao podem acessar ou modificar o estado da instancia ou da classe.


# Quando usar cada um:
# Use metodos de classe quando precisar acessar ou modificar o estado da classe, ou quando estiver criando metodos de fabrica. Use metodos estaticos quando precisar de uma funcao que esteja relacionada à classe, mas nao dependa do estado da instancia ou da classe.