#Para informar que o programa calculadora foi iniciado. 
print("CALCULADORA INICIADA ....")

# Começa com "s" para o laço rodar pelo menos uma vez
continuar = "s"

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    
    return a / b


while continuar == "s":
    # Menu de opções para o usuario
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    # variavel que vai guardar a escolha do usuario
    operacao = input("Escolha a operação: ")

    # variaveis que vai guardar os numeros que o usuario deseja fazer a operação:
    n1 = float(input("Primeiro número: "))
    n2 = float(input("Segundo número: "))


    #estrutura condicionais para identificar o numero digitado e fazer o processamento de acordo com a escolha desejada do usuario
    if operacao == "1":
        resultado = somar(n1, n2)       
        print("Resultado: " + str(resultado))
    elif operacao == "2":
        resultado = subtrair(n1, n2)                     
        print("Resultado: " + str(resultado))
    elif operacao == "3":
        resultado = multiplicar(n1, n2)                   
        print("Resultado: " + str(resultado))
    elif operacao == "4":
        if n2 == 0:
            print("Não é possível dividir por zero.")
        else:
            resultado = dividir(n1, n2)                 
            print("Resultado: " + str(resultado))
    else:
        print("Operação inválida.")

    # Atualiza a variável usada pelo while
    continuar = input("Deseja realizar outra operação? (s/n) ")

print("Calculadora encerrada.")