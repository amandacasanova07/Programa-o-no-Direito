def celsius_para_fahrenheit():
    # Solicitar ao usuário a temperatura em graus Celsius
    celsius = float(input("Digite a temperatura em graus Celsius: "))

    # Converter Celsius para Fahrenheit usando a fórmula
    fahrenheit = (celsius * 9/5) + 32

    # Imprimir o resultado da conversão
    print("A temperatura em Fahrenheit é:", fahrenheit)

# Exemplo de uso da função
celsius_para_fahrenheit()
