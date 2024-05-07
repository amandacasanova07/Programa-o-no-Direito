def calcular():
    # Pedir ao usuário dois números e a operação desejada
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (+, -, *, /): ")

    # Calcular o resultado com base na operação especificada
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        # Verificar divisão por zero
        if num2 == 0:
            print("Erro: divisão por zero!")
            return
        resultado = num1 / num2
    else:
        print("Operação inválida!")
        return

    # Imprimir o resultado da operação
    print("Resultado:", resultado)

# Exemplo de uso da função
calcular()
