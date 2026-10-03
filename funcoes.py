
#Função com retorno e parametros
def somar(n1, n2):       # Declaração da Função 
    resultado = n1 + n2  # Processamento logico da função.
    return resultado     # retorno/saida


valor_somado = somar(5,5) # Invocação da função passando valor de parametros. 


print(valor_somado)





#função sem retorno e com parametros

def mensagem(nome):
    print("Bom dia,  " + nome)



nome = mensagem(input("Digite seu nome : "))


#Funcção sem parametro com retorno 

def aplaudir():
    return "Estou aplaudindo"

print(aplaudir())


#Função sem parametro sem retorno 

def latir():
    print("Au Au AU")


latir()


# tem funções do proprio python 

# COMO A input() ou sum() ou print() etc..  FUNÇÕES JA CONSTRUIDA PELO PYTHON



