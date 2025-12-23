class SistemaEstoque:
    def __init__(self):
        """Inicializa o estoque como um conjunto vazio"""
        self.estoque = set()
    
    def adicionar_produto(self, produto):
        """
        Adiciona um produto ao estoque.
        
        Args:
            produto (str): Nome do produto a ser adicionado
        
        Returns:
            str: Mensagem indicando o resultado da operação
        """
        if produto in self.estoque:
            return f"Produto '{produto}' já existe no estoque."
        else:
            self.estoque.add(produto)
            return f"Produto '{produto}' adicionado ao estoque."
    
    def remover_produto(self, produto):
        """
        Remove um produto do estoque apenas se existir.
        
        Args:
            produto (str): Nome do produto a ser removido
        
        Returns:
            str: Mensagem indicando o resultado da operação
        """
        if produto in self.estoque:
            self.estoque.remove(produto)
            return f"Produto '{produto}' removido do estoque."
        else:
            return f"Produto '{produto}' não encontrado no estoque."
    
    def verificar_disponibilidade(self, produto):
        """
        Verifica se um produto está disponível no estoque.
        
        Args:
            produto (str): Nome do produto a verificar
        
        Returns:
            bool: True se disponível, False caso contrário
        """
        return produto in self.estoque
    
    def mostrar_produtos(self):
        """
        Mostra todos os produtos do estoque em ordem alfabética.
        
        Returns:
            list: Lista de produtos ordenados alfabeticamente
        """
        produtos_ordenados = sorted(self.estoque)
        return produtos_ordenados
    
    def mostrar_estoque(self):
        """
        Mostra uma representação formatada do estoque.
        
        Returns:
            str: String formatada com os produtos do estoque
        """
        if not self.estoque:
            return "Estoque vazio."
        
        produtos_ordenados = sorted(self.estoque)
        resultado = "Produtos no estoque:\n"
        for i, produto in enumerate(produtos_ordenados, 1):
            resultado += f"{i}. {produto}\n"
        return resultado.strip()


# Exemplo de uso do sistema
def demonstracao_sistema():
    print("=== SISTEMA DE CONTROLE DE ESTOQUE ===\n")
    
    # Cria uma instância do sistema
    sistema = SistemaEstoque()
    
    # Demonstração das funcionalidades
    print("1. Adicionando produtos ao estoque:")
    print(sistema.adicionar_produto("Notebook"))
    print(sistema.adicionar_produto("Mouse"))
    print(sistema.adicionar_produto("Teclado"))
    print(sistema.adicionar_produto("Monitor"))
    print(sistema.adicionar_produto("Mouse"))  # Tentativa de adicionar duplicado
    print()
    
    print("2. Verificando disponibilidade:")
    print("Mouse está disponível?", sistema.verificar_disponibilidade("Mouse"))
    print("Webcam está disponível?", sistema.verificar_disponibilidade("Webcam"))
    print()
    
    print("3. Mostrando estoque em ordem alfabética:")
    print(sistema.mostrar_estoque())
    print()
    
    print("4. Removendo produtos:")
    print(sistema.remover_produto("Mouse"))
    print(sistema.remover_produto("Fone de ouvido"))  # Produto que não existe
    print()
    
    print("5. Estoque após remoção:")
    print(sistema.mostrar_estoque())
    print()
    
    print("6. Lista ordenada de produtos:")
    produtos = sistema.mostrar_produtos()
    print(f"Produtos: {', '.join(produtos)}")
    print()
    
    print("7. Testando conjunto para evitar duplicatas:")
    sistema.adicionar_produto("Notebook")  # Já existe
    sistema.adicionar_produto("notebook")  # Diferente (case sensitive)
    print(sistema.mostrar_estoque())


# Versão simplificada (sem classes) para entendimento
def sistema_estoque_simplificado():
    """
    Versão simplificada usando apenas funções
    """
    estoque = set()
    
    def adicionar_produto(produto):
        if produto in estoque:
            return f"'{produto}' já existe."
        estoque.add(produto)
        return f"'{produto}' adicionado."
    
    def remover_produto(produto):
        if produto not in estoque:
            return f"'{produto}' não encontrado."
        estoque.remove(produto)
        return f"'{produto}' removido."
    
    def verificar_produto(produto):
        return produto in estoque
    
    def listar_produtos():
        return sorted(estoque)
    
    # Teste rápido
    print("=== SISTEMA SIMPLIFICADO ===")
    print(adicionar_produto("Cadeira"))
    print(adicionar_produto("Mesa"))
    print(adicionar_produto("Cadeira"))  # Duplicado
    print("Mesa disponível?", verificar_produto("Mesa"))
    print("Produtos:", listar_produtos())
    print(remover_produto("Mesa"))
    print("Produtos após remoção:", listar_produtos())


# Executar demonstrações
if __name__ == "__main__":
    print("=" * 50)
    demonstracao_sistema()
    print("\n" + "=" * 50 + "\n")
    sistema_estoque_simplificado()