def digitar_nomes():
    nomes = []  # Lista para armazenar os nomes digitados

    while True:
        nome = input("Digite um nome (ou 'sair' para encerrar): ")
        
        # Verificar se o usuário digitou 'sair'
        if nome.lower() == 'sair':
            break  # Sai do loop
        
        nomes.append(nome)  # Adiciona o nome à lista
    
    # Imprime todos os nomes digitados, um por linha
    for nome in nomes:
        print(nome)

# Exemplo de uso da função
digitar_nomes()
