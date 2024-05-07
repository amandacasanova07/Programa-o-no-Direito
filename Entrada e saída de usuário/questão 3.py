def lista_de_compras():
    # Solicitar ao usuário os itens da lista de compras
    entrada = input("Digite os itens da lista de compras, separados por vírgula: ")

    # Dividir a entrada em itens individuais usando a vírgula como separador
    itens = entrada.split(',')

    # Imprimir os itens em linhas separadas usando um laço
    print("Lista de compras:")
    for item in itens:
        print("-",item.strip())  # strip() remove espaços em branco extras ao redor do item

# Exemplo de uso da função
lista_de_compras()