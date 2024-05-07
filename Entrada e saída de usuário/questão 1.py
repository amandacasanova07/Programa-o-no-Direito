def imprimir_info(nome, idade, cidade, sep=' ', end='\n'):
    print("Nome:", nome, sep=sep, end='; ')
    print("Idade:", idade, sep=sep, end='; ')
    print("Cidade:", cidade, sep=sep, end=end)

# Exemplo de uso da função
imprimir_info("Amanda", 25, "Rio de Janeiro")